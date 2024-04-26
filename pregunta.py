# """
#  Ingestión de datos - Reporte de clusteres
#  -----------------------------------------------------------------------------------------

#  Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
#  cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
#  por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
#  espacio entre palabra y palabra.

# """
# import pandas as pd
# # #
# # # Lectura del archivo con open()
# # # ===============================================
# # # La función readline() lee una linea a la vez
# def ingest_data():
#     filename = "clusters_report.txt"
#     #license_file=pd.read_csv('clusters_report.txt', sep=' ')
#     with open(filename, mode="r") as file:
#         datos = []
#     # #lines = license_file.read()
#         next(file)
#         next(file)
#         #next(file)    
#         for line in file:
#             lines = line.split() 
#             #print(columns)
#     # Si la línea tiene al menos 1 elemento

#     ##         if len(columns) >= 1:

#             if len(lines) >= 1:
#                 try:
#                     try_first=int(lines[0])
#                     cluster=try_first
#                     #print(cluster)
#                     cantidad_de_palabras_clave=int(lines[1]) # Convertir a entero
#                     porcentaje_de_palabras_clave=lines[2] # Convertir a flotanter
#                     principales_palabras_clave= ' '.join(lines[4:]) # Unir las palabras clave
#                     #Agregar los datos a la lista
#                     datos.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])

#                 except:
#                     # Si la línea no tiene al menos 1 columna unir palabras clave a la última línea
#                     if len(datos) > 0:
#                         principales_palabras_clave= ' '.join(lines)
#                         datos[len(datos)-1][3] += ' ' + principales_palabras_clave
                    
#     # Crear un DataFrame de Pandas, renombrar columnas y convertir tipos de datos
#     df = pd.DataFrame(datos, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
#     df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.','')
#     df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',','.')
#     df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)
  
#     df.columns= df.columns.str.replace(' ', '_').str.lower()
            
#     return df


"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd



def ingest_data():

# Leer el archivo clusters_report.txt
    with open('clusters_report.txt', 'r') as file:

        data=[]
        # Saltar las primeras 3 líneas
        next(file)
        next(file)


        for line in file:
            columns = line.split() 

            # Si la línea tiene al menos 1 columna 

            if len(columns) >= 1:
                try:
                    element_1=int(columns[0])
                    cluster=element_1
                    cantidad_de_palabras_clave=int(columns[1]) # Convertir a entero
                    porcentaje_de_palabras_clave=columns[2] # Convertir a flotante
                    principales_palabras_clave= ' '.join(columns[4:]) # Unir las palabras clave

                    #Agregar los datos a la lista
                    data.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])
                    
                except:
                    # Si la línea no tiene al menos 1 columna unir palabras clave a la última línea
                    if len(data) > 0:
                        principales_palabras_clave= ' '.join(columns)
                        data[len(data)-1][3] += ' ' + principales_palabras_clave 
               
    
    # Crear un DataFrame de Pandas, renombrar columnas y convertir tipos de datos
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',','.').astype(float)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.','')
    df.columns= df.columns.str.replace(' ', '_').str.lower()
      
    return df
