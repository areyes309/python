import pandas as pd
import time
from datetime import datetime

path = r"\\yourpath" + datetime.now().strftime("\\%Y\\%m-%b\\%#m-%#d-%y\\")
path1 = path+datetime.now().strftime("fileA_%Y%m%d.csv")
path2 = path+datetime.now().strftime("fileB_%Y%m%d.csv")


df_file1 = pd.read_csv(path1)
df_file2 = pd.read_csv(path2)
print("read done")

##combine all files in the list
combined_csv = pd.concat([df_file1, df_file2])
print("concat done")
##export to csv
combined_csv.to_csv(path+datetime.now().strftime("filesCombined_%Y%m%d.csv"), index=False, encoding='utf-8-sig')
print("save done")
