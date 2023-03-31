#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 03:23:52 2023

@author: esnee
"""


import pandas as pd
import os 


##### Make the schedule file #####
def makeInputFile(path_2_injects):
#    path_2_injects = '/home/esnee/Desktop/transferFiles/origFILE/'
    
    # Read all files in the folder
    
    dict_folders = {'C':'CDDS', 'G':'GA' , 'T':'Tides' , 'U':'USGS' , 'F':'Felt' , 'S':'Stong Motion'}
    
    allFiles = os.listdir(path_2_injects)
    
    inject_times = []
    inject_names = []
    inject_folders = []
    
    allFiles.sort()
    
    for i in allFiles:
        if i[0] == '0':
            # Sort out name
            inject_names += [i]
            
            # Sort out time
            time_ = i[0:4]
            if time_[0:2] == '00':
                inject_times += [int(time_[2:4])]
            else:
                inject_times += [60]
                
                
            # Sort out folders GA CDDS Tide USGS PTWC Felt strong
            folderName = i[5:6]
            folderName.upper()
            inject_folders += [dict_folders[folderName]]
            
            
            
    # Make dataframe
    
    df_injects = pd.DataFrame(list(zip(inject_names,inject_folders,inject_times)), columns = ['Filename','Folder','Time'])
    
    
    # Save dataframe as an excel
    
    df_injects.to_excel(path_2_injects+'/schedule_test.xlsx', index = False)
    




        