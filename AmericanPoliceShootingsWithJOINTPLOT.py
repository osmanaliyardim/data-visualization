# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:01:07 2019

@author: Osman Ali Yardım

Data Visualization: Joint-Plot Work on Kaggle
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
median_house_hold_in_come = pd.read_csv('MedianHouseholdIncome2015.csv', encoding="cp1252")
percentage_people_below_poverty_level = pd.read_csv('PercentagePeopleBelowPovertyLevel.csv', encoding="cp1252")
percent_over_25_completed_highSchool = pd.read_csv('PercentOver25CompletedHighSchool.csv', encoding="cp1252")
share_race_city = pd.read_csv('ShareRaceByCity.csv', encoding="cp1252")
kill = pd.read_csv('PoliceKillingsUS.csv', encoding="cp1252")

# High School Graduation Rate vs Poverty Rate of Each State [Work-6: Joint Plot]
percentage_people_below_poverty_level.poverty_rate.replace(['-'],0.0,inplace=True)
percentage_people_below_poverty_level.poverty_rate = percentage_people_below_poverty_level.poverty_rate.astype(float)

area_list = list(percentage_people_below_poverty_level['Geographic Area'].unique())
area_poverty_ratio = []
for i in area_list:
    x = percentage_people_below_poverty_level[percentage_people_below_poverty_level['Geographic Area']==i]
    area_poverty_rate = sum(x.poverty_rate)/len(x)
    area_poverty_ratio.append(area_poverty_rate)

# Sorting 1    
dataFrame = pd.DataFrame({'area_list':area_list,'area_poverty_ratio':area_poverty_ratio})
new_index = (dataFrame['area_poverty_ratio'].sort_values(ascending=False)).index.values
sorted_data = dataFrame.reindex(new_index) # sorted_data 1



percent_over_25_completed_highSchool.percent_completed_hs.replace(['-'],0.0,inplace=True)
percent_over_25_completed_highSchool.percent_completed_hs = percent_over_25_completed_highSchool.percent_completed_hs.astype(float)
area_list = list(percent_over_25_completed_highSchool['Geographic Area'].unique())
area_hsGraduation_ratio = []
for i in area_list:
    x = percent_over_25_completed_highSchool[percent_over_25_completed_highSchool['Geographic Area']==i]
    area_hs_rate = sum(x.percent_completed_hs)/len(x)
    area_hsGraduation_ratio.append(area_hs_rate)

# Sorting 2
dataFrame = pd.DataFrame({'area_list':area_list,'area_hsGraduation_ratio':area_hsGraduation_ratio})
new_index = (dataFrame['area_hsGraduation_ratio'].sort_values(ascending=False)).index.values
sorted_data2 = dataFrame.reindex(new_index) # sorted_data 2    

print(sorted_data.head()) # Poverty by State
print(sorted_data2.head()) # High School Graduation by State

# Normalize and combine data
sorted_data['area_poverty_ratio']=sorted_data['area_poverty_ratio']/max(sorted_data['area_poverty_ratio']) 
sorted_data2['area_hsGraduation_ratio']=sorted_data2['area_hsGraduation_ratio']/max(sorted_data2['area_hsGraduation_ratio'])
data = pd.concat([sorted_data,sorted_data2['area_hsGraduation_ratio']],axis=1)
data.sort_values('area_poverty_ratio',inplace=True)

# Joint Plot visualization of kde type (kinds: scatter, reg, resid, kde, hex)
g = sns.jointplot(data.area_poverty_ratio, data.area_hsGraduation_ratio, kind="kde", size=7)
#plt.savefig('graph.png') #to display on Kaggle platform
plt.show()

# Joint Plot visualization of other kinds (kinds: scatter, reg, resid, kde, hex)
g = sns.jointplot("area_poverty_ratio", "area_hsGraduation_ratio", data=data, size=5, ratio=3, color='b')
g = sns.jointplot(data.area_poverty_ratio, data.area_hsGraduation_ratio, kind="reg", size=5)
g = sns.jointplot(data.area_poverty_ratio, data.area_hsGraduation_ratio, kind="resid", size=5)
g = sns.jointplot(data.area_poverty_ratio, data.area_hsGraduation_ratio, kind="hex", size=5)