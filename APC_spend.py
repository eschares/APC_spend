# Compare counts of journal and year in OpenAlex and Dimensions
# Eric Schares, 4/28/24

import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Comparison of OpenAlex and Dimensions article counts')
st.write('Eric Schares, 4/28/24')

merged2 = pd.read_csv('OpenAlex_and_Dimensions_counts_merged_withJournalName.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(merged2)

fig = px.scatter(merged2, x='n_works', y='Dim_count', color='issn', symbol='key', opacity=0.7,
          title='Count of articles in OpenAlex and Dimensions, by journal/year/OA status',
          hover_name = 'Publisher_Journalname',
          hover_data = ['issn', 'year'],
          labels={
              "n_works": "OpenAlex count",
              "Dim_count": "Dimensions count"}
        )

fig.add_shape(type="line",
    x0=1, y0=0, x1=2000, y1=2000,
    line=dict(color="Purple", width=1, dash="dot"))

fig.update_layout(width=1200, height=800)
st.plotly_chart(fig, use_container_width=True)