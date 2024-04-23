import pandas as pd

dados_titulo = {
    
    'Real Madrid': 34,
    'Barcelona': 26,
    'juventus': 12,
    'Bayer Munich': 20
}

anos_titulo = {
    
    'Real Madrid': [1959, 1996, 2001, 2006],
    'Barcelona': [1914, 1936, 1990, 2005],
    'juventus': [1995, 1997, 1998, 2002],
    'Bayer Munich': [1991, 1992, 1994, 2007]
    
}

series_dados = pd.Series(dados_titulo)

series_anos = pd.Series(anos_titulo)

data = {'titulos': series_dados, 'anos': series_anos}

dataframe = pd.DataFrame(data)

print(dataframe)