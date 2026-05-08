import pandas as pd

# Configurações
file_sas = 'data/CY08MSP_STU_QQQ.SAS7BDAT'
file_csv = 'data/pisa_students_cleaned.csv'

# Colunas Essenciais (para não carregar lixo)

print("A iniciar conversão... isto pode demorar uns minutos.")

# Criar o leitor em blocos (chunks)
reader = pd.read_sas(file_sas, format='sas7bdat', encoding='latin1', chunksize=10000)

first_chunk = True
for chunk in reader:
    # Filtramos apenas as colunas que queremos (opcional, mas poupa espaço)
    # df_filtered = chunk[cols_to_keep] 
    
    # Se quiseres TUDO, usa apenas 'chunk'
    if first_chunk:
        chunk.to_csv(file_csv, index=False, mode='w')
        first_chunk = False
    else:
        chunk.to_csv(file_csv, index=False, mode='a', header=False)

print(f"Sucesso! O ficheiro foi guardado em: {file_csv}")
