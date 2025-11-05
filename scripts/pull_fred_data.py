from fredapi import Fred    
import pandas as pd  
from datetime import datetime
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

series = {
    "Productivity": "OPHNFB", # Output per hour for all workers, nonfarm business sector
    "Real Hourly Compensation": "COMPRNFB", # Real hourly compensation (adjusted for inflation) for nonfarm business sector
    "Hourly Compensation (Nominal)": "COMPNFB", # Hourly compensation (index) before inflation adjustment
    "Labor Share": "PRS85006173", # Labor share of income in the nonfarm business sector
    "Unit Labor Costs": "PRS85006112", # Costs per unit of output for labor in non-farm business sector
    "Hours Worked": "PRS85006032", # Hours worked for all persons in the nonfarm business sector
}

df = pd.DataFrame({ name: fred.get_series(code) for name, code in series.items() })
df.index = pd.to_datetime(df.index)
df = df.loc["1980":"2025"] # Start and end years of data range

raw_dir = Path("../data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(raw_dir / "wages_productivity_data.csv")
print("Saved →", raw_dir / "wages_productivity_data.csv")
