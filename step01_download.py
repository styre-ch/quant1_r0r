from pathlib import Path

import akshare as ak


def main():
    # 项目目录 Project directory
    project_dir = Path(__file__).resolve().parent

    # 原始数据目录 Raw data directory
    data_dir = project_dir / "data" / "raw"
    data_dir.mkdir(parents=True, exist_ok=True)

    print("正在获取行情，请等待……", flush=True)

    # 获取日频、不复权行情
    df = ak.stock_zh_a_hist(
        symbol="000001",
        period="daily",
        start_date="20240101",
        end_date="20241231",
        adjust="",
        timeout=30,
    )

    # 空数据不视为成功
    if df is None or df.empty:
        raise RuntimeError("接口没有返回行情数据，未保存文件。")

    # 保存接口返回的数据，不填充、不删除记录
    output_file = data_dir / "000001_2024_unadjusted.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print("\n前5行数据：")
    print(df.head().to_string(index=False))

    print(f"\n总记录数：{len(df)}")
    print(f"字段名称：{list(df.columns)}")
    print(f"保存位置：{output_file}")
    print("\nDownload OK")


if __name__ == "__main__":
    main()