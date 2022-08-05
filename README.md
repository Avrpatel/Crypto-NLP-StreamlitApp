# Crypto-NLP-StreamlitApp

Northwestern Bootcamp Project 3 - Evan Sadasivan, Avinash Patel and Christine Nashihibi

## Presentation link - https://docs.google.com/presentation/d/1OiwSgGDrdHpk1HVWhfzqexHyUQFfCJyszj6cuxqoOcY/edit?usp=sharing

## Installation Guide - Technologies utilized

* ### Alpha Vantage -Crypto Currencies Api and News and Intelligence API - https://www.alphavantage.co/
* ### news api - https://www.newsapi.ai/

* ### Anaconda -
    * Navigate to the Anaconda website in order to download the appropriate installer.
    * https://www.anaconda.com/products/distribution#windows 

* ### Anaconda - conda environment 
            <!-- (After installing Anaconda we need to enable the terminal commands) -->

            conda init bash

            <!-- (Close your terminal and open a new one) -->

            conda update conda
            conda update anaconda

            <!-- (Now we need to create a suitable environment to run our jupyter lab and
             install libraries necessary for pyviz) -->

            conda activate base
            conda create -n pyvizenv python=3.7 anaconda -y

            conda activate pyvizenv

            conda install -c conda-forge python-dotenv -y
            conda install -c anaconda nb_conda -y
            conda install -c conda-forge nodejs=12 -y
            conda install -c pyviz holoviz -y
            conda install -c plotly plotly -y
            conda install -c conda-forge jupyterlab=2.2 -y
            conda install -c anaconda numpy==1.19 -y
            conda install -c conda-forge matplotlib==3.0.3 -y

            jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
            jupyter labextension install jupyterlab-plotly --no-build
            jupyter labextension install plotlywidget --no-build
            jupyter labextension install @pyviz/jupyterlab_pyviz --no-build
            jupyter lab build

            <!-- (Remember to also setup a dot env file containing api keys. You will need keys for both alphavantage and newsapi)  -->
            
* ###  Other libraries - can be quick installed using the following commands in the pyviz environment:

pip install pathlib 
pip install requests
pip install datetime
            
           
             <!-- (The following will need to be run in google co lab before importing anything and working with the machine learning models.Remember to include an ! at the beginning of the install in order to run it) -->
            
           pip install AlphaVantage
           pip install utils
           pip install hvplot
           pip install streamlit
           
Avi, paste in any additional pip installs here.



## Overall Aim 

The aim of this project is to give investors a holistic view of the performance and potential trajectory of six different crypto currencies. We designed a streamlit app that provides clear insights and easily comprehensible data about both the close price of the currency and the sentiments expressed in news articles about the currecy. The app is user friendly and provides timeline graphs as well as dataframes with the original data should users want to drill down further.

The following currencies and coins will be the focus of the analysis 

   * Bitcoin
   * Ethereum
   * Luna
   * Binance
   * Cardano
   * Solana

The components of the analysis provided in the app are listed below:

* Evan - historical close values and logistic regression model
* Christine - Alphavantage news and intelligence sentiment analysis
* Avi - additional news api and streamlit app design

## General Process

* ## Historical data
Our app takes data on the historical close prices of crypto currencies from Alpha Vantage Cryptocurrencies API. We collected data beginning August 21, 2020 (due to limitations of the API). We pulled data for each of the six crypto currencies and organized them into dataframe. We then cleaned and regularized the data and dropped extraneous columns. 

Once the data cleaning was complete, we imported scikit learn and created a logistic regression model for each dataframe to forecast close prices of the cryptos. The features our model took into consideration were 'open price', 'high', 'low', 'volumn' and 'market cap'. The dataframe with the models' predcitions were then added to the streamlit application to be viewable by the user.

* ## News APIs and Sentiment analysis

We collected articles for sentiment analysis using two separate APIs. We used the Alpha Vantage News and Intelligence API as well as the News API. Below is a brief outline of the process for pulling and cleaning the data from each API as well as a description of how we conducted sentiment analysis. The sentiment scores from our analysis compiled into a dataframe for each crypto currency and the data frames are included on the streamlit application for the user to view.

**Alpha Vantage News and Intelligence APIs and Sentiment analysis**

Alpha Vantage Market News & Sentiment historical data begins March 01, 2020. Sentiment scores and labels were gathered within the parameters of the API call. 200 results for each month March-July per crypto were requested and gathered into a dataframe.

**News API and Sentiment analysis**

Avi can you give a brief overview of your steps here


* ## Setting up the streamlit application

After creating dataframes for the historical performance and model predictions and the sentiment analysis from both APIs, we designed a streamlit application that would a allow a user to select which of the six crypto currencies they wished to see data about. The application would display they dataframes and had options to highlight the high and low values in the historical performance. The application also included interactive graphs demonstrating how the sentiment analysis scores and historical performance tracked with each other.





