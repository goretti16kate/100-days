#from playsound import playsound 
#playsound('path')
"""from PIL import Image 

image= Image.open()
created = image.Crop()

"""
"""lst1= []
lst1=[item for item in input ("enter the words you want to guess: ").split()]
print (lst1)"""

import pandas as pd 
import csv 
reader = csv.DictReader(open("blms.csv"))
for raw in reader:
    print (raw)
