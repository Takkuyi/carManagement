# check_headers.py
import pandas as pd

df = pd.read_csv("uploads_etc_data/202504031446.csv", encoding="shift_jis")
print("📋 カラム名一覧：")
for col in df.columns:
    print(f"- {col}")
