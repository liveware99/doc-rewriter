
import pandas as pd

def extract_comply_records(filepath):
    df = pd.read_excel(filepath)
    return df[df["Level of Compliance"] == "FC"]
