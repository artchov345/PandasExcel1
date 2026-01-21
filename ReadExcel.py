
import pandas as Data
import time as Tempo
Excel = Data.read_excel(r'Grafico.xlsx')

stop_temas = Excel.columns.tolist()
stop_temas = stop_temas[1:]

print(stop_temas)

stop_tema = input('Choose a theme from the list below: ')
Tempo.sleep(1)
print("Okay")
Tempo.sleep(1)
stop_letra = input("Choose a letter: ").upper()

stop_numero = ord(stop_letra) - 65

stop_celula = Excel.loc[stop_numero, stop_tema]
print(f"You Chose: {stop_celula}")