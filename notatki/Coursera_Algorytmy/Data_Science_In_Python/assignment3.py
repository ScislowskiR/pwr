import pandas as pd
import numpy as np
import lxml
import re
energy = pd.read_excel('notatki/Coursera_Algorytmy/Data_Science_In_Python/Energy Indicators.xls', index_col=None, header=None, skipfooter=1)
GDP=pd.read_excel('notatki/Coursera_Algorytmy/Data_Science_In_Python/API_NY.GDP.MKTP.CD_DS2_en_excel_v2_3011485.xls')
ScimEn=pd.read_excel('notatki/Coursera_Algorytmy/Data_Science_In_Python/scimagojr country rank 1996-2020.xlsx')
#%%
#energy = energy[18:245].reset_index()
energy.head()
#%%
#['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
def answer_one(energy):
    energy = energy[18:245].reset_index()
    energy.drop( "index", axis=1, inplace=True)
    energy.drop( columns=energy.columns[0:2], axis=1, inplace=True)
    energy.rename(columns={energy.columns[0]:'Country',
                           energy.columns[1]:'Energy Supply',
                           energy.columns[2]:'Energy Supply per Capita',
                           energy.columns[3]:'% Renewable'}
                  ,inplace=True)
    energy['Energy Supply'].replace('...',pd.NA, inplace=True)
    energy['Energy Supply per Capita'].replace('...',pd.NA,inplace=True)
    energy.dropna(inplace=True)
    energy['Energy Supply']=pd.to_numeric( energy['Energy Supply'] )
    energy['Energy Supply per Capita']=pd.to_numeric( energy['Energy Supply per Capita'] )
    energy['Energy Supply']=energy['Energy Supply'].apply(lambda x:x*1000000)
    energy['Country'] = energy['Country'].str.replace( r'\d+', '',regex=True )
    energy['Country'] = energy['Country'].str.replace(r' \(.*\)','',regex=True)
    energy['Country']=energy['Country'].replace({"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"})
    """energy['Country'] = energy['Country'].replace({"Korea, Rep.": "South Korea",
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"})"""
    return energy
    #return list(energy['Country'])
answer_one(energy)#90838000000/286=Population
#%%
def answer_one():
    Energy = pd.read_excel( "notatki/Coursera_Algorytmy/Data_Science_In_Python/Energy Indicators.xls" )
    Energy = Energy[17:245].reset_index()
    Energy.drop( "index", axis=1, inplace=True )
    Energy.drop( columns=Energy.columns[0:2], axis=1, inplace=True )
    Energy.rename( columns={Energy.columns[0]: 'Country',
                            Energy.columns[1]: 'Energy Supply',
                            Energy.columns[2]: 'Energy Supply per Capita',
                            Energy.columns[3]: '% Renewable'}
                   , inplace=True )
    Energy['Energy Supply'].replace( '...', np.nan, inplace=True )
    Energy['Energy Supply per Capita'].replace( '...', np.nan, inplace=True )
    Energy.dropna( inplace=True )
    Energy['Energy Supply'] = Energy['Energy Supply'].apply( lambda x: x * 1000000 )

    l = []
    for i in Energy['Country']:
        i = i.split( ' (' )
        l.append( i[0] )
    Energy['Country'] = l

    li = []
    for i in Energy['Country']:
        i = re.findall( "[^0-9]+", i )
        li.append( i[0] )
    Energy['Country'] = li

    Energy.replace( {"Republic of Korea": "South Korea",
                     "United States of America": "United States",
                     "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                     "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace=True )
    return Energy

#return list(energy['Country'])
answer_one()#90838000000/286=Population
