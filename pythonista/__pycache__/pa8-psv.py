from CSE8ACSV import *
import math

#############################
#blm_protest_data = get_blm_data("blm_state.csv")
state_populations = get_state_pops()
##############################
#DO NOT MODIFY CODE BLOCK ABOVE

states = []
#list_of_states = list(states)

states=[item for item in input ("States: ").split()]
print (states)
def total_blm_protests(states):
    for i in states:
        #keys= list(state_populations)
        #values = state_populations.values()
        #print (keys)
        #print (values)
        #print (i)
        #for v in states.values():
            #print (v)
        #print (state_populations.get(i))
        the_values = state_populations.get(i)
        #the_values = iter(the_values)
    
        #the_values = int(the_values)
        print (sum(the_values))
        #print (sums)
        

        


#def protest_attendance(threshold):
total_blm_protests(states)