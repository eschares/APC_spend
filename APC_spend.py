# Compare counts of journal and year in OpenAlex and Dimensions
# Eric Schares, 4/28/24

import pandas as pd
import plotly.express as px
import streamlit as st

# had used plotly#==5.10.0
#streamlit#==1.13.0
#pandas#==1.4.2


st. set_page_config(layout="wide")

st.header('Comparison of OpenAlex and Dimensions article counts test')
st.write('Eric Schares, 4/28/24')
st.write('Pulled the counts of articles for >8700 individual journals * 5 years each. Used Dimensions document type filters (PT=Article, DT=Research Article OR Review Article), but nothing for OpenAlex.')
st.write('Recorded Unpaywall classifications. How well do they compare? Can only show a few ISSNs at a time, showing the first 10 and 50 ISSNs here.')

first10 = pd.read_csv('OpenAlex_and_Dimensions_counts_merged_first10ISSNs_withJournalName.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write('n_works is from OpenAlex, Dim_count is from Dimensions')
    st.write(first10)

st.header('Compare first 10 ISSNs')

fig = px.scatter(first10, x='n_works', y='Dim_count', color='Publisher_Journalname', symbol='key', opacity=0.7,
          title='Count of articles in OpenAlex and Dimensions, by journal/year/OA status',
          hover_name = 'Publisher_Journalname',
          hover_data = ['issn', 'year'],
          labels={
              "n_works": "OpenAlex count",
              "Dim_count": "Dimensions count"}
        )
fig.update_traces(marker=dict(size=10))

fig.add_annotation(x=550, y=120,
                        text="Lots of Letters to Editor",
                        showarrow = False,
                        ax=-120,
                        ay=100)

fig.add_annotation(x=200, y=50,
                        text="Lots of LtE",
                        showarrow = False,
                        ax=-120,
                        ay=100)

fig.add_annotation(x=700, y=750,
                        text="OpenAlex finds non-gold for some Gold journals",
                        showarrow = True,
                        ax=-100,
                        ay=-80)
fig.add_annotation(x=1280, y=1350,
                        text="",
                        showarrow = True,
                        ax=-250,
                        ay=80)
fig.add_annotation(x=200, y=250,
                        text="",
                        showarrow = True,
                        ax=50,
                        ay=-200)

fig.add_shape(type="line",
    x0=1, y0=0, x1=2000, y1=2000,
    line=dict(color="Purple", width=1, dash="dot"))

fig.update_layout(width=800, height=800)
st.plotly_chart(fig, use_container_width=True)



st.header('Expanding to compare first 50 ISSNs')
first50 = pd.read_csv('OpenAlex_and_Dimensions_counts_merged_first50ISSNs_withJournalName.csv')

if st.checkbox('Show raw data '):
    st.subheader('Raw data')
    st.write('n_works is from OpenAlex, Dim_count is from Dimensions')
    st.write(first50)

fig = px.scatter(first50, x='OpenAlex_count', y='Dim_count', color='Publisher_Journalname', symbol='key', opacity=0.7,
          title='Count of articles in OpenAlex and Dimensions, by journal/year/OA status',
          hover_name = 'Publisher_Journalname',
          hover_data = ['issn', 'year'],
          labels={
              "n_works": "OpenAlex count",
              "Dim_count": "Dimensions count"}
        )
fig.update_traces(marker=dict(size=8))

fig.add_annotation(x=1550, y=400,
                        text="Nearly all conference abstracts",
                        showarrow = False,
                        ax=-120,
                        ay=100)

fig.add_shape(type="line",
    x0=1, y0=0, x1=3000, y1=3000,
    line=dict(color="Purple", width=1, dash="dot"))

fig.update_layout(width=800, height=800)
st.plotly_chart(fig, use_container_width=True)