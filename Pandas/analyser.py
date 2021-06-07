import pandas as pd


data = pd.read_csv("new.csv", engine="python")

rate = pd.read_csv("rate.csv", engine="python")

rate_data = rate.to_dict("index")
new_dict = {}
for k, v in rate_data.items():
    # print(f'{k} \n {v}')
    for k, v in v.items():
        # print(f'{k} : {v}')
        if k == "OPTION":
            new_dict[v] = {}
            val = v
        if k != "OPTION":
            new_dict[val][v] = k
# print(new_dict)
# print(data.to_dict('index'))

for i, row in data.iterrows():
    if int(row['March Deduction']) == 0:
        val = 0
    
    data_d = new_dict[row['FAMILY']]
    # print(row['FAMILY'])
    # print(data_d)
    value = row['March Deduction']
    # print(value)
    if value in data_d.keys():
        val = data_d[value]
    else:
        val = 0
    # print(val)
    data.at[i,'PLAN CODE'] = int(val)
print(data)
data.to_csv('out.csv', index=False)