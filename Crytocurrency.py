#second example:
#To install the nasdaqdatalink run = python -m pip install nasdaq-data-link    
import nasdaqdatalink
import pandas as pd
import pygal
from datetime import timedelta, date
import urllib.request
import json



def cryptocurrency():
#Configuring the information for a dataframe to be displayed when printing:
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 12)
    pd.set_option('display.width', 400)

    #Using the API key and loading all the data:
    nasdaqdatalink.ApiConfig.api_key = 'CzrvEnaNLwQVBiWQQNF-'
    TVTVR_data = nasdaqdatalink.get_table('QDL/BCHAIN',  code= 'TVTVR') #TVTVR - Bitcoin Trade Volume vs Transaction Volume Ratio

    #Code to obtain the min and max dates:
    TVTVR_data_temp_date_min =TVTVR_data['date'].min()
    print(TVTVR_data_temp_date_min)
    TVTVR_data_temp_date_max =TVTVR_data['date'].max()
    print(TVTVR_data_temp_date_max)


    #Obtaining the current bitcoin rate:
    TVTVR_current= TVTVR_data[TVTVR_data['date'] == TVTVR_data_temp_date_max]
    TVTVR_current_rate = TVTVR_current.iloc[0,2]
    TVTVR_current_date = TVTVR_current.iloc[0,1].strftime('%Y-%m-%d')
    
    print(TVTVR_current_date)

    #Code to obtain one week of data:
    last_7_days = TVTVR_data_temp_date_max - timedelta(days=7)
    TVTVR_data_temp = TVTVR_data[(TVTVR_data['date'] >= last_7_days) & (TVTVR_data['date'] <= TVTVR_data_temp_date_max)]
    #print(TVTVR_data_temp)
    #TVTVR_data_temp = TVTVR_data.head(100)

    TVTVR_data_temp = TVTVR_data_temp.sort_values(by='date', ascending=True) 
    print(TVTVR_data_temp)

    #Formatting the data to print the graph
    TVTVR = {
        "TVTVR": "Bitcoin Trade Volume vs Transaction Volume Ratio",
        "Code": TVTVR_data_temp.iloc[0,0],
        "Date": TVTVR_data_temp.iloc[0,1],
        "Value": TVTVR_data_temp.iloc[0,2],

    }

    #create an empty list to store the fetched data
    TVTVR_list = []

    for index, row in TVTVR_data_temp.iterrows():

        #This is a way to convert to SQL
        date = row[1].strftime('%Y-%m-%d')

        #Append the date and the row
        TVTVR_list.append((date,row[2]))

        #Extract and separate the list for date and values
        dates,value = zip(*TVTVR_list)


        #To draw a line
        chart = pygal.Line(x_label_rotation = 45)
        chart.title=('Bitcoin Trade Volume vs Transaction Ratio')
        chart.x_labels = dates
        chart.add("values", value)
        chart.render_to_file('static/Bitcoin_Trade_vs_Transaction_volume_Ratio.svg') #svg format


    #Part 2: 
    #Using the API key and loading all the data:
    #we will be retrieving Peru (PER) and Employment in millions LE
    #The code of the table is 'QDL/ODA for IMF Cross Country Macroeconomics Statistics'
    #https://data.nasdaq.com/databases/ODA#anchor-product-overview
    QDL_ODA = nasdaqdatalink.get_table('QDL/ODA', indicator='PER_LUR')
    print(QDL_ODA)

    #Code to obtain the min and max dates:
    IMF_Cross_Country_Macroeconomic_Statistics_Min =QDL_ODA['date'].min()
    print(IMF_Cross_Country_Macroeconomic_Statistics_Min)
    IMF_Cross_Country_Macroeconomic_Statistics_Max =QDL_ODA['date'].max()
    print(IMF_Cross_Country_Macroeconomic_Statistics_Max)

    #After analyzing the information we saw that we have data for the 2021 period, which will be analyze.
    QDL_ODA_temp = QDL_ODA[(QDL_ODA['date'] >= '2000-01-01') & (QDL_ODA['date'] <= '2024-12-31')]
    #QDL_ODA_temp =QDL_ODA

    QDL_ODA_temp = QDL_ODA_temp.sort_values(by='date', ascending=True) 
    print(QDL_ODA_temp)

    #create an empty list to store the fetched data
    QDL_ODA_list = []

    for index, row in QDL_ODA_temp.iterrows():

        #This is a way to convert to SQL
        date = row[1].strftime('%Y-%m-%d')

        #Append the date and the row
        QDL_ODA_list.append((date,row[2]))

        #Extract and separate the list for date and values
        dates,value = zip(*QDL_ODA_list)


        #To draw a line
        chart = pygal.Line(x_label_rotation = 45)
        chart.title=('Peru Unemployment Rate from 2000 to 2024')
        chart.x_labels = dates
        chart.add("values", value)
        chart.render_to_file('static/Peru_unemployment.svg') #svg format
    return 



def Bitcoin_rate():

    #To store the data 
    data = []

    #This is the data for 7 days:
    #for value in range(7): #from 0 to 6


    #From testing we see that the data is from one day before the current date:
    Current_Date = date.today() - timedelta(days=1)
    print(Current_Date)
    print(date.today())

    #This will be the code for only current date:
    for value in range(1): #from 0 to 6
        
        #The data will be taken from the 2nd of march plus to 7 days more.
        url=f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{Current_Date}/v1/currencies/btc.json'
        request = urllib.request.urlopen(url)
        result = json.loads(request.read())
        data.append(result["btc"]["usd"])   
        
    Current_rate_btc = round(data[0],2)
    print(Current_rate_btc)

    #To store the data 
    data1 = []

    #This will be the code for only current date:
    for value in range(1): #from 0 to 6
        
        #The data will be taken from the 2nd of march plus to 7 days more.
        url=f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{Current_Date}/v1/currencies/usd.json'
        request = urllib.request.urlopen(url)
        result = json.loads(request.read())
        data1.append(result["usd"]["jpy"])   
        
    Current_rate_jpy = round(data1[0],2)
    print(Current_rate_jpy)


    return Current_rate_btc, Current_rate_jpy, Current_Date