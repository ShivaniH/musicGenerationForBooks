import numpy as np 
import os
import re 
from os.path import isfile, join


temp = []
f = open ('data_1/MIREX_dataset/dataset/categories.txt') 

line = f.readline ()
while (line) : 
    line = line.strip('\n').replace ('-', ' ')
    line = line.split (" ")
    temp.append ("_".join([ i for i in line if i]))
    line = f.readline()

catagory_name = np.unique(np.array (temp)) 

# print (catagory_name, catagory_name.shape)

# for i in range (1,6): 
#     folder = 'cluster_' + str(i)
#     onlyfiles = [f for f in os.listdir('data/' + folder) if isfile(join('data/' + folder, f))]
#     for File in onlyfiles : 
#         catagory = temp [int(File[:-4])]
#         os.system ('mv data/' + folder + '/' +File +" " + 'data/' + folder + '/' + catagory+ '/')

for i in range (1, 6) :
    folder = 'cluster_' + str(i)  
    sub_folders = os.listdir ('data/'  + folder)  
    for s_sub_folder in sub_folders :
        if not os.listdir ('data/' + folder + '/' + s_sub_folder ):
            os.system('rmdir data/' + folder +'/' + s_sub_folder)
         

# for i in range (1,6) : 
#     for name in catagory_name :
#         os.system ('mkdir ' + 'data' + '/cluster_'+ str(i)+ '/' + name)

# for catagory in temp : 


# list_files = os.listdir('/home2/divy.kala/Music_Generation/DeepJ/data/1') 

# for i in list_files : 
#     print (i[:-4])