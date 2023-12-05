import pandas as pd
import numpy as np

df=pd.read_csv('D:\Data_Excel\singapore _resale\ResaleFlatPricesBasedonApprovalDate19901999.csv')
df2=pd.read_csv('D:\Data_Excel\singapore _resale\ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv')
df3=pd.read_csv('D:\Data_Excel\singapore _resale\ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv')
df4=pd.read_csv('D:\Data_Excel\singapore _resale\ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv')
df5=pd.read_csv('D:\Data_Excel\singapore _resale\ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv')

#print(df.head())

#print(df['flat_model'].unique())

#print(df.info(),df2.info(),df3.info(),df4.info(),df5.info())

list = ["month", "town", "flat_type", "block","street_name","storey_range","floor_area_sqm","flat_model","lease_commence_date","resale_price"]
df_1 = df.merge(df2,
                   on = list,
                   how = 'outer')
#print(df_1)

list = ["month", "town", "flat_type", "block","street_name","storey_range","floor_area_sqm","flat_model","lease_commence_date","resale_price"]
df_2 = df_1.merge(df3,
                   on = list,
                   how = 'outer')
#print(df_2)

list = ["month", "town", "flat_type", "block","street_name","storey_range","floor_area_sqm","flat_model","lease_commence_date","resale_price"]
df_3 = df_2.merge(df4,
                   on = list,
                   how = 'outer')
#print(df_3)

list = ["month", "town", "flat_type", "block","street_name","storey_range","floor_area_sqm","flat_model","lease_commence_date","resale_price"]
df_4 = df_3.merge(df5,
                   on = list,
                   how = 'outer')
#print(df_4.head())
#print(df_4.info())

df_4.pop('remaining_lease_x')
df_4.pop('remaining_lease_y')

print(df_4.head())
print(df_4.info())

# a=df_4['flat_model'].unique()
# print(a)
# print(len(a))

df_4['flat_model']=df_4['flat_model'].map(str.title)

b=df_4['flat_model'].unique()
print(b)
#print(len(b))

#df_4.to_csv('singapore_resale.csv')
