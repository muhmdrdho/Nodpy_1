from app.index_lib import *

st.set_page_config(layout='wide', initial_sidebar_state="expanded")

hc.hydralit_experimental(True)


modal_code = """
<div>
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
Hydralit Components Experimental Demo!
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
<div class="modal-dialog" role="document">
<div class="modal-content">
<div class="modal-header">
  <h5 class="modal-title" id="exampleModalLabel">Modal Popup Form!</h5>
  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>
<div class="modal-body">
  <div class="container">
<h2>Pure JS+HTML Form</h2>
<form class="form-horizontal" action="/">
<div class="form-group">
<label class="control-label col-sm-2" for="email">Email:</label>
<div class="col-sm-10">
  <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
</div>
</div>
<div class="form-group">
<label class="control-label col-sm-2" for="pwd">Password:</label>
<div class="col-sm-10">          
  <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pwd">
</div>
</div>
<div class="form-group">        
<div class="col-sm-offset-2 col-sm-10">
  <div class="checkbox">
    <label><input type="checkbox" name="remember"> Remember me</label>
  </div>
</div>
</div>
<div class="form-group">        
<div class="col-sm-offset-2 col-sm-10">
  <button type="submit" class="btn btn-default">Submit</button>
</div>
</div>
</form>
</div>
</div>
<div class="modal-footer">
  <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
  <button type="button" class="btn btn-primary">Save changes</button>
</div>
</div>
</div>
</div>
</div>
"""


st.markdown(modal_code,unsafe_allow_html=True)
query_param = st.experimental_get_query_params()

if query_param:
    st.write('We caputred these values from the experimental modal form using Javascript + HTML + Streamlit + Hydralit Components.')
    st.write(query_param)
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
