#%%
import requests
import pandas as pd
import streamlit as st
from datetime import date, timedelta
from awesome_table import AwesomeTable
from awesome_table import Column 


today = date.today()

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield end_date - timedelta(n)

# %%

st.set_page_config(page_title='NYC Permits by Abdullah Ramadan', page_icon='📊', layout='wide')
st.title('New York City Permit Issuance')

response = []

for i in daterange(today - timedelta(weeks=2), today):
    url = 'https://data.cityofnewyork.us/resource/ipu4-2q9a.json?issuance_date={}'.format(i.strftime("%m/%d/%Y"))
    for job in requests.get(url).json():
        response.append(job)

df = pd.DataFrame(response)
df.to_excel('./output.xlsx')

with open('./output.xlsx', 'rb') as f:
   st.download_button('Download as Excel', f, file_name='NYC_Permits.xlsx')  # Defaults to 'application/octet-stream'

AwesomeTable(df, columns=[
    Column(name='borough', label='Borough'),
    Column(name='street_name', label='Street Name'),
    Column(name='issuance_date', label='Permit Issue Date'),
    Column(name='job_start_date', label='Job Start Date'),
    Column(name='permittee_s_first_name', label='Permittee First Name'),
    Column(name='permittee_s_last_name', label='Permittee Last Name'),
    Column(name='permittee_s_business_name', label='Permittee Business Name'),
    Column(name='permittee_s_phone__', label='Permittee Phone Number'),
    Column(name='owner_s_business_name', label='Owner Business Name'),
    Column(name='owner_s_first_name', label='Owner First Name'),
    Column(name='owner_s_last_name', label='Owner Last Name'),
    Column(name='owner_s_phone__', label='Owner Phone Number'),
], show_order=True, show_search=True, show_search_order_in_sidebar=True)
