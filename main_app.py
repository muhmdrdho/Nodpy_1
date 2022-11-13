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



from app.core.maps import *

    

    
    


#Initialize 
