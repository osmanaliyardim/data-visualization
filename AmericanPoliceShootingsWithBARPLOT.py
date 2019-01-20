# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:49:44 2019

@author: Osman Ali Yardım

Data Visualization: Bar-Plot Work on Kaggle
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Read data
median_house_hold_in_come = pd.read_csv('MedianHouseholdIncome2015.csv', encoding="cp1252")
percentage_people_below_poverty_level = pd.read_csv('PercentagePeopleBelowPovertyLevel.csv', encoding="cp1252")
percent_over_25_completed_highSchool = pd.read_csv('PercentOver25CompletedHighSchool.csv', encoding="cp1252")
share_race_city = pd.read_csv('ShareRaceByCity.csv', encoding="cp1252")
kill = pd.read_csv('PoliceKillingsUS.csv', encoding="cp1252")

"""print(percentage_people_below_poverty_level.head())
print(percentage_people_below_poverty_level.info()) #Poverty rate must be float type

poverty_level = percentage_people_below_poverty_level.poverty_rate
print(poverty_level.value_counts()) # There are 201 "-" that is a problem


# Poverty rate of each state (not city) [WORK-1]
percentage_people_below_poverty_level.poverty_rate.replace(['-'],0.0,inplace=True)
percentage_people_below_poverty_level.poverty_rate = percentage_people_below_poverty_level.poverty_rate.astype(float)

area_list = list(percentage_people_below_poverty_level['Geographic Area'].unique())
area_poverty_ratio = []
for i in area_list:
    x = percentage_people_below_poverty_level[percentage_people_below_poverty_level['Geographic Area']==i]
    area_poverty_rate = sum(x.poverty_rate)/len(x)
    area_poverty_ratio.append(area_poverty_rate)

# Sorting
data = pd.DataFrame({'area_list':area_list, 'area_poverty_ratio':area_poverty_ratio})
new_index = (data['area_poverty_ratio'].sort_values(ascending=False)).index.values
sorted_data = data.reindex(new_index)

# Visualization of WORK-1
plt.figure(figsize=(15,10))
sns.barplot(x=sorted_data['area_list'], y=sorted_data['area_poverty_ratio'])
plt.xticks(rotation=45)
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate of Given States')"""


# Most common 15 name and surname of killed people [WORK-2]
"""print(kill.head())
kill.info()
kill.columns
print(kill.name.value_counts()) # Got a problem "TK TK"

seperate = kill.name[kill.name != 'TK TK'].str.split() # Ignore "TK TK" and seperate names and surnames
a, b = zip(*seperate) # Unzip
name_list = a + b # Bring names and surnames together again in name_list
name_count = Counter(name_list) # Count names and surnames to find most commons
most_common_names = name_count.most_common(15) # Take most common names
x,y = zip(*most_common_names) # Unzip
x,y = list(x), list(y)

# Visualization of WORK-2
plt.figure(figsize=(15,10))
sns.barplot(x=x, y=y, palette=sns.cubehelix_palette(len(x)))
plt.xlabel('Name or Surnmae of Killed People')
plt.ylabel('Frequency')
plt.title('Most Common 15 Name or Surname of Killed People')"""


# High School Graduation Rate of the Population That is Older than 25 in States [WORK-3]
"""print(percent_over_25_completed_highSchool.head())
percent_over_25_completed_highSchool.info() # percent_completed_hs must be float
print(percent_over_25_completed_highSchool.percent_completed_hs.value_counts()) # There are 197 "-" in data that must be corrected

percent_over_25_completed_highSchool.percent_completed_hs.replace(['-'],0.0,inplace=True)
percent_over_25_completed_highSchool.percent_completed_hs = percent_over_25_completed_highSchool.percent_completed_hs.astype(float)
area_list = list(percent_over_25_completed_highSchool['Geographic Area'].unique())
area_highschool = []
for i in area_list:
    x = percent_over_25_completed_highSchool[percent_over_25_completed_highSchool['Geographic Area']==i]
    area_highschool_rate = sum(x.percent_completed_hs)/len(x)
    area_highschool.append(area_highschool_rate)

# Sorting   
data = pd.DataFrame({'area_list':area_list, 'area_highschool_ratio':area_highschool})
new_index = (data['area_highschool_ratio'].sort_values(ascending=True)).index.values
sorted_data2 = data.reindex(new_index)

# Visualization of WORK-3
plt.figure(figsize=(15,10))
sns.barplot(x=sorted_data2['area_list'], y=sorted_data2['area_highschool_ratio'])
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('High School Graduate Rate')
plt.title("Percentage of Given State's Population Older Than 25 That Has Graduated from High School")"""


# Population percentages of states' races that are black, white, native american, asian and hispanic [WORK-4 : Horizontal Bar Plot]
"""print(share_race_city.head())
share_race_city.info()

share_race_city.replace(['-'],0.0,inplace=True)
share_race_city.replace(['(X)'],0.0,inplace=True)
share_race_city.loc[:,['share_white','share_black','share_native_american','share_asian','share_hispanic']] = share_race_city.loc[:,['share_white','share_black','share_native_american','share_asian','share_hispanic']].astype(float)

area_list = list(share_race_city['Geographic area'].unique())

share_white = []
share_black = []
share_native_american = []
share_asian = []
share_hispanic = []

for i in area_list:
    x = share_race_city[share_race_city['Geographic area']==i]
    share_white.append(sum(x.share_white)/len(x))
    share_black.append(sum(x.share_black)/len(x))
    share_native_american.append(sum(x.share_native_american)/len(x))
    share_asian.append(sum(x.share_asian)/len(x))
    share_hispanic.append(sum(x.share_hispanic)/len(x))
    
# Visualization of Work-4
f, ax = plt.subplots(figsize=(9,15))
sns.barplot(x=share_white,y=area_list,color='green',label='White')
sns.barplot(x=share_black,y=area_list,color='blue',label='African American')
sns.barplot(x=share_native_american,y=area_list,color='cyan',label='Native American')
sns.barplot(x=share_asian,y=area_list,color='yellow',label='Asian')
sns.barplot(x=share_hispanic,y=area_list,color='red',label='Hispanic')

ax.legend(loc='lower right', frameon='True')
ax.set(xlabel='Percentage of Races', ylabel='States', title='Percentage of Population According to Races by State')"""