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
over_theme = {'txc_inactive': 'black','menu_background':'rgb(246, 246, 246)','txc_active':'yellow','option_active':'red', 'align':'center'}
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

# specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label':"Left End"},
    {'id':'Copy','icon':"🐙",'label':"Copy"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
    {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
    {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    {'icon': "far fa-copy", 'label':"Right End"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)
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
