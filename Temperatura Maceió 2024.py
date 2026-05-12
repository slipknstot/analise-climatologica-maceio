import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

caminho_arquivo = r'C:\Users\Usuário\Documents\Climatologia Local - Projeto 1\INMET_NE_AL_A303_MACEIO_01-01-2024_A_31-12-2024.CSV'

df = pd.read_csv(
    caminho_arquivo, 
    sep=';',              
    skiprows=8,           
    decimal=',',          
    encoding='latin-1'   
    )

print(df.columns.tolist())
df['Data'] = pd.to_datetime(df['Data'])
df = df.dropna(axis=1, how='all')
df = df.replace(-9999, np.nan)
plt.figure(figsize=(12, 5))
plt.plot(df['Data'], df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'], color='red', linewidth=0.8)
plt.title('Temperatura Horária - Maceió (Janeiro a Dezembro de 2024)', fontsize=14)
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
print(df.head(15))
