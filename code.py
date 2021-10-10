# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head()


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event']) 

better_event = data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here
from functools import reduce

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(index=len(top_countries) - 1, axis=0, inplace=True)

def top_ten(df, column_name):
    country_list = []
    country_list = list(df.nlargest(10, column_name)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = list(reduce(np.intersect1d, (top_10_summer, top_10_winter, top_10)))


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.plot(summer_df['Country_Name'], summer_df['Total_Summer'], color='blue')
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.title('Summer')
plt.show()

plt.plot(winter_df['Country_Name'], winter_df['Total_Winter'], color='red')
plt.xlabel('Country_Name')
plt.ylabel('Total_Winter')
plt.title('Winter')
plt.show()

plt.plot(top_df['Country_Name'], top_df['Total_Medals'], color='black')
plt.xlabel('Country_Name')
plt.ylabel('Total_Medals')
plt.title('Total')
plt.show()



















# --------------
#Code starts here





summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio, summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_max_ratio, winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_max_ratio, top_country_gold)


# --------------
#Code starts here



data_1=data[:-1]
data_1['Total_Points'] = (data_1['Gold_Total'] * 3) + (data_1['Silver_Total'] * 2) + (data_1['Bronze_Total'])
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


