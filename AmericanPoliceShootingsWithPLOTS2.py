# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 08:15:11 2019

@author: Osman Ali Yardım

Data Visualization: Box, Swarm and Count Plots Work on Kaggle
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

# Manner of death, victims' genders and ages work [Work-8]
print(kill.head())
kill.info()
print(kill.manner_of_death.value_counts())
print(kill.gender.value_counts())
print(kill.age.value_counts())

# Visualization of box, swarm and count plot
sns.boxplot(x="gender", y="age", hue="manner_of_death", data=kill, palette="PRGn") # Box plot
sns.swarmplot(x="gender", y="age", hue="manner_of_death", data=kill) #Swarm plot

# ---Count plot works /start---
sns.countplot(kill.gender)
sns.countplot(kill.manner_of_death)
plt.title('Manner of death',color = 'blue', fontsize=15)

# Age of Killed People
above25 = ['above25' if i>=25 else 'below25' for i in kill.age] # list comprehension method
df = pd.DataFrame({'age':above25})
sns.countplot(x=df.age)
plt.ylabel('Number of Killed People')
plt.xlabel('Age')

# Race of Killed People
sns.countplot(data=kill, x='race')
plt.title('Race of Killed People', color='blue', fontsize=15)

# Having Mental Illness or Not for Killed People
sns.countplot(kill.signs_of_mental_illness)
plt.xlabel('Mental Illness')
plt.ylabel('Number of Mental Illness')
plt.title('Having Mental Illness or Not', color='blue', fontsize=15)

# Threat Types
sns.countplot(kill.threat_level)
plt.xlabel('Threat Types')
plt.title('Threat Types', color='blue', fontsize=15)

# Flee Types
sns.countplot(kill.flee)
plt.xlabel('Flee Types')
plt.title('Flee Types', color='blue', fontsize=15)

# Having Body Cameras or Not For P.Officers
sns.countplot(kill.body_camera)
plt.xlabel('Having Body Camera')
plt.title('Having Body Cam or Not on P.Officers', color='blue', fontsize=15)
# ---Count plot works /end---