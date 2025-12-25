import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

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

#print(current_drivers_df.head(20))
#Missing Hadjar, Bortoleto, Antonelli b/c they are rookies

results = pd.read_csv('data/results.csv')

#print(results.head())

results.drop(['positionText'], axis=1, inplace=True)
results.drop(['resultId'], axis=1, inplace=True)
results.drop(['time'], axis=1, inplace=True)
results.drop(['rank'], axis=1, inplace=True)


print(results.dtypes)

numerical_dataset = results.select_dtypes(include=['number'])

plt.figure(figsize=(12,6))
sns.heatmap(numerical_dataset.corr(),
            cmap = 'BrBG',
            fmt = '.2f',
            linewidths = 2,
            annot = True)

#plt.show()

current_drivers_results = results[results["driverId"].isin(current_drivers_df["driverId"])]


# s = (current_drivers_results.dtypes == 'object')
# object_cols = list(s[s].index)

# print(len(object_cols))
# OH_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
# OH_cols = pd.DataFrame(OH_encoder.fit_transform(current_drivers_results[object_cols]))
# OH_cols.index = current_drivers_results.index
# OH_cols.columns = OH_encoder.get_feature_names_out()
# df_res_final = current_drivers_results.drop(object_cols, axis=1)
# df_res_final = pd.concat([df_res_final, OH_cols], axis=1)

# print(df_res_final.shape)

# X = df_res_final.drop(['position'], axis=1)
# Y = df_res_final['position']

# X_train, X_valid, Y_train, Y_valid = train_test_split(
#     X, Y, train_size=0.8, test_size=0.2, random_state=0)


#Current issue: before we get into one hot encoding, or anything, I need a way to handle the /N values
# in the relevant columns. We could do a "DNF", or Did Not Finish, by setting all /N values
# to some punishment value. I.e. for milliseconds, we set all DNF to some substantial time
# that is much slower than the slowest racer who did finish.