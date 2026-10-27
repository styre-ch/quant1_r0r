from pathlib import Path

import pandas as pd


project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "raw" / "000001_2024_unadjusted.csv"
df = pd.read_csv(
    file_path,
    encoding="utf-8-sig",
    dtype={"股票代码": str},
)

df["日期"] = pd.to_datetime(df["日期"], errors="raise")

print("=== 基础数据检查 / Basic Data Checks ===")
print(f"记录数 / Rows：{len(df)}")
print(f"开始日期 / Start：{df['日期'].min()}")
print(f"结束日期 / End：{df['日期'].max()}")
print(f"重复日期数 / Duplicate dates：{df.duplicated(subset=['日期']).sum()}")
print(f"日期是否升序 / Sorted：{df['日期'].is_monotonic_increasing}")

print("\n各字段缺失数量 / Missing values：")
print(df.isna().sum().to_string())

print("\n前5行 / First five rows：")
print(df.head().to_string(index=False))