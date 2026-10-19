\# A股多因子量化研究

\# A-share Multi-factor Research



\## 项目简介 / Overview



本项目研究A股多因子选股，逐步完成数据获取、

基础因子计算、因子检验、策略回测与绩效归因。



\## 当前进度 / Current Status



\- 已创建本地Git仓库并连接GitHub

\- 已搭建Python虚拟环境

\- 已完成单只股票2024年不复权日行情下载

\- 已完成基础检查：日期范围、重复日期、排序、字段缺失值

\- 已生成依赖清单 requirements.txt

\- 尚未完成交易日历核对、复权处理、因子计算与策略回测



\## 研究声明 / Disclaimer



本项目用于学习与研究，不构成投资建议。



\## 运行环境 / Environment



已测试环境：Windows、Python 3.14.3。

依赖版本见 requirements.txt。



\## 运行步骤 / How to Run



在项目根目录打开PowerShell，逐条执行。



\### 1. 创建虚拟环境



```powershell

python -m venv .venv

```



\### 2. 安装依赖



```powershell

.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt

```



\### 3. 下载示例行情



```powershell

.\\.venv\\Scripts\\python.exe step01\_download.py

```



\### 4. 检查本地数据



```powershell

.\\.venv\\Scripts\\python.exe step02\_check.py

```



\## 数据说明 / Data Notes



\- 示例股票代码：000001。

\- 请求区间：2024-01-01至2024-12-31。

\- 使用日频、不复权行情。

\- 下载结果保存在 data/raw/，不上传GitHub。

\- 基础检查通过不代表已验证全年数据完整性。

\- 数据下载依赖网络连接及上游接口可用性。

