import streamlit as st
import pandas as pd
import datetime as dt
from pathlib import Path
import numpy as np
import plotly.express as px

######################################################################################

#Background image

import base64
@st.cache(allow_output_mutation=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_bg('../assets/background.png')


######################################################################################

#Streamlit App

st.markdown("# Crypto NLP App")
st.markdown("## Choose from the following crypto currencies: ")

option = st.selectbox(
     'List of currencies',
     ('Luna', 'Bitcoin', 'Ethereum', 'Binance', 'Solana', 'Cardano'))

st.write('You chose:', option)

# Choose to highlight min or max data within dataframes
highlights = st.radio(
     "Please select one of the following if you wish to highlight min or max data:",
     ('None','Min', 'Max'))




crypto_list = ['Luna', 'Bitcoin', 'Ethereum', 'Binance', 'Solana', 'Cardano']

# Crypto Price csv 

for x in crypto_list:
    if option == x:
        x_path = Path(f'../data/Price/{x}price.csv')
        x_data = pd.read_csv(x_path)
        

        x_data.set_index(pd.to_datetime(x_data['Date'], infer_datetime_format=True), inplace=True)
        x_data = x_data.drop(columns=['Date'])

st.markdown("## Crypto Price Dataframe:")

if highlights == 'Max':
    st.dataframe(x_data.style.highlight_max(axis=0, props='color:red'), width=1800)

elif highlights == 'Min':
    st.dataframe(x_data.style.highlight_min(axis=0, props='color:red'), width=1800)

elif highlights == 'None':
    st.dataframe(x_data, width=1800)

    

# AlphaVantage Sentiment csv

for z in crypto_list:
    if option == z:
        z_path = Path(f'../data/AlphaVantage/{z}_sent.csv')
        z_data = pd.read_csv(z_path)
        z_data.set_index(pd.to_datetime(z_data['Date'], infer_datetime_format=True), inplace=True)
        z_data = z_data.drop(columns=['Date'])

st.markdown("## AlphaVantage Sentiment Dataframe:")

if highlights == 'Max':
    st.dataframe(z_data.style.highlight_max(axis=0, props='color:red'), width=1800)

elif highlights == 'Min':
    st.dataframe(z_data.style.highlight_min(axis=0, props='color:red'), width=1800)
    
elif highlights == 'None':
    st.dataframe(z_data, width=1800)

# NewsAPI Sentiment csv

for y in crypto_list:
    if option == y:
        y_path = Path(f'../data/NewsAPI/{y}nlp.csv')
        y_data = pd.read_csv(y_path)
        y_data.set_index(pd.to_datetime(y_data['Date'], infer_datetime_format=True), inplace=True)
        y_data = y_data.drop(columns=['Date'])

st.markdown("## News API Sentiment Dataframe:")

if highlights == 'Max':
    st.dataframe(y_data.style.highlight_max(axis=0, props='color:red'), width=1800)

elif highlights == 'Min':
    st.dataframe(y_data.style.highlight_min(axis=0, props='color:red'), width=1800)
    
elif highlights == 'None':
    st.dataframe(y_data, width=1800)



#########################################################


# Radio Button

price_df = pd.DataFrame(x_data)
new_price_df= price_df.reset_index()


news_sentiment_df = pd.DataFrame(y_data)
final_news_df = news_sentiment_df.reset_index()

alpha_sentiment_df = pd.DataFrame(z_data)
final_alpha_df = alpha_sentiment_df.reset_index()


plot_type = st.radio(
     "Which data set would you like to see a plot for?:",
     ('Crypto Price', 'AlphaVantage', 'NewsAPI', 'All'))


if plot_type == 'Crypto Price':
     st.write('You selected crypto prices.')

     fig = px.line(new_price_df, x="Date", y="Close", title='Crypto Closing Price')
     st.plotly_chart(fig, use_container_width=True)
     

elif plot_type == 'AlphaVantage':
    st.write("You selected AlphaVantage.")

    fig_alpha_sentiment = px.line(final_alpha_df, x="Date", y="overall_sentiment_score", title='Crypto Closing Price')
    st.plotly_chart(fig_alpha_sentiment, use_container_width=True)
    

elif plot_type == 'NewsAPI':
    st.write('You selected NewsAPI.')
    for score in crypto_list:
        if score == option:
            fig_news_sentiment = px.line(final_news_df, x="Date", y=f"{score}_avg", title='Crypto Average Sentiment Score - NewsAPI', markers=True)
            st.plotly_chart(fig_news_sentiment, use_container_width=True)    


