import pandas as pd

print("Reading table...")
df = pd.read_csv("20191028_Matrícula_unica_2019_20190430_PUBL.CSV", sep=";", na_values=[' '],
                    
                    usecols=["NOM_RBD", "COD_REG_RBD", "RURAL_RBD", 
                    "COD_ENSE2", "COD_ENSE", "COD_DEPE2", 
                    "EDAD_ALU", "GEN_ALU", "ESTADO_ESTAB"],

                    dtype={"NOM_RBD": "string", "ESTADO_ESTAB": int, 
                    "COD_REG_RBD": int, "RURAL_RBD": int, "COD_ENSE2": int,
                     "COD_ENSE": int, "COD_DEPE2": int, 
                     "EDAD_ALU": 'Int64', "GEN_ALU": int})
print("Done")

# print(df.count()) # 3624343

# Filtro 1: Que esté funcionando normalmente (ESTADO_ESTAB == 1)
df1 = df.loc[df["ESTADO_ESTAB"] == 1]
# print(df1.count()) # 3623883

# Filtro2: Que la region sea la region metropolitana (COD_REG_RBD == 13)
df2 = df1.loc[df1["COD_REG_RBD"] == 13]
# print(df2.count()) # 1398164

# Filtro3: Que sea urbano (RURAL_RBD == 0)
df3 = df2.loc[df2["RURAL_RBD"] == 0]
# print(df3.count()) # 1354334

# Filtro4: Que sea educación básica para niños sin necesidades especiales
#   (COD_ENSE2 == 2)
df4 = df3.loc[df3["COD_ENSE2"] == 2]
# print(df4.count()) # 748338

# Filtro5: Quea sea de alguno de los 3 tipos
#   (COD_DEPE2 == 1 or COD_DEPE2 == 2 or COD_DEPE2 == 3)
# Equivalente a (COD_DEPE2 != 4 or COD_DEPE2 != 5)
df5 = df4.loc[df4["COD_DEPE2"] != 4]
df5 = df5.loc[df5["COD_DEPE2"] != 5]
# print(df5.count()) # 733026

# Filtro6: Edad al 30 de junio del año escolar sea 11 o 12
#   (EDAD_ALU > 10 and EDAD_ALU < 13)
df6 = df5.loc[(df5["EDAD_ALU"] > 10) & (df5["EDAD_ALU"] < 13)]
# print(df6.count()) # 175573

print(df6.head())
