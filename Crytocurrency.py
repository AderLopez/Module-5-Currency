#second example:
#To install the nasdaqdatalink run = python -m pip install nasdaq-data-link    
import nasdaqdatalink
import pandas as pd
import pygal
from datetime import timedelta


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

    #Code to obtain one week of data:
    last_7_days = TVTVR_data_temp_date_max - timedelta(days=7)
    TVTVR_data_temp = TVTVR_data[(TVTVR_data['date'] >= '2016-07-14') & (TVTVR_data['date'] <= TVTVR_data_temp_date_max)]
    print(TVTVR_data_temp)
    #TVTVR_data_temp = TVTVR_data.head(100)


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
        chart.title=('Bitcoin Trade Volume vs Transaction Ratio')
        chart.x_labels = dates
        chart.add("values", value)
        chart.render_to_file('static/Peru_unemployment.svg') #svg format
    return