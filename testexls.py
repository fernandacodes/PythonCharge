import pandas as pd

arquivoExcel = 'compilado_das_demandas.xlsx'

planilha = pd.read_excel(arquivoExcel, sheet_name='Tutores')

pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  


print(planilha)