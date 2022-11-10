from app.index_lib import *

st.set_page_config(layout='wide', initial_sidebar_state="expanded")
    #sidebar
sidebar_setting = st.markdown(
        """
        <style>
            .css-1fkbmr9 {
                        background-color: rgb(255, 255, 255);
                        background-attachment: fixed;
                        flex-shrink: 0;
                        height: calc(100vh - 2px);
                        top: 0px;
                        width: 18rem;
                        z-index: 999991;
                        margin-left: 0px;
                        }
        </style>
        """,
        unsafe_allow_html=True,
    )
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
 
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
    #sidebar logo


    #sidebar main menu
st.sidebar.image('app/assets/logo/Nodpy2.png')
with st.sidebar:
    selected = option_menu("Main Menu",["Preacquisition", "Interpretation", "About"],
                            icons=["file","compass","megaphone"],
                            menu_icon="cast",
                            default_index=0
                            )
over_theme = {'txc_inactive': 'purple','menu_background':'white','txc_active':'yellow','option_active':'pink'}
if selected=="Preacquisition":
    menu_data = [{'label':"Preacquisition"}]
    menu_id = hc.nav_bar(menu_definition=menu_data, override_theme=over_theme)



st.info(f"{menu_id=}")
footer="""

        <style> your css code put here</style>

        <div class='footer'>

        <p>the word you want to tell<a style='display:block;text-align:center;' 

        href='https://www.streamlit.io' target='_blank'>your email address put here</a></p>

        </div>
        """

st.markdown(footer, unsafe_allow_html=True)
reduce_header_height_style = """
            <style>
                div.block-container {padding-top:0rem;}
            </style>
        """
st.markdown(reduce_header_height_style, unsafe_allow_html=True)
