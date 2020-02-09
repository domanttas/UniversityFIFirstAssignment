import pandas as pd

def load(data):
    result = pd.read_csv(data, parse_dates=['Local time'])

    return pd.DataFrame(result)
