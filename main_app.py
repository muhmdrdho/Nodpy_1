from app.index_lib import *

st.set_page_config(layout='wide', initial_sidebar_state="expanded")
    #sidebar
sidebar_setting = st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            min-width: 100px;
            max-width: 200px;
        }
    
        </style>
        """,
        unsafe_allow_html=True,
    )
    #sidebar logo
st.sidebar.image('app/assets/logo/Nodpy2.png')

    #sidebar navigation
with st.sidebar:
    selected = option_menu("Main Menu",["Preacquisition", "Interpretation", "About"],
                                icons=["file","compass","megaphone"],
                                menu_icon="cast",
                                default_index=0
                                )
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