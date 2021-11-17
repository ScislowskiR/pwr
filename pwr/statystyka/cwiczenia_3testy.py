import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
x=np.random.normal(0,10,70)
normalVar = pd.DataFrame(x)
normalVar.columns = ['value']
normalVar.head()
#%%
sns.distplot(normalVar)
plt.show()
#%%
from scipy import stats
import seaborn as sns
stats.probplot(normalVar['value'], plot=sns.mpl.pyplot)
stats.probplot(x, plot=sns.mpl.pyplot)
#%%
import seaborn_qqplot as sqp
sqp.pplot(normalVar,
           x='value',
           y=stats.gamma,
          aspect=2.5,
           height = 4,
           display_kws={"identity":True}
          )
plt.title("QQ Plot")
plt.show()
#%%
from scipy.stats import normaltest
stats, p = normaltest(normalVar)
print(stats, p)
if p > 0.05:
    print ("Rozkład wygląda na normalny")
#%%
from scipy.stats import shapiro
stats, p = shapiro(normalVar)
print(stats,p)
if p > 0.05:
    print ("Rozkład wygląda na normalny")
#%%
