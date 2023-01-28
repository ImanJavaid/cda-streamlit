# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:45:25 2023

@author: imanj
"""

import pandas as pd
import streamlit as st

#reading the file
df= pd.read_csv('Billionaire.csv')

# df = read_excel(filename)

# data cleaning
new_column  = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))
df['NetWorth ($B)'] = new_column


st.title('Billionaire Dataset')

all_countries = sorted(df['Country'].unique())
col1, col2 = st.columns(2)

# COLUMN 1
# display on streamlist
selected_country = col1.selectbox('Select Your Country', all_countries)
#subest on selected country
subset_country = df[df['Country'] == selected_country]

# get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())
#display multi select option on the sources
selected_source = col1.multiselect('Select Source of Income', sources)
# subset on the selected sources
subset_source = subset_country[subset_country['Source'].isin(selected_source)]

#COLUMN 2
main_string='{} - Billionaires'.format(selected_country)

col2.header(main_string)
col2.dataframe(subset_country)
col2.header('Source wise info')
col2.dataframe(subset_source)




