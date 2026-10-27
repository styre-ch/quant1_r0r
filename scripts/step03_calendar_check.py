from pathlib import Path

import akshare as ak
import pandas as pd


def main():
    project_dir = Path(__file__).resolve().parent
    raw_dir = project_dir / "data" / "raw"

    start = pd.Timestamp("2024-01-01")
    end = pd.Timestamp("2024-12-31")

    # 读取本地行情，不重新下载股票数据
    prices = pd.read_csv(
        raw_dir / "000001_2024_unadjusted.csv",
        dtype={"股票代码": str},
        encoding="utf-8-sig",
    )
    actual_dates = pd.DatetimeIndex(
        pd.to_datetime(prices["日期"], errors="raise")
    ).normalize()

    print("正在获取交易日历，请等待……", flush=True)
    calendar = ak.tool_trade_date_hist_sina()

    if calendar is None or calendar.empty:
        raise RuntimeError("交易日历为空，无法完成核对。")

    calendar["trade_date"] = pd.to_datetime(
        calendar["trade_date"], errors="raise"
    ).dt.normalize()

    if calendar["trade_date"].isna().any():
        raise RuntimeError("交易日历包含空日期，需要检查。")

    if (
        calendar["trade_date"].min() > start
        or calendar["trade_date"].max() < end
    ):
        raise RuntimeError("返回的日历范围不足以覆盖研究区间。")

    # 筛选2024年，并保存本次使用的日历
    calendar_2024 = (
        calendar.loc[
            calendar["trade_date"].between(start, end),
            ["trade_date"],
        ]
        .drop_duplicates()
        .sort_values("trade_date")
    )

    if calendar_2024.empty:
        raise RuntimeError("日历中没有2024年的交易日期。")

    calendar_2024.to_csv(
        raw_dir / "trading_calendar_2024_sina.csv",
        index=False,
        encoding="utf-8-sig",
    )

    expected_dates = pd.DatetimeIndex(calendar_2024["trade_date"])

    # 比较日期集合，而不是只比较记录数量
    missing_dates = expected_dates.difference(actual_dates)
    extra_dates = actual_dates.difference(expected_dates)

    print("\n=== 交易日历核对 / Trading Calendar Check ===")
    print(f"日历交易日数 / Calendar days：{len(expected_dates)}")
    print(f"行情记录数 / Price rows：{len(prices)}")
    print(f"行情唯一日期数 / Unique dates：{actual_dates.nunique()}")
    print(f"行情重复日期数 / Duplicates：{actual_dates.duplicated().sum()}")
    print(f"日历有、行情没有 / Missing dates：{len(missing_dates)}")
    print(f"行情有、日历没有 / Extra dates：{len(extra_dates)}")

    if len(missing_dates):
        print("待核查日期：", missing_dates.strftime("%Y-%m-%d").tolist())

    if len(extra_dates):
        print("日历外日期：", extra_dates.strftime("%Y-%m-%d").tolist())

    if (
        len(missing_dates) == 0
        and len(extra_dates) == 0
        and not actual_dates.has_duplicates
    ):
        print("\n日期与本次获取的交易日历一致。")
    else:
        print("\n存在待核查项，未自动填充或删除任何行情。")


if __name__ == "__main__":
    main()