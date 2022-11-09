from app.index_lib import *

st.set_page_config(layout='wide', initial_sidebar_state="expanded")
    #sidebar
sidebar_setting = st.markdown(
        """
        <style>
            .css-1fkbmr9 {
                        background-color: rgb(246, 246, 246);
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
    #sidebar logo
st.sidebar.image('app/assets/logo/Nodpy2.png')

    #sidebar main menu
option_data = [
   {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
   {'icon':"fa fa-question-circle",'label':"Unsure"},
   {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
]
over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'yellow','option_active':'red', 'align':'center'}
font_fmt = {'font-class':'h2','font-size':'150%'}
with st.sidebar:
    op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=False)
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
 
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
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
