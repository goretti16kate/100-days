from CSE8ACSV import *
import pandas as pd 

#############################
#blm_protest_data = get_blm_data("blm_state.csv")
state_populations = get_state_pops()
##############################
#DO NOT MODIFY CODE BLOCK ABOVE


# List the inputs

states=[item for item in input ("States: ").split()]
def total_blm_protests(states):
    arra = []
    for i in states:
        #get values of the keys
        the_values = state_populations.get(i)
        #create an array using the values
        arra.append(the_values)

    #add the values from the array
    additioo = sum (arra)

    print (additioo)
threshold = 0.1
def protest_attendance(threshold): 
    #read the csv file
    blm_protest_data= pd.read_csv('blm_state.csv')
    #create new column for TotalPop
    blm_protest_data["TotalPopulation"]=blm_protest_data["BlackPop"]+blm_protest_data["AsianPop"]+blm_protest_data["HispanicPop"]+blm_protest_data["WhitePop"]
    #create threshhold column
    blm_protest_data["Threshold"]=(blm_protest_data["TotalAttendance"]/blm_protest_data["TotalPopulation"])*100
    #check those above the threshold
    above_threshold = blm_protest_data.loc[blm_protest_data["Threshold"] > threshold, "State"]
    #print as a list
    return list(above_threshold)
    
    

total_blm_protests(states)
protest_attendance(threshold)