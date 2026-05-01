import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Explore the Accidents Insights here👇")

df = sns.load_dataset("car_crashes")
st.dataframe(df)

fig = px.bar(df, x='abbrev', y= 'total',
            title = 'Total Accidents Statewise',
            labels = {'abbrev' : 'State','total' : 'Total Accidents'},
            template = 'plotly_dark',
            color = 'abbrev'
            )
st.plotly_chart(fig)
st.subheader("Insights")
st.markdown('''California has the highest number of total accidents,
             followed by Texas and Florida. This could be due to the larger
             population and higher traffic volume in these states. On the other hand,
             states like Vermont and Wyoming have significantly lower total accidents,
             which may be attributed to their smaller populations
             and less traffic congestion.    ''')