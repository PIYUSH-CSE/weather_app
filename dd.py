import json
from itertools import islice
import pandas as pd

with open('days.json', 'r') as f:
    data = json.load(f)
Min_temp=[]
Max_temp=[]
for i in range(40):
    Min_temp.append(data['list'][i]['main']['temp_min']-273.15)
    Max_temp.append(data['list'][i]['main']['temp_max']-273.15)

length_to_split = [5,5,5,5,5]
Inputt = iter(Max_temp)
Output = [list(islice(Inputt, elem))
        for elem in length_to_split]

Maxi=[]
for i in Output:
    Maxi.append(max(i))


Inputt = iter(Min_temp)
Output = [list(islice(Inputt, elem))
        for elem in length_to_split]
Mini =[]
for i in Output:
    Mini.append(min(i))

