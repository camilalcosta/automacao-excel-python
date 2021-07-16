"""
@author: Camila Costa 
e-mail: camila.lcosta7@gmail.com
"""

import pandas as pd

planilha_mae = "C:/......./relatórios/Vendas.xlsx"

df = pd.read_excel(planilha_mae)

df['ID Loja'] = df['ID Loja'].str.replace(' ','_')

lojas = df['ID Loja'].unique()


for loja in lojas:
    nova_planilha = df.loc[df['ID Loja'] == loja]
    nova_planilha.to_excel(f'C:/............./relatórios/{loja}.xlsx')
        
