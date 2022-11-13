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

st.header("Preacquisition")
st.markdown("---")

with st.sidebar:
    selected = option_menu("Main Menu",["Preacquisition", "Interpretation", "About"],
                            icons=["file","compass","megaphone"],
                            menu_icon="cast",
                            default_index=0
                            )
if selected=="Preacquisition":
    cols = st.columns([5,2])
    with cols[1]:
        st.subheader("SetBox")
        upload_pre = st.file_uploader("choose your file")
        with st.expander("Set your map"):
            geology_map_slider = st.slider('Set your geology map transparency', 0.0, 1.0,(0.2, 0.7))
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
        st_folium(pre_map, width=700)

        from app.core.maps import *
    

    
    


#Initialize 
