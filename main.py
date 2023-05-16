import json
from body import *
from urllib.request import urlopen
import streamlit as st

# url = 'https://ipinfo.io/json'
# response = urlopen(url)
# city_def = json.load(response)['city']

stream = st
stream.set_page_config(layout='wide')

stream.title("\t Weather Forecast")

col1, col2 = stream.columns(2)
with col1:
    city = stream.text_input('', placeholder='Search a City')
with col2:
    stream.write(' ')
    stream.write(' ')
    but = stream.button("SEARCH")

if but:
    global_is_day = body_main(stream, city)
else:
    global_is_day = body_main(stream, 'noida')

search = '''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v4 > div:nth-child(1) > div:nth-child(1) > div > div > div > div.css-1if5ada.effi0qh1{
            visibility: hidden;
            }
            </style>
            '''
stream.markdown(search, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
stream.markdown(hide_streamlit_style, unsafe_allow_html=True)

if global_is_day == 0:
    page_bg_img = '''
                                       <style>
                                       #root > div:nth-child(1) > div.withScreencast > div > div{
                                       background: url('https://images.pexels.com/photos/4737484/pexels-photo-4737484.jpeg?cs=srgb&dl=pexels-rafael-cerqueira-4737484.jpg&fm=jpg') no-repeat center;
                                       background-size:cover;
                                       }
                                       #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(6){
                                        border-radius: 25px;
                                        background: #041e39;
                                        opacity: 0.9;
                                        padding: 20px;
                                        }
                                        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div.css-1r6slb0.e1tzin5v2{
                                        border-radius: 25px;
                                        background: #041e39;
                                        padding: 20px;
                                        width: 400px;
                                        opacity: 0.9;
                                        }
                                        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(10){
                                        border-radius: 25px;
                                        background: #041e39;
                                        opacity: 0.9;
                                        padding: 20px;
                                        }
                                       </style>
                                       '''
elif global_is_day == 1:
    page_bg_img = '''
                                           <style>
                                           #root > div:nth-child(1) > div.withScreencast > div > div{
                                           background: url('https://p4.wallpaperbetter.com/wallpaper/142/225/285/the-sun-macro-rays-background-wallpaper-preview.jpg') no-repeat center;
                                       background-size:cover;
                                           }
                                           #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(6){
                                            border-radius: 25px;
                                            background: #331605;
                                            opacity: 0.9;
                                            padding: 20px;
                                            }
                                            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div.css-1r6slb0.e1tzin5v2{
                                            border-radius: 25px;
                                            background: #331605;
                                            padding: 20px;
                                            width: 400px;
                                            opacity: 0.9;
                                            }
                                            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(10){
                                            border-radius: 25px;
                                            background: #331605;
                                            opacity: 0.9;
                                            padding: 20px;
                                            }
                                           </style>
                                           '''
else:
    page_bg_img = '''
                                           <style>
                                           #root > div:nth-child(1) > div.withScreencast > div > div{
                                           background: url('https://wallpaperaccess.com/full/4898189.jpg') no-repeat center;
                                           background-size:cover;
                                           }'''
stream.markdown(page_bg_img, unsafe_allow_html=True)
