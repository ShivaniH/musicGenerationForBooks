import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv ('pianoMidiVA_Init.csv')

V = df.Valence.to_numpy ()
A = df.Arousal.to_numpy ()

# data = np.array ( [[i, j] for i, j in zip (V, A)] )

# s = np.std (data, axis=0) 

# m = np.mean (data, axis = 0) 

# data = np.array( [(i - m)/s for i in data] )

# V = data[:,0]
# A = data [:,1] 

m = np.mean ( A )

print(m)
songs = []
k = 0 
for i, j in zip(V, A) : 
    if i >= 0.5 and j >= m :
        songs.append ([i, j , k])
    k += 1 

songs = np.array (songs) 
songs_nums = songs[:,2]

d = df.loc [songs_nums][['Track', 'Valence', 'Arousal']] 
d = d.sort_values (by = ['Arousal'])
print (d)

# plt.plot (V, A, 'bo') 
# plt.plot ( np.linspace (0,1,1000),  np.linspace (m,m,1000) , 'r')
# plt.plot (  np.linspace (0.5,0.5,1000) ,np.linspace (0,0.5,1000), 'r')
# plt.show ()
