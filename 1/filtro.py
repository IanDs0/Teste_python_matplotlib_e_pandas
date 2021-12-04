import pandas as pd
import matplotlib.pyplot as plt

#linux
#lol = pd.read_csv('./2021_LoL_esports.csv')
#windows
lol = pd.read_csv('1\LOL2021_LoL_esports.csv')

#Liga/Time/Resltado/
lol_partidas = lol.groupby(['team','league','result'])['result'].count()/6

print(lol_partidas.head())

#plt.bar(lol_partidas['team'],lol_partidas['result'])
lol_partidas.plot(kind = 'bar')