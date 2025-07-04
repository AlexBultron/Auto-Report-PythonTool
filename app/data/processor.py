import pandas as pd

def generate_report():
    data = {
        "date": pd.date_range("2024-01-01", periods=5),
        "value": [100, 110, 95, 130, 120]
    }
    df = pd.DataFrame(data)
    avg = df["value"].mean()
    return {
        "average_value": avg,
        "data": df.to_dict(orient="records")
    }
