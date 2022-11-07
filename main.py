import json
import streamlit as st
import requests
import pandas as pd
import numpy as np
from test import table as tb
from Forecast2 import future as f
from IPython.core.display import HTML
import altair as alt
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from streamlit_folium import st_folium, folium_static
import folium
from folium import features
from plotly.graph_objects import Layout
import plotly.graph_objects as go
from datetime import datetime

url = "https://weatherapi-com.p.rapidapi.com/current.json"
st.set_page_config(layout='wide')

st.title("\t Weather Forecast")

col1, col2 = st.columns(2)
with col1:
    city = st.text_input('', placeholder='Search a City')
with col2:
    st.write(' ')
    st.write(' ')
    but = st.button("SEARCH")

if but:
    if city != "":
        try:
            querystring = {"q": "{}".format(city)}

            headers = {
                "X-RapidAPI-Key": "5813e2cf35mshca95fb7c1db2f5dp1ed490jsn579d844299d5",
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }

            # response = requests.request("GET", url, headers=headers, params=querystring)
            # op = response.json()
            # json_object = json.dumps(op, indent=4)
            # with open("sample.json", "w") as outfile:
            #     outfile.write(json_object)

            # country = op['location']['country']
            # lat = op['location']['lat']
            # lon = op['location']['lon']
            # time = op['location']['localtime']
            # humidity = op['current']['humidity']
            # feelslike = op['current']['feelslike_c']
            # icon = 'https:'+str(op['current']['condition']['icon'])
            # is_day = op['current']['is_day']

            country = 'india'
            lat = 90
            lon = 67
            time = '9:50'
            humidity = 50
            feelslike = 30
            icon = 'http://openweathermap.org/img/wn/10d@2x.png'
            is_day = 1

            hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''

            st.markdown(hide_img_fs, unsafe_allow_html=True)

            col1, col2 = st.columns([2,1])
            with col1:
                st.header(' ')
                st.header(' ')
                st.text(time)
                st.image(f"{icon}",width=70)
                st.metric(label='{}/ {}'.format(city.upper(), country), value="{}°c".format(feelslike), delta=None)
                st.markdown('Streamlit is **_really_ cool**.')
                st.markdown('Streamlit is **really cool jj hh jj kk**.')
            with col2:
                # data = pd.DataFrame({
                #     'awesome cities' : ['{}'.format(city)],
                #     'lat' : [15.2993],
                #     'lon' : [74.1240]
                # })
                # st.map(data)
                map_sby = folium.Map(location=[15.2993, 74.1240], width=400, height=500,zoom_start=10)
                folium.Marker([15.2993, 74.1240], popup='Liberty Bell', tooltip="Liberty Bell").add_to(map_sby)
                folium.Figure(width=400, height=500)
                folium.TileLayer(
                    #tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attr='Esri',
                    name='Esri Satellite',
                    overlay=False,
                    control=False
                ).add_to(map_sby)
                folium_static(map_sby)
                map_style='''
                <style>
                
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > iframe
                    { height: 400px;
                            width: 400px;
                            zoomControl: false;}
                </style>
                '''
                st.markdown(map_style,unsafe_allow_html=True)
            st.text('Hourly Forecast')
            col3, col4,col5 = st.columns([2,2,2])
            # tb()
            # w_data = pd.read_excel(r'Hourly_forecast.xlsx')
            # with col3:
                # st.dataframe(tb())
            style='''
            <style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(5) > div{             
                font-size:39.608px;
                font-family: "Source Sans Pro", sans-serif;
                font-weight: bold;
                text-align: center;}
            </style>
            '''
            st.markdown(style,unsafe_allow_html=True)
            with col3:
                def path_to_image_html(path):
                    return '<img src="' + path + '" width="30" height="30" >'


                def convert_df(input_df):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return input_df.to_html(escape=False, formatters=dict(Icon = path_to_image_html), border='0', justify='center')


                html = convert_df(tb())

                st.markdown(
                    html,
                    unsafe_allow_html=True
                )
                # page_bg_img = '''
                # <style type="text/css">
                # #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(1) {
                # height: 400px;
                # width: 300px;
                # //background: url("https://wallpaperaccess.com/full/1442216.jpg");
                # overflow-y: auto;
                # overflow-x: hidden;
                #
                # }
                # td {
                # height: 5px;
                # }
                # thead tr th:first-child {display:none;}
                # tbody tr, thead {border: 2px solid black;}
                # tbody th {display:none}
                # .css-1fv8s86 td {border: 0px}
                # .dataframe {color: white; border-style: none; align:center; margin-top: 3px;}
                # table {margin: 0 auto;}
                #
                # </style>
                # '''
                # st.markdown(page_bg_img, unsafe_allow_html=True)
                img='''
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
                 .dataframe {color: black; border-style: none; align:center; margin-top: 3px;}
                 table {margin: 0 auto;}
                </style>
                
                '''
                st.markdown(img, unsafe_allow_html=True)
            data = pd.read_excel(r"Hourly_forecast.xlsx")
            with col4:
                # st.header(' ')
                # st.header(' ')
                # st.line_chart(data=tb(), x="Time", y='Temp')
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Scatter(x=data.Time, y=data.Temp, mode='lines+markers', name='<b>Temp</b>', marker={'color': '#de4802'},hovertemplate='Temp: %{y:.2f}°C'+'<br>Time: %{x}'))
                fig.update_yaxes(  # the y-axis is in dollars
                    tickformat="°C", showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(  # the y-axis is in dollars
                    tickangle=45, showgrid=False
                )
                fig.update_layout(plot_bgcolor='#0e1117',paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Time</b>", yaxis_title="<b>Temperature(°C)</b>")
                st.plotly_chart(fig, use_container_width=True, config=config)
            with col5:
                # st.header(' ')
                # st.header(' ')
                # st.bar_chart(data=tb(), x="Time", y='Temp')
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Bar(x=data.Time, y=data.Temp, name='<b>Temp</b>', marker={'color': '#de4802'},hovertemplate='Temp: %{y:.2f}°C'+'<br>Time: %{x}'))
                fig.update_yaxes(  # the y-axis is in dollars
                    showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(  # the y-axis is in dollars
                    tickangle=45, showgrid=False
                )
                fig.update_layout(plot_bgcolor='#0e1117',paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Time</b>", yaxis_title="<b>Temperature(°C)</b> ")
                st.plotly_chart(fig, use_container_width=True, config=config)
            st.text('5-Day Forecast')
            style = '''
                     <style>
                         #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(8) > div{             
                         font-size:39.608px;
                         font-family: "Source Sans Pro", sans-serif;
                         font-weight: bold;
                         text-align: center;}
                     </style>
                     '''
            st.markdown(style, unsafe_allow_html=True)
            col6, col7, col8 = st.columns([2, 2, 2])
            with col6:
                st.header('')
                def path_to_image_html(path):
                    return '<img src="' + path + '" width="30" height="30" >'


                def convert_df(input_df):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return input_df.to_html(escape=False, formatters=dict(Icon = path_to_image_html), border='0', justify='center')


                html = convert_df(f())

                st.markdown(
                    html,
                    unsafe_allow_html=True
                )
                style_table ='''
                <style>
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > div > table > thead > tr{
                    color: white;
                    background-color: black;
                </style>
                '''
                st.markdown(style_table,unsafe_allow_html=True)
                data = pd.read_excel(r"5Days_Forecast.xlsx")
            with col7:
                # st.header('5-DAY FORECAST')
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Scatter(x=data.Date, y=data.Min_temp, mode='lines+markers', name='<b>Min_temp</b>', marker = {'color' : '#de4802'},hovertemplate='Min_temp: %{y:.2f}°C'+'<br>Date: %{x}'))
                fig.add_trace(go.Scatter(x=data.Date, y=data.Max_temp, mode='lines+markers', name='<b>Max_temp</b>', marker = {'color' : '#d48b6a'},hovertemplate='Max_temp: %{y:.2f}°C'+'<br>Date: %{x}'))
                fig.update_yaxes(  # the y-axis is in dollars
                    tickformat="°C", showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(  # the y-axis is in dollars
                    tickangle=45,showgrid=False
                )
                fig.update_layout(plot_bgcolor='#0e1117',paper_bgcolor='rgba(0,0,0,0)', xaxis_title="<b>Date</b>", yaxis_title="<b>Temperature(°C)</b>")
                st.plotly_chart(fig, use_container_width=True, config=config)

            with col8:
                fig = go.Figure()
                config = {'displayModeBar': False}
                fig.add_trace(go.Bar(x=data.Date, y=data.Min_temp, name='<b>Min_temp</b>', marker = {'color' : '#de4802'}, hovertemplate='Min_temp: %{y:.2f}°C'+'<br>Date: %{x}'))
                fig.add_trace(go.Bar(x=data.Date, y=data.Max_temp, name="<b>Max_temp</b>", marker = {'color' : '#d48b6a'}, hovertemplate='Max_temp: %{y:.2f}°C'+'<br>Date: %{x}'))
                fig.update_yaxes(  # the y-axis is in dollars
                    showgrid=True, gridcolor='#333333'
                )
                fig.update_xaxes(  # the y-axis is in dollars
                    tickangle=45, showgrid=False
                )
                fig.update_layout(plot_bgcolor='#0e1117',paper_bgcolor='rgba(0,0,0,0)',xaxis_title="<b>Date</b>", yaxis_title="<b>Temperature(°C)</b> ")
                st.plotly_chart(fig, use_container_width=True, config=config)

        except:
            st.write('Enter valid city')

time_now = datetime.now()
mid = time_now.replace(hour=12, minute=0, second=0, microsecond=0)
if time_now < mid:
    page_bg_img = '''
                                       <style>
                                       #root > div:nth-child(1) > div.withScreencast > div > div{
                                       background-image: linear-gradient(red, yellow);
                                       }
                                       </style>
                                       '''
else:
    page_bg_img = '''
                                           <style>
                                           #root > div:nth-child(1) > div.withScreencast > div > div{
                                           background-image: linear-gradient(#33ccff 0%, #00ff99 100%);
                                           }
                                           </style>
                                           '''
st.markdown(page_bg_img, unsafe_allow_html=True)