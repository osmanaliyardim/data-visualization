# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:18:25 2019

@author: Osman Ali Yardım

Data Visualization: Pie-Chart Work on Kaggle
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

# Race rates of killed people
print(kill.head(15))
kill.info()
print(kill.race.value_counts()) # "O" means Other races
kill.race.dropna(inplace=True)

labels = kill.race.value_counts().index
colors = ['grey','blue','red','yellow','green','brown']
explode = [0,0,0,0,0,0] # Rates of pie chart
sizes = kill.race.value_counts().values

plt.figure(figsize=(7,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Killed People According to Races', color='blue', fontsize=15)