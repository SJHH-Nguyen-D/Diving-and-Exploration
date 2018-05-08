#EDA methods for looking at your data
df.columnname.value_counts(dropna=False)
df.columnname.value_counts(dropna=False).head()

#summary statistics for outliers in the data
df.describe()

#looking at your data for outliers using visuaslization
import matplotlib.pyplot as pyplot

df.population.plot('hist')
plt.show()

"""
use barplots for discrete data
use histograms for continuous data

"""

#querying the data through subsetting your data through column/series conditions
df[df.population > 1000000000]

#box plots are good to visualize your data in a way that 
df.boxplot(column='population', by='continent', rot=90)
plt.show()

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_free', rot=70)
plt.show()

#combining two categorical columns together if they are mutually exclusive...use the pd melt method
pd.melt(frame=df, id_vars=['list of columns that you wish to keep from being melted','other names'],
		value_vars=['treatmentgroupa', 'treatmentgroupb'],
		 )