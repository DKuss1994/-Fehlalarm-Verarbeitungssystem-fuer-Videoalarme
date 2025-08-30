import pandas as pd


def load_customer_data(excel_path, objekt_id):
    df = pd.read_excel(excel_path, engine="openpyxl")
    row = df[df["Objekt-ID"] == objekt_id]

    if row.empty:
        return None  # nichts gefund
    else:
        return row.to_dict(orient="records")[0]

