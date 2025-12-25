import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

drivers = pd.read_csv('data/drivers.csv')
#The columns we have are:
# index(?) | driverId | driverRef | number | forename | surname | dob | nationality | url

drivers_converted = drivers.convert_dtypes()
#print(drivers_converted.dtypes)
#print(drivers.columns)

#Drop URL b/c it's useless
drivers.drop(['url'], axis=1, inplace=True)
validNumbers = drivers[drivers['number'] != "\\N"]

#print(validNumbers.head(59))

current_drivers = ["Verstappen", "Piastri", "Norris", "Leclerc", 
                   "Russell", "Alonso", "Ocon", "Hamilton", 
                   "Hülkenberg", "Stroll", "Bortoleto", "Bearman",
                   "Sainz", "Tsunoda", "Antonelli", "Albon",
                   "Hadjar", "Lawson", "Gasly", "Colapinto"]

current_drivers_df = validNumbers[validNumbers["surname"].isin(current_drivers)]

#print(current_drivers_df.head(20))
#Missing Hadjar, Bortoleto, Antonelli b/c they are rookies

results = pd.read_csv('data/results.csv')

#print(results.head())

results.drop(['positionText'], axis=1, inplace=True)
results.drop(['resultId'], axis=1, inplace=True)

#print(results.dtypes)

numerical_dataset = results.select_dtypes(include=['number'])

plt.figure(figsize=(12,6))
sns.heatmap(numerical_dataset.corr(),
            cmap = 'BrBG',
            fmt = '.2f',
            linewidths = 2,
            annot = True)

plt.show()