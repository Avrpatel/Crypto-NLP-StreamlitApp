import streamlit as st
import pandas as pd
import datetime as dt
from pathlib import Path
import numpy as np
import altair as alt
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


crypto_list = ['Luna', 'Bitcoin', 'Ethereum', 'Binance', 'Solana', 'Cardano']

for x in crypto_list:
    if option == x:
        x_path = Path(f'../data/Price/{x}price.csv')
        x_data = pd.read_csv(x_path)
        

        x_data.set_index(pd.to_datetime(x_data['Date'], infer_datetime_format=True, format='%Y%m%d'), inplace=True)
        x_data = x_data.drop(columns=['Date'])


st.dataframe(x_data)

for y in crypto_list:
    if option == y:
        y_path = Path(f'../data/NewsAPI/{y}nlp.csv')
        y_data = pd.read_csv(y_path)
        y_data.set_index(pd.to_datetime(y_data['Date'], infer_datetime_format=True, format='%Y%M%D'), inplace=True)
        y_data = y_data.drop(columns=['Date'])

st.dataframe(y_data)



#########################################################


# Radio Button

plot_type = st.radio(
     "Which data set would you like to see a plot for?:",
     ('Crypto Price', 'AlphaVantage', 'NewsAPI', 'All'))

# x_data_copy = x_data.reset_index()
# price_df = pd.DataFrame(x_data_copy)
# price_df['Date'] = price_df['Date'].dt.to_pydatetime()
# date_list = list(price_df.index.values)

# x_data_copy

price_df = pd.DataFrame(x_data)
new_price_df= price_df.reset_index()


news_sentiment_df = pd.DataFrame(y_data)
final_news_df = news_sentiment_df.reset_index()



if plot_type == 'Crypto Price':
     st.write('You selected crypto prices.')

     fig = px.line(new_price_df, x="Date", y="Close", title='Crypto Closing Price')
     st.plotly_chart(fig, use_container_width=True)
     

    #  price_chart = alt.Chart(price_df).mark_line().encode(
    #     x = price_df['Date'],
    #     y = price_df['Close']
    #  )

    #  st.altair_chart(price_chart, use_container_width=True)
     

#elif plot_type == 'AlphaVantage':
    # st.write("You selected AlphaVantage.") 
    # st.line_chart(data)

elif plot_type == 'NewsAPI':
    st.write('You selected NewsAPI.')
    fig_news_sentiment = px.line(final_news_df, x="Date", y="luna_avg", title='Crypto Closing Price')
    st.plotly_chart(fig_news_sentiment, use_container_width=True)    


