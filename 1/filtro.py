import pandas as pd
import matplotlib.pyplot as plt

#linux
lol = pd.read_csv('./1/LOL2021_LoL_esports.csv')
#windows
#lol = pd.read_csv('1\LOL2021_LoL_esports.csv')

#Agrupado - Liga/Time/Resltado/
lol_partidas = lol.groupby(['league','team','result'])['result'].count()

print(lol_partidas.head())

#Numero da partida que o Champ apareceu
lol['Champs_num'] = lol['champion'].map({'Akali': 0, 'Lee Sin': 1, 'Irelia': 2})

lol_champs = lol.groupby('champion')['champion'].count()

print(lol_champs.head())

plt.pie(lol_champs, labels=lol_champs)
plt.show()

plt.scatter(lol['league'],lol['team'])
plt.show()

lol_partidas.plot(kind = 'bar')
plt.show()