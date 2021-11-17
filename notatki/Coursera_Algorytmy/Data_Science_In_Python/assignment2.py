import pandas as pd
"""
xr
Fr
"""

df=pd.read_csv('notatki/Coursera_Algorytmy/Data_Science_In_Python/NISPUF17.csv')
#%%
print(dir(df)[322:])
print(len(df.columns))
# Children VS mother education level
#%%
def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    less_hs=len([i for i in df['EDUC1'] if i==1])/len(df['EDUC1'])
    hs=len([i for i in df['EDUC1'] if i==2])/len(df['EDUC1'])
    more_hs=len([i for i in df['EDUC1'] if i==3])/len(df['EDUC1'])
    college=len([i for i in df['EDUC1'] if i==4])/len(df['EDUC1'])
    return {"less than high school":less_hs,"high school":hs,"more than high school but not college":more_hs,"college":college}
proportion_of_education()
#breastmilk vs vaccine
#%%
def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    import pandas as pd
    mb = df
    n = mb['EDUC1'].value_counts() / mb['EDUC1'].shape[0]
    li = ['less than high school', 'high school', 'more than high school but not college', 'college']
    di = {}
    i = 0
    for l in li:
        di[l] = n[i + 1]
        i += 1

    return di
proportion_of_education()
#%%
len((df['PDAT']==1)==False)
#%%
len([i for i in df['PDAT'] if i==1])
#%%
len([i for i in df['PDAT'] if i==2])
pd.isna(df['P_NUMFLU'])
#%%
#page 29
def average_influenza_doses():
    breast=df['CBF_01']    #breast=[i for i in df['CBF_01'] if pd.notna(i)]
    #array([ 1,  2, 99, 77], dtype=int64)
    vaccine=df['P_NUMFLU']    #vaccine = [i for i in df['P_NUMFLU'] if pd.notna(i)]
    #array([3., 0., 2., 1., 4., 5., 6.])
    new_df=pd.DataFrame(df, columns=['CBF_01', 'P_NUMFLU'])
    new_df.dropna(inplace=True)
    #drop_not_av.sort_values(by=['P_NUMFLU'],inplace=True)
    breast1=new_df[new_df['CBF_01'].transform(lambda x: x == 1)]
    breast2=new_df[new_df['CBF_01'].transform(lambda x: x == 2)]

    return tuple([breast1['P_NUMFLU'].mean(), breast2['P_NUMFLU'].mean()])
average_influenza_doses()
#%%
def average_influenza_doses():
    # YOUR CODE HERE

    import pandas as pd
    import numpy as np
    mb = df
    gp1 = mb[mb['CBF_01'] == 1]
    gp2 = mb[mb['CBF_01'] == 2]

    return np.mean( gp1['P_NUMFLU'] ), np.mean( gp2['P_NUMFLU'] )
average_influenza_doses()
#%%
#{sex: chicken pox}
def chickenpox_by_sex():
    #new_df=pd.DataFrame(df, columns=['SEX', 'HAD_CPOX', 'P_NUMVRC'])

    male=df[df['SEX'].transform(lambda x:x==1)] #             [1, 2])
    female=df[df['SEX'].transform(lambda x:x==2)]

    male_vax=male[male['P_NUMVRC'].transform(lambda x:x>=1)] # [nan,  3.,  0.,  2.,  1.,  4.,  5.,  6.]
    female_vax=female[female['P_NUMVRC'].transform(lambda x:x>=1)] # [nan,  3.,  0.,  2.,  1.,  4.,  5.,  6.]

    male_cpox=male[male['HAD_CPOX'].transform(lambda x:x==1)] #       [ 2,  1, 77, 99]
    female_cpox=female[female['HAD_CPOX'].transform(lambda x:x==1)]

    male_not=male_vax[male_vax['HAD_CPOX'].transform(lambda x:x==2)]
    female_not=female_vax[female_vax['HAD_CPOX'].transform(lambda x:x==2)]
    return {'male':male_cpox.__len__()/male_not.__len__(),'female':female_cpox.__len__()/female_not.__len__()}
    #return male_not.nunique()
chickenpox_by_sex()
#chickenpox vaccinated VS no chickenpox vaccinated
#VACCINATED chickenpox VS no chickenpox
#%%
#{sex: chicken pox}
def chickenpox_by_sex():
    male1=df[df['SEX'].eq(1)&df['P_NUMVRC'].ge(1)&df['HAD_CPOX'].eq(1)]
    male2=df[df['SEX'].eq(1)&df['P_NUMVRC'].ge(1)&df['HAD_CPOX'].eq(2)]
    female1=df[df['SEX'].eq(2)&df['P_NUMVRC'].ge(1)&df['HAD_CPOX'].eq(1)]
    female2=df[df['SEX'].eq(2)&df['P_NUMVRC'].ge(1)&df['HAD_CPOX'].eq(2)]
    return {'male':male1.__len__() / male2.__len__(),'female':female1.__len__() / female2.__len__()}
    #return male_not.nunique()
chickenpox_by_sex()
#chickenpox vaccinated VS no chickenpox vaccinated
#VACCINATED chickenpox VS no chickenpox

#%%
import pandas as pd
old_df=pd.read_csv('notatki/Coursera_Algorytmy/Data_Science_In_Python/NISPUF17.csv')

#n_vaccine VS n_disease
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    pox=[i for i in old_df.HAD_CPOX]
    vacc=[i for i in old_df.P_NUMVRC]
    # this is just an example dataframe
    df = pd.DataFrame( {"had_chickenpox_column": pox,
                        "num_chickenpox_vaccine_column": vacc} )
    #df=df[df['had_chickenpox_column'].eq(1)]
    df.dropna(inplace=True)
    df = df[df.had_chickenpox_column != 77]
    # here is some stub code to actually run the correlation
    corr, pval = stats.pearsonr( df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"] )
    return corr
    #return 'corr:  '+str(corr)+'     pval:  '+str(pval)
corr_chickenpox()
#%%
import numpy as np
arr=pd.array(np.random.randint( 1, 3, size=(100)))
pd.Series(arr).mean()