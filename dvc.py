import pandas as pd
import os
data = {
    "name" :["sunny","hariom","vintee"],
    "Age" :[21,22,20],
    "city":["idn","Ayodhya","pune"]
}

os.makedirs("data",exist_ok=True)
df = pd.DataFrame(data)
df.to_csv("data/sample.csv",index=False)