from app.index_lib import *
from st_card_component_2 import card_component
st.set_page_config( layout="wide", initial_sidebar_state="expanded")
    #sidebar
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
with st.sidebar:
    selected = option_menu("Main Menu",["Preacquisition", "Interpretation", "About"],
                            icons=["file","compass","megaphone"],
                            menu_icon="cast",
                            default_index=0
                            )

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
 
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

#Initialize 
df_map = pd.read_csv("app/assets/data/Geology+Jambi4.csv")
df_map1 = df_map[["SYMBOLS","IDX_FORMATION"]]
state_geo = "app/assets/data/Geology+Jambi.geojson"
geojson = gpd.read_file(state_geo)
geojson_states = list(geojson.SYMBOLS.values)
final_df = geojson.merge(df_map, on="SYMBOLS")
map_dict = df_map1.set_index('SYMBOLS')['IDX_FORMATION'].to_dict()


color_scale = LinearColormap(['darkblue','brown','tan','olive','blue','cyan','yellow','orange','red','aquamarine','azure','navy','teal','beige'], vmin = min(map_dict.values()), vmax = max(map_dict.values()))
def get_color(feature):
    value = map_dict.get(feature['properties']['SYMBOLS'])
    if value is None:
        return '#8c8c8c' # MISSING -> gray
    else:
        return color_scale(value)

#subheader
st.header("Preacquisition")
st.markdown("---")

#Map Processing
pre_map = folium.Map(tiles='StamenTerrain',location=[-1.609972, 103.607254], zoom_start=6)
    
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
                                    'fillOpacity': 0.7,
                                    'color' : 'black',
                                    'weight' : 1,
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


    
 
        
  
#columns
cols = st.columns([5,2])
if selected=="Preacquisition":
    with cols[0]:
        st.subheader("Digital Map")
        folium_static(pre_map)

    with cols[1]:
        st.subheader("SetBox")
        upload_pre = st.file_uploader("choose your file")
        if upload_pre is not None :
            data_pre = pd.read_csv(upload_pre)
            coordinate_data = data_pre
            coordinate_data = coordinate_data.dropna(subset=['Latitude'])
            coordinate_data = coordinate_data.dropna(subset=['Longitude'])
            for i in range(len(coordinate_data)):
                folium.Marker(location=[coordinate_data.iloc[i]['Latitude'], coordinate_data.iloc[i]['Longitude']]).add_to(pre_map)