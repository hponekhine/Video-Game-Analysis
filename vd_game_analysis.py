import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reading file
vd_df = pd.read_csv('vgsales.csv')

vd_df.head(10)

#print info
print(vd_df.info())

#to view stas overview
vd_stat = vd_df.describe()

#view the null values
vd_df.isnull().sum()

vd_df['Year'].value_counts()
vd_df['Publisher'].value_counts()

#let's treat null values first
year_mode = vd_df['Year'].mode()[0]
pub_mode = vd_df['Publisher'].mode()[0]

#replacing with modes 
vd_df['Year'].fillna(year_mode, inplace = True)
vd_df['Publisher'].fillna(year_mode, inplace = True)

#check for null values again
vd_df.isnull().sum()

#check for correlation
vd_corr = vd_df.corr(numeric_only = True)

#sales comparison
vd_sales = vd_df[['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales']]
#sum all cols in vd_sales
sal_sum = vd_sales.sum()
#plot in seaborn
plt.figure(figsize= (12,8))
sns.barplot(x = sal_sum.index , y = sal_sum.values, palette= 'viridis')
plt.title('Sales Comparison in Each Region')
plt.xlabel('Name of Region')
plt.ylabel('Total Sales')
plt.show()

#publsiher influence on sales
pub_df = vd_df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending = False).head(10)
#plot pub influence
plt.figure(figsize = (12, 9))
sns.barplot(x = pub_df.index , y = pub_df.values, palette= 'pastel')
plt.title('Publisher on Global Sales')
plt.xlabel('Name of Publisher')
plt.ylabel('Global Sales')
plt.xticks(rotation = 45)
plt.show()

#groupby for sales through years
sal_yr = vd_df.groupby('Year')['Global_Sales'].sum()
plt.figure(figsize = (12, 9))
sns.lineplot(x = sal_yr.index , y = sal_yr.values, color = 'blue')
plt.title('Total Sales through Years')
plt.xlabel('Year')
plt.ylabel('Total Global Sales')
plt.show()

#check for only year is above 2015
filt = vd_df['Year'] > 2015
filt_df = vd_df[filt]

#valuecounts for genre
vd_df['Genre'].value_counts()

#compare genre sales with barplot
gen_sales = vd_df.groupby('Genre') ['Global_Sales'].sum()
#plot gen_sales
plt.figure(figsize = (12, 9))
sns.barplot(x = gen_sales.index , y = gen_sales.values, palette = 'muted')
plt.title('Sales by Genre')
plt.xlabel('Genre')
plt.ylabel('Total Global Sales')
plt.show()

#which platform makes most global sales
#check for platform value counts
vd_df['Platform'].value_counts()
#groupby platform and global sales
plat_sales = vd_df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending = False).head(12)
#plot plat_sales
plt.figure(figsize = (12, 9))
sns.barplot(x = plat_sales.index , y = plat_sales.values, palette = 'deep')
plt.title('Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Global Sales')
plt.show()

#let's plot sales for japan, eu and na
na_sales = vd_df.groupby('Year')['NA_Sales'].sum()
eu_sales = vd_df.groupby('Year')['EU_Sales'].sum()
jp_sales = vd_df.groupby('Year')['JP_Sales'].sum()

#plot 3 lines in matplot
plt.figure(figsize = (15,9))
plt.plot(na_sales.index , na_sales.values, color = 'r', label = 'Northe America')
plt.plot(eu_sales.index , eu_sales.values, color = 'b', label = 'Europe')
plt.plot(jp_sales.index , jp_sales.values, color = 'g', label = 'Japan')
plt.legend()
plt.title('Comparison of Sales on NA, EU & JAPAN')
plt.ylabel('Total Sales')
plt.show()

# Group sales by Genre
gen_na = vd_df.groupby('Genre')['NA_Sales'].sum().sort_values(ascending=False).head(6)
gen_eu = vd_df.groupby('Genre')['EU_Sales'].sum()
gen_jp = vd_df.groupby('Genre')['JP_Sales'].sum()
gen_other = vd_df.groupby('Genre')['Other_Sales'].sum()

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot for each region
sns.barplot(x=gen_na.index, y=gen_na.values, ax=axes[0, 0], palette='deep')
axes[0, 0].set_title("NA Sales by Genre")
axes[0, 0].set_xlabel("Genre")
axes[0, 0].set_ylabel("Sales")
axes[0, 0].tick_params(axis='x', rotation=90, labelsize=10)  # Rotate x-ticks and set smaller text

sns.barplot(x=gen_eu.index, y=gen_eu.values, ax=axes[0, 1], palette='dark')
axes[0, 1].set_title("EU Sales by Genre")
axes[0, 1].set_xlabel("Genre")
axes[0, 1].set_ylabel("Sales")
axes[0, 1].tick_params(axis='x', rotation=90, labelsize=10)

sns.barplot(x=gen_jp.index, y=gen_jp.values, ax=axes[1, 0], palette='bright')
axes[1, 0].set_title("JP Sales by Genre")
axes[1, 0].set_xlabel("Genre")
axes[1, 0].set_ylabel("Sales")
axes[1, 0].tick_params(axis='x', rotation=90, labelsize=10)

sns.barplot(x=gen_other.index, y=gen_other.values, ax=axes[1, 1], palette='colorblind')
axes[1, 1].set_title("Other Sales by Genre")
axes[1, 1].set_xlabel("Genre")
axes[1, 1].set_ylabel("Sales")
axes[1, 1].tick_params(axis='x', rotation=90, labelsize=10)

# Adjust layout
plt.tight_layout()
plt.show()


