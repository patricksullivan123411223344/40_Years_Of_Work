from fredapi import Fred
import pandas as pd
from datetime import time
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

series = {
    "Average Weekly Earnings All": "CES0500000003", # All full-time wage and salary workers
    "Median Weekly Earnings Men": "LEU0252881500A", # Men, 16 years and over (Annual)
    "Median Weekly Earnings Women": "LEU0252881600A", # Women, 16 years and over (Annual)
    "Employment Pop Ratio": "EMRATIO", # Employment-population ratio, 16+
    "Labor Force Participation": "CIVPART", # Labor force participation rate, 16+
    "Unemployment Rate Men": "LNS14000001", # Unemployment rate, Men 16+
    "Unemployment Rate Women": "LNS14000002" # Unemployment rate, Women 16+
}

df = pd.DataFrame({ name: fred.get_series(code) for name, code in series.items() })
df.index = pd.to_datetime(df.index)
df = df.loc["1980":"2025"] # Start and end years of data range

raw_dir = Path("../data/raw/fred")
raw_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(raw_dir / "macro_demographs.csv")
print("Saved →", raw_dir / "macro_demographs.csv")