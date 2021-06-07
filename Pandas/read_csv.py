import pandas as pd
chunksize = 400000
count = 0
for df in pd.read_csv('new.csv', chunksize=chunksize, encoding='latin-1'):
    count = 0
    print(df)
    duplicated = df[df.duplicated(['GROWER_NUMBER'])]
    clean = df.drop_duplicates(subset='GROWER_NUMBER', keep='first')
    dup = duplicated.fillna(value='')
    print(dup)
    x = clean.fillna(value='')
    x.to_csv('clean.csv')
    print(x)
    dup.to_csv('duplicated.csv',index=False)