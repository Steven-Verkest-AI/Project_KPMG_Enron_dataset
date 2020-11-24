import streamlit as st

import numpy as np
import pandas as pd

st.title('Company communications dashboard')

#import data
df = pd.read_csv('sortedemails.csv')

#convert columns to datetime
df['Date'] = pd.to_datetime(df['Date'],utc=True)
df = df.set_index(pd.DatetimeIndex(df['Date']))
chart_data = df.resample('D').size()
#q.plot()
st.line_chart(chart_data)


#st.write(pd.DataFrame({
#    'first column': [ 1,2,3,4],
#    'second column': [10,20, 30, 40]
#}))

#can also use st.dataframe() and st.table()

#Add a chart
#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

#st.line_chart(chart_data)

