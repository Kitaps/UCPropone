import pandas as pd

print("Reading table...")
data = pd.read_csv("20191028_Matrícula_unica_2019_20190430_PUBL.CSV", sep=";", na_values=[' '],
                    
                    usecols=["NOM_RBD", "COD_REG_RBD", "RURAL_RBD", 
                    "COD_ENSE2", "COD_ENSE", "COD_DEPE2", 
                    "EDAD_ALU", "GEN_ALU", "ESTADO_ESTAB"],

                    dtype={"NOM_RBD": "string", "ESTADO_ESTAB": int, 
                    "COD_REG_RBD": int, "RURAL_RBD": int, "COD_ENSE2": int,
                     "COD_ENSE": int, "COD_DEPE2": int, 
                     "EDAD_ALU": 'Int64', "GEN_ALU": int})
print("Done")
