import pandas as pd
chunksize = 400000
count = 0
for df in pd.read_csv('insis_data.csv', chunksize=chunksize, encoding='latin-1'):
    count = 0
    print(df)
    duplicated = df[df.duplicated(['GROWER NUMBER'], keep=False)]
    clean = df.drop_duplicates('GROWER NUMBER')
    dup = duplicated.fillna(value='')
    print(dup)
    x = clean.fillna(value='')
    print(x)
    dup.to_csv('duplicated',index=False)