from app.index_lib import *
from branca.colormap import StepColormap

st.set_page_config( layout="wide", initial_sidebar_state="expanded")
sidebar_setting = st.markdown(
                                """
                                <style>
                                    .css-1fkbmr9 {
                                                background-color: rgb(245, 245, 245);
                                                background-attachment: fixed;
                                                flex-shrink: 0;
                                                height: calc(100vh - 2px);
                                                top: 0px;
                                                width: 17rem;
                                                z-index: 999991;
                                                margin-left: 0px;
                                                }
                                </style>
                                """,
                                unsafe_allow_html=True,
                            )
sidebar_expand_hide = st.markdown(
                                    """
                                    <style>
                                        .css-1o0o1ai {
                                                    visibility: hidden;
                                                    }
                                    </style>
                                    """,
                                    unsafe_allow_html=True,
                                )
    #sidebar logo
st.sidebar.image('app/assets/logo/Nodpy2.png')

    #sidebar main menu


hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

reduce_header_height_style = """
            <style>
                div.block-container {padding-top:0rem;}
            </style>
        """
st.markdown(reduce_header_height_style, unsafe_allow_html=True)



with st.sidebar:
    selected = option_menu("Main Menu",["Preacquisition", "Interpretation", "About"],
                            icons=["file","compass","megaphone"],
                            menu_icon="cast",
                            default_index=0
                            )

pre_map = folium.Map(tiles='StamenTerrain',location=[-1.609972, 103.607254], zoom_start=6)
df_map = pd.read_csv("app/assets/data/Geology+Jambi4.csv")
df_map1 = df_map[["SYMBOLS","IDX_FORMATION"]]
state_geo = "app/assets/data/Geology+Jambi.geojson"
df_map2 = pd.read_csv("app/assets/data/GeologyJambieditcolor.csv")
df_map3 = df_map2[["CLR_IDX"]]
geojson = gpd.read_file(state_geo)
geojson_states = list(geojson.SYMBOLS.values)
final_df = geojson.merge(df_map, on="SYMBOLS")
map_dict = df_map1.set_index('SYMBOLS')['IDX_FORMATION'].to_dict()
color_scale = LinearColormap(['darkblue','brown','blue','green','skyblue','purple','pink','cadetblue','aqua','green','lime',
                            'turquoise','blue','orange','yellow','seagreen','red','maroon','midnightblue',
                            'aquamarine','azure','navy','teal','beige','darkgreen',], vmin = min(map_dict.values()), vmax = max(map_dict.values()))
def get_color(feature):
    value = map_dict.get(feature['properties']['SYMBOLS'])
    if value is None:
        return '#8c8c8c' # MISSING -> gray
    else:
        return color_scale(value)

if selected=="Preacquisition":
    st.header("Preacquisition")
    st.markdown("---")

    cols = st.columns([5,2])
    with cols[1]:
        st.subheader("SetBox")
        upload_pre = st.file_uploader("choose your file")
        with st.expander("Set your map", expanded=True):
            st.subheader("Marker")
            st.write("For all of digital maps")
            loc_num_lat = st.number_input("Mark your latitude")
            loc_num_long = st.number_input("Mark your longitude")
            st.subheader("Slider")
            st.write("Just for geology map")
            geology_map_slider = st.slider('Set your geology map transparency', 0.0,1.0)
        if upload_pre is not None :
            data_pre = pd.read_csv(upload_pre)
            coordinate_data = data_pre
            coordinate_data = coordinate_data.dropna(subset=['Latitude'])
            coordinate_data = coordinate_data.dropna(subset=['Longitude'])
            for i in range(len(coordinate_data)):
                folium.Marker(location=[coordinate_data.iloc[i]['Latitude'], coordinate_data.iloc[i]['Longitude']]).add_to(pre_map)
#Map Processing


    with cols[0]:
        st.subheader("Digital Map")
        #Initialize 
    
        

        
        folium.Marker(location=[loc_num_lat, loc_num_long]).add_to(pre_map)

        
            
            #base tile map
        Esri_Satellite = folium.TileLayer(
                                                                tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                                                attr = 'Esri',
                                                                name = 'Esri Satellite',
                                                                overlay = True,
                                                                control = True
                                                                ).add_to(pre_map)
        Google_Satellite_Hybrid =  folium.TileLayer(
                                                                tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                                                                attr = 'Google',
                                                                name = 'Google Satellite',
                                                                overlay = True,
                                                                control = True
                                                                ).add_to(pre_map)
        Google_Terrain = folium.TileLayer(
                                                                tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                                                                attr = 'Google',
                                                                name = 'Google Terrain',
                                                                overlay = True,
                                                                control = True
                                                                ).add_to(pre_map)
        Google_Satellite = folium.TileLayer(
                                                                tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                                                                attr = 'Google',
                                                                name = 'Google Satellite',
                                                                overlay = True,
                                                                control = True
                                                                ).add_to(pre_map)
        Google_Maps = folium.TileLayer(
                                                                tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                                                                attr = 'Google',
                                                                name = 'Google Maps',
                                                                overlay = True,
                                                                control = True
                                                                ).add_to(pre_map)

        n = folium.GeoJson(
                            name= 'Geology Map',
                            data = state_geo,
                            
                            style_function = lambda feature: {
                                                                'fillColor': get_color(feature),
                                                                'fillOpacity': geology_map_slider,
                                                                'color' : 'black',
                                                                'weight' : 0,
                                                            }    
                                        ).add_to(pre_map)
            #Layer control
        folium.LayerControl().add_to(pre_map)
            
            #Fullscreeen
        plugins.Fullscreen().add_to(pre_map)

            #Locate Control
        plugins.LocateControl().add_to(pre_map)
            #Locate Control
                    
                    
                    #Cursor Postion
        fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",lat_formatter=fmtr, lng_formatter=fmtr).add_to(pre_map)
                    
                    #Add the draw 
        plugins.Draw(export=True, filename='data.geojson', position='topleft', draw_options=None, edit_options=None).add_to(pre_map)
                    
                    #Measure Control
        plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(pre_map)
        st_folium(pre_map, width=700)

if selected=="Interpretation":
    st.header("Interpretation")
    st.markdown("---")
    number_of_tabs = st.sidebar.number_input("Number of Tabs", min_value=1, max_value=16, value=1)
    number_of_tabs = int(number_of_tabs)
    int_map = folium.Map(tiles='StamenTerrain',location=[-1.609972, 103.607254], zoom_start=6)
    with st.container():
        cols = st.columns([5,2])
        with cols[1]:
            st.subheader("Set Box")
            uploaded_files = st.file_uploader("Choose", accept_multiple_files=True)
            with st.expander("Set your map", expanded=True):
                st.subheader("Marker")
                st.write("For all of digital maps")
                loc_num_lat1 = st.number_input("Mark your latitude")
                loc_num_long1 = st.number_input("Mark your longitude")
                st.subheader("Slider")
                st.write("Just for geology map")
                geology_map_slider1 = st.slider('Set your geology map transparency', 0.0,1.0)

            
        
   
        with cols[0]:
            st.subheader("Digital Map")
            folium.Marker(location=[loc_num_lat1, loc_num_long1]).add_to(int_map)
            #base tile map
            Esri_Satellite = folium.TileLayer(
                                                                    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                                                    attr = 'Esri',
                                                                    name = 'Esri Satellite',
                                                                    overlay = True,
                                                                    control = True
                                                                    ).add_to(int_map)
            Google_Satellite_Hybrid =  folium.TileLayer(
                                                                    tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                                                                    attr = 'Google',
                                                                    name = 'Google Satellite',
                                                                    overlay = True,
                                                                    control = True
                                                                    ).add_to(int_map)
            Google_Terrain = folium.TileLayer(
                                                                    tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                                                                    attr = 'Google',
                                                                    name = 'Google Terrain',
                                                                    overlay = True,
                                                                    control = True
                                                                    ).add_to(int_map)
            Google_Satellite = folium.TileLayer(
                                                                    tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                                                                    attr = 'Google',
                                                                    name = 'Google Satellite',
                                                                    overlay = True,
                                                                    control = True
                                                                    ).add_to(int_map)
            Google_Maps = folium.TileLayer(
                                                                    tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                                                                    attr = 'Google',
                                                                    name = 'Google Maps',
                                                                    overlay = True,
                                                                    control = True
                                                                    ).add_to(int_map)

            m = folium.GeoJson(
                                name= 'Geology Map',
                                data = state_geo,
                                
                                style_function = lambda feature: {
                                                                    'fillColor': get_color(feature),
                                                                    'fillOpacity': geology_map_slider1,
                                                                    'color' : 'black',
                                                                    'weight' : 0,
                                                                }    
                                            ).add_to(int_map)
                #Layer control
            folium.LayerControl().add_to(int_map)
                
                #Fullscreeen
            plugins.Fullscreen().add_to(int_map)

                #Locate Control
            plugins.LocateControl().add_to(int_map)
                #Locate Control
                        
                        
                        #Cursor Postion
            fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
            plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",lat_formatter=fmtr, lng_formatter=fmtr).add_to(int_map)
                        
                        #Add the draw 
            plugins.Draw(export=True, filename='data.geojson', position='topleft', draw_options=None, edit_options=None).add_to(int_map)
            folium.GeoJsonTooltip(['SYMBOLS', 'CLASS_LITH'], sticky=True).add_to(m)         
                        #Measure Control
            plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(int_map)
            for uploaded_file in uploaded_files:
        
                coordinate_data = pd.read_csv(uploaded_file)
                coordinate_data = coordinate_data.dropna(subset=['Latitude'])
                coordinate_data = coordinate_data.dropna(subset=['Longitude'])
                for i in range(len(coordinate_data)):
                    folium.Marker(location=[coordinate_data.iloc[i]['Latitude'], coordinate_data.iloc[i]['Longitude']]).add_to(int_map)
            st_folium(int_map, width=700)
            
        
        
        tabs = st.tabs([f"tab{i+1}" for i in range(number_of_tabs)])
        for i in range(number_of_tabs):
            with tabs[i]:
                st.subheader("Resistivity")
                
                upload = st.file_uploader(f"tab{i+1}")
                
                number_scale_of_bar = st.number_input(f"tab{i+1}", min_value=12, max_value=25)
                if upload is not None:
                    data = pd.read_csv(upload)
                        #input
                    filein = data  
                    ncolours=number_scale_of_bar
                    colourscheme='Spectral_r' 
                    #Resistivity
                    rhos_min = filein['Resistivity'].min()
                    rhos_max = filein['Resistivity'].max()
                            

                    clevels_res = np.logspace(np.log10(np.min(rhos_min)),np.log10(np.max(rhos_max)),num=ncolours)
                    fig, axes_res = plt.subplots( nrows=2, sharex=False, squeeze=True, sharey=True)

                    for ax in axes_res:
                        x=filein['X']
                        z=filein['Depth']
                        rho=filein['Resistivity']
                        triang = mpl.tri.Triangulation(x, z)
                        mask = mpl.tri.TriAnalyzer(triang).get_flat_tri_mask()
                        triang.set_mask(mask)
                
                    
                    #plt.tricontourf(triang,rho,levels=clevels, cmap=colourscheme)
                    #cc=ax.tricontourf(triang,rho,levels=clevels, cmap=colourscheme)
                        cc=ax.tricontourf(triang,rho,levels=clevels_res, norm=mpl.colors.LogNorm(vmin=rhos_min, vmax=rhos_max), cmap=colourscheme)
                        ax.set_ylim(min(z)-2, max(z)+2)
                        ax.set_xlim(0, max(x)+2)

                        axes_res[0].set_visible(False)

                    clabels=[]
                    for c in clevels_res: 
                        clabels.append('%d' % c) 
                    thecbar=fig.colorbar(cc, ax=axes_res,format='%.5f',ticks=clevels_res, orientation="horizontal")
                    thecbar.ax.set_xticklabels(clabels, rotation=45)

                    #Conductivity
                    cond_min = filein['Cond'].min()
                    cond_max = filein['Cond'].max()
                            

                    clevels_cond = np.logspace(np.log10(np.min(cond_min)),np.log10(np.max(cond_max)),num=ncolours)
                    fig_cond, axes_cond = plt.subplots( nrows=2, sharex=False, squeeze=True, sharey=True)

                    for ax in axes_cond:
                        x=filein['X']
                        z=filein['Depth']
                        rho=filein['Cond']
                        triang = mpl.tri.Triangulation(x, z)
                        mask = mpl.tri.TriAnalyzer(triang).get_flat_tri_mask()
                        triang.set_mask(mask)
                
                    
                    #plt.tricontourf(triang,rho,levels=clevels, cmap=colourscheme)
                    #cc=ax.tricontourf(triang,rho,levels=clevels, cmap=colourscheme)
                        cc_cond=ax.tricontourf(triang,rho,levels=clevels_cond, norm=mpl.colors.LogNorm(vmin=cond_min, vmax=cond_max), cmap=colourscheme)
                        ax.set_ylim(min(z)-2, max(z)+2)
                        ax.set_xlim(0, max(x)+5)

                        axes_cond[0].set_visible(False)

                    clabels=[]
                    for c in clevels_cond: 
                        clabels.append('%2.4f' % c) 
                    thecbar=fig_cond.colorbar(cc_cond, ax=axes_cond,format='%.5f',ticks=clevels_cond, orientation="horizontal")
                    thecbar.ax.set_xticklabels(clabels, rotation=45)
                            
                    cols = st.columns(2)
                    with cols[0]:
                        st.pyplot(fig)
                    with cols[1]:
                        st.pyplot(fig_cond)
                    with st.container():
                        datum_file = data
                        datum_file_x = datum_file["X"]
                        datum_file_y = datum_file["Depth"]


                        datum_fig, ax = plt.subplots()
                        ax.plot(datum_file_x, datum_file_y ,"o")
                    with st.container():
                        
                        AgGrid(data)
                    
            
                   


    
    

                    
    

    
    


#Initialize 
