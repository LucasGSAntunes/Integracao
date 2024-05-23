import pandas as pd
import datetime

def filterData(data):
    df = pd.DataFrame(data)
    date_now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_now = pd.to_datetime(date_now_str)
    
    novos_nomes = df.iloc[0]

    df = df[1:]

    df = df.rename(columns=novos_nomes)

    df["Data"] = pd.to_datetime(df["Data"])
    df["Data"] = df["Data"] - pd.Timedelta(hours=3)

    for Data in df["Data"]:
        print(Data)
        print(date_now)
        if Data < date_now:
            df = df.drop(df[df["Data"] == Data].index)

    print (df)