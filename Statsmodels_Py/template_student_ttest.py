# template_student_ttest.py
# from r-bloggers website
import pandas as pd
import numpy as np
import random
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
from scipy.stats import t
# from scipy import stats

seed(1)

df=pd.DataFrame({"female":np.random.randint(10, 100, size=10),
                 "male":np.random.randint(10, 140, size=10)})

print(df.head())


se_male=df.std()['male']/np.sqrt(10)

se_female=df.std()['female']/np.sqrt(10)

sed=np.sqrt((se_male**2) + (se_female**2))

t_stat=(df.mean()['male'] - df.mean()['female'])/sed
print(t_stat)

dof = 10 + 10 - 2

t_stat, p = ttest_ind(df['male'], df['female'])
print(f't={t_stat}, p={p}')
