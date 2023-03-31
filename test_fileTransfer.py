#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:06:32 2023

@author: esnee
"""

#Inject scheduler 


#Move a file to a different place

import shutil
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 
import time
from makeSchedule import makeInputFile

#### 1. Make sure spreasheet is filled in
#### 2. Make folder for injects in scartch
#### 3. Update filepaths in this script


teamColour = 'Blue'


path_2_injects = '/home/esnee/Desktop/transferFiles/origFILE/'
path_2_active = '/home/esnee/Desktop/transferFiles/moveHERE/'

###### Read schedule file ######

makeInputFile(path_2_injects)

schedule = 'schedule_test.xlsx'

file = pd.read_excel(path_2_injects+schedule)

data_array = file.values
filenames = x_data = data_array[:,0]
folder_names = x_data = data_array[:,1]
times = x_data = data_array[:,2]


###### make overall folder ######

if not os.path.exists(path_2_active+'exercise'+teamColour):
    os.makedirs(path_2_active+'exercise'+teamColour)

###### make new folders ######

folders_2Make = np.unique(folder_names)

for i in folders_2Make:
    if not os.path.exists(path_2_active+'exercise'+teamColour+'/'+i):
        os.makedirs(path_2_active+i)

###### Cycle through time ######

times_seconds = times * 60 #convert minutes to wait to second
times_steps = times_seconds[1:]-times_seconds[:-1]

times_steps = np.insert(times_steps,0,times_seconds[0])
counter = 0

for i in times_steps:
    time.sleep(i)
    print('Moving inject '+ filenames[counter]+' now')
    specificFOLDER = folder_names[counter]
    shutil.move(path_2_injects+filenames[counter],path_2_active+'exercise'+teamColour+'/'+specificFOLDER+'/' +filenames[counter])
    counter += 1 


# filename = 
# specificFOLDER =

# s