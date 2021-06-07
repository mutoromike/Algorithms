import numpy as np
import pandas as pd
import glob


def clean_data():
    all_data = pd.DataFrame()
    for f in glob.glob("./Pandas/files2/*"):
        print("sdfsdfdf", f)
        df = pd.read_csv(f, encoding='latin-1')
        all_data = all_data.append(df,ignore_index=True)
        print(all_data)
        # print(all_data)
        all_data.fillna(value='')
    all_data.to_csv("final2.csv")

    return


clean_data()

