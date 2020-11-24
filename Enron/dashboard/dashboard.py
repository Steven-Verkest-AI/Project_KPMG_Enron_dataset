import streamlit as st
import numpy as np
import pandas as pd
import datetime
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

@st.cache
def load_data():
    DATA_URL = ('./data/reduced_mails_FINAL.csv')

    #def load_data():
    df = pd.read_csv(DATA_URL, nrows=5000)
    df['Date'] = pd.to_datetime(df['Date'],utc=True)
    df = df.set_index(pd.DatetimeIndex(df['Date']))
    return df

@st.cache
def load_sentiment():
    SENTIMENT_URL = ('./data/emotional_content.csv')
    dfs = pd.read_csv(SENTIMENT_URL, nrows=5000)
    dfs['Date'] = pd.to_datetime(dfs['Date'],utc=True)
    dfs = dfs.set_index(pd.DatetimeIndex(dfs['Date']))
    return dfs

def main():

    pages={
        'Company communications': page_first,
        'Employee communications': page_second,
        'Employee churn analytics':page_third,
        'Social networks': page_fourth,
        'Fraud analytics': page_fifth,
        }

    st.sidebar.title('Views')

    page = st.sidebar.radio('Select view', tuple(pages.keys()))

    pages[page]()

def page_first():
    st.title('Company communications dashboard')

    df = load_data()
    dfs = load_sentiment()

    selecteddate = st.date_input("Select date range", [df.index.min(), df.index.max()])

    #Resample email traffic by day
    chart_data = df.resample('D').size()

    #Plot email traffic
    st.line_chart(chart_data)

    #Create a plotly big indicator card
    fig = go.Figure(go.Indicator(
        mode = "number+delta",
        value = 400,
        number = {'prefix': "$"},
        delta = {'position': "top", 'reference': 320},
        domain = {'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor = "lightgray")
    st.plotly_chart(fig)

    #Plot sentiment
    st.subheader('Sentiment Trends')
    chart_data_sentiment = dfs.resample('D').size()
    st.line_chart(chart_data_sentiment)

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 200,
        title = {"text": "Emails volume<br>"},
        domain = {'x': [0, 0.5], 'y': [0, 0.5]},
        delta = {'reference': 400, 'relative': True, 'position' : "bottom"}))

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 350,
        title = {"text": "Emails recieved<br>"},
        delta = {'reference': 400, 'relative': True},
        domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 450,
        title = {"text": "Emails sent<br>"},
        delta = {'reference': 400, 'relative': True},
        domain = {'x': [0.6, 1], 'y': [0, 1]}))
    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 450,
        title = {"text": "Another indicator<br>"},
        delta = {'reference': 400, 'relative': True},
        domain = {'x': [0.6, 1], 'y': [0, 1]}))
    #Show plotly big indicator card
    fig.update_layout(paper_bgcolor = "lightblue")
    st.plotly_chart(fig)
    st.subheader('Email traffic last 24 hours')

    st.subheader('Email traffic heatmap past week')

    st.subheader('Email traffic past month')

    st.subheader('Email traffic past year')

    st.subheader('Out of hours emails past week')

    st.subheader('Out of hours emails past month')

    st.subheader('Out of hours emails past year')

    st.subheader('Main topics mentioned in past 24 hours')

    st.subheader('Main topics mentioned in past week')

    st.subheader('Main topics mentioned in past month')

    st.subheader('Main topics mentioned in past year')

#can also use st.dataframe() and st.table()

def page_second():
    st.title('Employee communications dashboard')

    df = load_data()
    dfs = load_sentiment()
    employee = st.selectbox("Select employee", df["From"].unique())

    st.write('Time at company')


    #Create a plotly gauge indicator
    fig = go.Figure()
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 70,
        title = {'text': "Postive"},
        domain = {'x': [0, 1], 'y': [0, 1]}
        ))
    #setting range of x-axis doesn't work
    fig.update_xaxes(range=[0,100])
    st.plotly_chart(fig)

    fig = go.Figure()
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 30,
        title = {'text': "Negative"},
        domain = {'x': [0, 1], 'y': [0, 1]}
        ))
    #setting range of x-axis doesn't work
    fig.update_xaxes(range=[0,100])
    st.plotly_chart(fig)

    st.subheader('Overall Sentiment emails sent')

    st.subheader('Overall Sentiment emails received')

    st.subheader('Profanity emails sent')

    st.subheader('Profanity emails received')

    st.subheader('Emails sent')

    st.subheader('Emails received')

    st.subheader('Emails received')

    st.subheader('Out of hours emails')

    st.subheader('Response rate')

    st.subheader('Time spent on email')




def page_third():
    st.title('Employee Churn Analytics')
    st.subheader('A subheader here')

def page_fourth():
    st.title('Social networks')

    df = load_data()
    dfs = load_sentiment()
    employee = st.selectbox("Select employee", df['From'].unique())

    st.write('This is the social network of', employee)

# Create From network from edgelist

    G_rt = nx.from_pandas_edgelist(
    df=df[df.From.str.contains(employee)],
    source = 'From',
    target = 'To',
    create_using = nx.DiGraph())

# Create random layout positions
    pos = nx.random_layout(G_rt)

# Create size list
    sizes = [x[1] for x in G_rt.degree()]

# Draw the network
    fig, ax = plt.subplots()

    ax = nx.draw_networkx(G_rt, pos,
        with_labels = False,
        node_size = sizes,
        width = 0.1, alpha = 0.7,
        arrowsize = 2, linewidths = 2)

    st.pyplot(fig)

def page_fifth():
    st.title('Fraud Analytics')
    st.subheader('A subheader here')
    df = load_data()
    dfs = load_sentiment()

if __name__ == '__main__':

    main()
