# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here
data.head(2)
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],"Both", 
(np.where(data['Total_Summer']>data['Total_Winter'],"Summer","Winter")))
print(data.head(2))
better_event=data.Better_Event.value_counts().index[0]
print(better_event)



# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[-1],inplace=True)
def top_ten(ffd,col):
    country_list=[]
    country_list=ffd.nlargest(10,col)['Country_Name']
    return country_list
top_10_summer=list(top_ten(top_countries,'Total_Summer'))
top_10_winter=list(top_ten(top_countries,'Total_Winter'))
top_10=list(top_ten(top_countries,'Total_Medals'))
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))





# --------------

# --------------
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
print(summer_df.head(10))
summer_df.plot.bar('Country_Name','Total_Summer')





# --------------


# --------------
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax()][0]
print(summer_max_ratio)
print(summer_country_gold)
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax()][0]
print(winter_max_ratio)
print(winter_country_gold)
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax()][0]
print(top_max_ratio)
print(top_country_gold)





# --------------
data_1=data
data_1.drop(data_1.index[-1],inplace=True)
data_1['Total_Points']=data_1['Gold_Total'] *3 + data_1['Silver_Total'] *2 + data_1['Bronze_Total']
most_points=data_1.Total_Points.max()
best_country=data_1.loc[data_1.Total_Points.idxmax(),'Country_Name']
print(best_country)




# --------------
#Code starts here
best=data_1[data_1['Country_Name']==best_country]
best
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)



