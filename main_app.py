from app.index_lib import *

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

if selected=="Preacquisition":
    st.header("Preacquisition")
    st.markdown("---")

    cols = st.columns([5,2])
    with cols[1]:
        st.subheader("SetBox")
        upload_pre = st.file_uploader("choose your file")
        with st.expander("Set your map"):
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
        from app.core.maps import *
        st_folium(pre_map, width=700)

if selected=="Interpretation":
    st.header("Interpretation")
    st.markdown("---")
    cols = st.columns([5,2])
    with cols[1]:
        st.subheader("Set Box")
        number_of_tabs = st.number_input("Number of Tabs", min_value=1, max_value=16, value=1)
        number_of_tabs = int(number_of_tabs)
    with cols[0]:
        tabs = st.tabs([f"tab{i+1}" for i in range(number_of_tabs)])
        for i in range(number_of_tabs):
            with tabs[i]:
                st.subheader("Digital Map")




        
    

    
    


#Initialize 
