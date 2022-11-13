import streamlit as st
from streamlit_folium import folium_static
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu

st.set_page_config( layout="wide", initial_sidebar_state="expanded")
from app.core.maps import *
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

st.header("Preacquisition")
st.markdown("---")

cols = st.columns([5,2])
if selected=="Preacquisition":
    

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

        geology_map_slider = ('Set your geology map transparency', 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)

#Map Processing


    with cols[0]:
        st.subheader("Digital Map")
        st_folium(pre_map)
