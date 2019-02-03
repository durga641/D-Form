# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:29:41 2019

@author: Venkat Durga Rao
"""

import numpy as np
import pandas as pd

data=np.random.randint(1,30,size=(4,5))
np.random.seed(100)
df=pd.DataFrame(data,index=['a','b','c','d'],columns=['one','two','three','four','five'])
df2=pd.DataFrame(data)
print(df)
df[1]['two']
df['two'][1]
df[4]['four']

type(df.iloc[[1],[0,1]] )  #### out put is dataframe
type(df.iloc[1,[0,1]] ) #### output is series
df[(df['three'] > 10 )  &  (df['four'] < 10)]
df.iloc[[1],[0,1]] )


type(df.loc[[1],[0,1]] )  #### out put is dataframe using labled index mechanism
type(df.loc[1,[0,1]] ) #### output is series with labeled index mechanism

df[1:,['0','1']]

df.iloc[1:,[0,1]] 

df[['one','two']]

df['five']=df['one']+df['three']

df.append(df[df['three'] > 10 ])

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
    df.apply(np.mean)
    
    list(df.index)


