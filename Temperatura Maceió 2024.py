import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

caminho_arquivo = r'C:\Users\Usuário\Documents\Climatologia Local - Projeto 1\2000\2000\INMET_CO_DF_A001_BRASILIA_07-05-2000_A_31-12-2000.CSV'

df = pd.read_csv(
    caminho_arquivo, 
    sep=';',              
    skiprows=8,           
    decimal=',',          
    encoding='latin-1'   
    )

df['DATA (YYYY-MM-DD)'] = pd.to_datetime(df['DATA (YYYY-MM-DD)'])
df = df.dropna(axis=1, how='all')
df = df.replace(-9999, np.nan)
print(df.columns.tolist())
plt.figure(figsize=(12, 5))
plt.plot(df['DATA (YYYY-MM-DD)'], df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'], color='red', linewidth=0.8)
plt.title('Temperatura Horária - Brasília (Maio a Dezembro de 2000)', fontsize=14)
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
print(df.head(15))