def QuestionsMarks(strParam):
    numbers=[]
    between=[]
    for i in strParam:
        """if i.isnumeric():
            numbers.append(i)"""
        if len(numbers)==1:
            if i =='?':
                between.append(i)
        if i.isnumeric():
            print(i)
            numbers.append(i)
            if len(numbers)==2:
                if len(between)>=3:
                    if sum(map(int, numbers))>=10:
                        return True
                    between.clear()
                numbers.pop(0)

    return False

print(QuestionsMarks("arrb6???4xxbl5???eee5"))
#%%
import pandas as pd
"""
xr
Fr
"""

df=pd.read_csv('notatki/Coursera_Algorytmy/Data_Science_In_Python/NISPUF17.csv')
#%%
def chickenpox_by_sex():
    # YOUR CODE HERE
    import pandas as pd
    mb = pd.read_csv('notatki/Coursera_Algorytmy/Data_Science_In_Python/NISPUF17.csv')

    v1m = mb[(mb['P_NUMVRC'] >= 1) & (mb['HAD_CPOX'] == 1) & (mb['SEX'] == 1)]
    v2m = mb[(mb['P_NUMVRC'] >= 1) & (mb['HAD_CPOX'] == 2) & (mb['SEX'] == 1)]
    v1f = mb[(mb['P_NUMVRC'] >= 1) & (mb['HAD_CPOX'] == 1) & (mb['SEX'] == 2)]
    v2f = mb[(mb['P_NUMVRC'] >= 1) & (mb['HAD_CPOX'] == 2) & (mb['SEX'] == 2)]
    #return {'male':v1m.__len__() / v2m.__len__(),'female':v1f.__len__() / v2f.__len__()}
    rm = v1m.shape[0] / v2m.shape[0]
    rf = v1f.shape[0] / v2f.shape[0]
    r = [rm, rf]

    sex = ['male', 'female']
    d = {}
    i = 0
    for s in sex:
        d[s] = r[i]
        i += 1
    return d=={'male':v1m.__len__() / v2m.__len__(),'female':v1f.__len__() / v2f.__len__()}

chickenpox_by_sex()
#%%
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    mb = pd.read_csv( 'notatki/Coursera_Algorytmy/Data_Science_In_Python/NISPUF17.csv' )

    v1 = mb[(mb['P_NUMVRC'] >= 0) & (mb['HAD_CPOX'] <= 2)]

    no_yes = v1['HAD_CPOX']

    est_vaccine = v1['P_NUMVRC']

    # this is just an example dataframe
    df = pd.DataFrame( {"had_chickenpox_column": no_yes,
                        "num_chickenpox_vaccine_column": est_vaccine} )

    # here is some stub code to actually run the correlation
    corr, pval = stats.pearsonr( df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"] )

    # just return the correlation
    return corr

    # YOUR CODE HERE
    # raise NotImplementedError()
corr_chickenpox()
#%%
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
def answer_one():
    Energy = pd.read_excel( "notatki/Coursera_Algorytmy/Data_Science_In_Python/Energy Indicators.xls" )
    Energy.drop(Energy.index[0:17],0,inplace=True)
    Energy.drop(Energy.index[227:],0,inplace=True)
    #Energy.drop( "index", axis=1, inplace=True )
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