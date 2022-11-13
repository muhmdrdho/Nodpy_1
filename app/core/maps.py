import folium
from folium import plugins


pre_map = folium.Map(tiles='StamenTerrain',location=[-1.609972, 103.607254], zoom_start=6)
    
    #base tile map
Esri_Satellite = folium.TileLayer(
                                                        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                                        attr = 'Esri',
                                                        name = 'Esri Satellite',
                                                        overlay = True,
                                                        control = True
                                                        ).add_to(pre_map)
Google_Satellite_Hybrid =  folium.TileLayer(
                                                        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                                                        attr = 'Google',
                                                        name = 'Google Satellite',
                                                        overlay = True,
                                                        control = True
                                                         ).add_to(pre_map)
Google_Terrain = folium.TileLayer(
                                                        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                                                        attr = 'Google',
                                                        name = 'Google Terrain',
                                                        overlay = True,
                                                        control = True
                                                        ).add_to(pre_map)
Google_Satellite = folium.TileLayer(
                                                        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                                                        attr = 'Google',
                                                        name = 'Google Satellite',
                                                        overlay = True,
                                                        control = True
                                                        ).add_to(pre_map)
Google_Maps = folium.TileLayer(
                                                        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                                                        attr = 'Google',
                                                        name = 'Google Maps',
                                                        overlay = True,
                                                        control = True
                                                        ).add_to(pre_map)

n = folium.GeoJson(
                                name= 'Geology Map',
                                data = state_geo,
                                style_function = lambda feature: {
                                    'fillColor': get_color(feature),
                                    'fillOpacity': geology_map_slider,
                                    'color' : 'black',
                                    'weight' : 1,
                                    }    
                                ).add_to(pre_map)
    #Layer control
folium.LayerControl().add_to(pre_map)
    
    #Fullscreeen
plugins.Fullscreen().add_to(pre_map)

    #Locate Control
plugins.LocateControl().add_to(pre_map)
     #Locate Control
            
            
            #Cursor Postion
fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",lat_formatter=fmtr, lng_formatter=fmtr).add_to(pre_map)
            
            #Add the draw 
plugins.Draw(export=True, filename='data.geojson', position='topleft', draw_options=None, edit_options=None).add_to(pre_map)
            
            #Measure Control
plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(pre_map)