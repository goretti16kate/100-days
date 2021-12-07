import pandas as pd
threshold = 0.1
i = pd.read_csv('/home/k4t13/Documents/blms.csv')
#print(i)
above_threshold = i.loc[i["Threshold"]> threshold,"state"]
print(list(above_threshold))
#i["Add_me"]= i["TotalAtendance"]+i["TotalPopulation"]
#print(i)
#adding a column