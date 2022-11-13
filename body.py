from hourly import table as tb
from forecast import future as f
from api import api_key
from streamlit_folium import folium_static
import folium

import plotly.graph_objects as go


def body_main(stream, city):
    global_is_day = -1

    if city != "":
        try:
            file = api_key(city)
            op = file[0]
            country = op['location']['country']
            lat = op['location']['lat']
            lon = op['location']['lon']
            time = op['location']['localtime']
            humidity = op['current']['humidity']
            feelslike = op['current']['temp_c']
            icon = 'https:' + str(op['current']['condition']['icon'])
            is_day = op['current']['is_day']
            global_is_day = is_day
            sunrise = op['forecast']['forecastday'][0]['astro']['sunrise']
            sunset = op['forecast']['forecastday'][0]['astro']['sunset']
            moonrise = op['forecast']['forecastday'][0]['astro']['moonrise']
            moonset = op['forecast']['forecastday'][0]['astro']['moonset']
            moon_phase = op['forecast']['forecastday'][0]['astro']['moon_phase']
            wind = op['current']['wind_mph']
            wind_dir = op['current']['wind_dir']
            visibility = op['current']['vis_km']

            hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''

            stream.markdown(hide_img_fs, unsafe_allow_html=True)

            col1, col2 = stream.columns([1, 2])

            with col1:
                stream.text(time)
                stream.image(f"{icon}", width=70)
                stream.metric(label='{}/ {}'.format(city.upper(), country), value="{}°C".format(feelslike),
                              delta=None)
                stream.text('Sunrise: {}    Moonrise: {}'.format(sunrise, moonrise))
                stream.text('Sunset: {}     Moonset: {}'.format(sunset, moonset))
                stream.text('Moon_phase: {}'.format(moon_phase))
                stream.text('Humidity: {}%        Visibility(km): {}'.format(humidity, visibility))
                stream.text('Wind(MPH): {}       Wind_Dir: {} '.format(wind, wind_dir))

            with col2:
                map_sby = folium.Map(location=[lat, lon], width=400, height=500, zoom_start=10, control_scale=True,
                                     no_touch=True)
                folium.Marker([lat, lon], popup=city.capitalize(), tooltip=city.capitalize()).add_to(map_sby)
                folium.Figure(width=400, height=500)
                folium.TileLayer(
                    # tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attr='Esri',
                    name='Esri Satellite',
                    overlay=False,
                    control=False
                ).add_to(map_sby)
                folium_static(map_sby)
                map_style = '''
                <style>

                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > iframe
                    { height: 400px;
                            width: 400px;
                            zoomControl: false;
                    }
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div.css-115gedg.e1tzin5v2 > div:nth-child(1) > div > div:nth-child(1){
                            text-align: center;}
                </style>
                '''
                stream.markdown(map_style, unsafe_allow_html=True)
            stream.text('Hourly Forecast')

            col3, col4, col5 = stream.columns([2, 2, 2])
            style = '''
            <style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(5) > div{             
                font-size:39.608px;
                font-family: "Source Sans Pro", sans-serif;
                font-weight: bold;
                text-align: center;}
            </style>
            '''
            stream.markdown(style, unsafe_allow_html=True)

            with col3:
                def path_to_image_html(path):
                    return '<img src="' + path + '" width="30" height="30" >'

                def convert_df(input_df):
                    return input_df.to_html(escape=False, formatters=dict(Icon=path_to_image_html), border='0',
                                            justify='center')

                html = convert_df(tb(op))

                stream.markdown(
                    html,
                    unsafe_allow_html=True
                )

                img = '''
                <style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(1){  
                 height: 400px;
                 width: 300px;
                 //background: url("https://wallpaperaccess.com/full/1442216.jpg");
                 overflow-y: auto;
                 overflow-x: hidden;

                } 
                td {
                 height: 5px;
                 text-align: center;
                 }
                 thead tr th:first-child {display:none;}
                 tbody tr, thead {border: 2px solid black;}
                 tbody th {display:none}

                 #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > div > div > table > thead > tr > th {position: sticky; top:0;
                 color: white;
                 background-color: black;
                 # border: 2px solid black;
                 }
                 .css-1fv8s86 td {border: 0px}
                 .dataframe {color: white; border-style: none; align:center; margin-top: 3px;}
                 table {margin: 0 auto;}
                </style>

                '''
                stream.markdown(img, unsafe_allow_html=True)
            # data = pd.read_excel(r"Hourly_forecast.xlsx")
            data = tb(file[0])

            with col4:
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Scatter(x=data.Time, y=data.Temp, mode='lines+markers', name='<b>Temp</b>',
                                         marker={'color': '#de4802'},
                                         hovertemplate='Temp: %{y:.2f}°C' + '<br>Time: %{x}'))
                fig.update_yaxes(
                    showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(
                    tickangle=45, showgrid=False
                )
                fig.layout.xaxis.color = 'white'
                fig.layout.yaxis.color = 'white'
                fig.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Time</b>",
                                  yaxis_title="<b>Temperature(°C)</b>")
                stream.plotly_chart(fig, use_container_width=True, config=config)

            with col5:
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Bar(x=data.Time, y=data.Temp, name='<b>Temp</b>', marker={'color': '#de4802'},
                                     hovertemplate='Temp: %{y:.2f}°C' + '<br>Time: %{x}'))
                fig.update_yaxes(  # the y-axis is in dollars
                    showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(  # the y-axis is in dollars
                    tickangle=45, showgrid=False
                )
                fig.layout.xaxis.color = 'white'
                fig.layout.yaxis.color = 'white'
                fig.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Time</b>",
                                  yaxis_title="<b>Temperature(°C)</b> ")
                stream.plotly_chart(fig, use_container_width=True, config=config)

            stream.text('5-Day Forecast')
            style = '''
                     <style>
                         #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(8) > div{             
                         font-size:39.608px;
                         font-family: "Source Sans Pro", sans-serif;
                         font-weight: bold;
                         text-align: center;}
                     </style>
                     '''
            stream.markdown(style, unsafe_allow_html=True)

            col6, col7, col8 = stream.columns([2, 2, 2])

            with col6:
                stream.header('')

                def path_to_image_html(path):
                    return '<img src="' + path + '" width="30" height="30" >'

                def convert_df(input_df):
                    return input_df.to_html(escape=False, formatters=dict(Icon=path_to_image_html), border='0',
                                            justify='center')

                html = convert_df(f(file[1]))

                stream.markdown(
                    html,
                    unsafe_allow_html=True
                )
                style_table = '''
                <style>
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > div > table > thead > tr{
                    color: white;
                    background-color: black;
                </style>
                '''
                stream.markdown(style_table, unsafe_allow_html=True)
                # data = pd.read_excel(r"5Days_Forecast.xlsx")
                data = f(file[1])

            with col7:
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Scatter(x=data.Date, y=data.Min_temp, mode='lines+markers', name='<b>Min_temp</b>',
                                         marker={'color': '#de4802'},
                                         hovertemplate='Min_temp: %{y:.2f}°C' + '<br>Date: %{x}'))
                fig.add_trace(go.Scatter(x=data.Date, y=data.Max_temp, mode='lines+markers', name='<b>Max_temp</b>',
                                         marker={'color': '#d48b6a'},
                                         hovertemplate='Max_temp: %{y:.2f}°C' + '<br>Date: %{x}'))
                fig.update_yaxes(
                    showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(
                    tickangle=45, showgrid=False
                )
                fig.layout.xaxis.color = 'white'
                fig.layout.yaxis.color = 'white'
                fig.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Date</b>",
                                  yaxis_title="<b>Temperature(°C)</b>")
                stream.plotly_chart(fig, use_container_width=True, config=config)

            with col8:
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(
                    go.Bar(x=data.Date, y=data.Min_temp, name='<b>Min_temp</b>', marker={'color': '#de4802'},
                           hovertemplate='Min_temp: %{y:.2f}°C' + '<br>Date: %{x}'))
                fig.add_trace(
                    go.Bar(x=data.Date, y=data.Max_temp, name="<b>Max_temp</b>", marker={'color': '#d48b6a'},
                           hovertemplate='Max_temp: %{y:.2f}°C' + '<br>Date: %{x}'))
                fig.update_yaxes(
                    showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(  # the y-axis is in dollars
                    tickangle=45, showgrid=False
                )
                fig.layout.xaxis.color = 'white'
                fig.layout.yaxis.color = 'white'
                fig.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Date</b>",
                                  yaxis_title="<b>Temperature(°C)</b> ")
                stream.plotly_chart(fig, use_container_width=True, config=config)

        except Exception as e:
            stream.write('Enter valid city')

    return global_is_day
