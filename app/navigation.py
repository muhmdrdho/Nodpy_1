import streamlit as st
with st.sidebar:
    selected = option_menu("Main Menu",["Preacquisition", "Interpretation", "About"],
                            icons=["file","compass","megaphone"],
                            menu_icon="cast",
                            default_index=0
                            )
if selected=="Preacquisition":
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