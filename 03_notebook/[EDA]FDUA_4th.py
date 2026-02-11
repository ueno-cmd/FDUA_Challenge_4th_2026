import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import altair as alt

    # 日本語フォント設定 (Windows環境向け)
    try:
        import japanize_matplotlib
    except ImportError:
        # japanize_matplotlibが入っていない場合は、MS Gothicなどを設定
        plt.rcParams['font.family'] = 'MS Gothic'
    return alt, mo, pd


@app.cell
def _(pd):
    # データの読み込み
    data_path = "../01_input/financial_data.csv"
    df = pd.read_csv(data_path)
    return (df,)


@app.cell
def _(df, mo):
    # 基本情報の表示
    mo.md(f"""
    ## データ基本情報
    - 行数: {df.shape[0]}
    - 列数: {df.shape[1]}
    """)
    return


@app.cell
def _(df, mo):
    mo.md("### 先頭5行")
    mo.ui.table(df.head())
    return


@app.cell
def _(df, mo):
    # 欠損値の確認
    mo.md("### 欠損値の確認")
    missing_info = df.isnull().sum()
    missing_info = missing_info[missing_info > 0]
    mo.ui.table(missing_info.reset_index(name="Missing Count"))
    return


@app.cell
def _(df, mo):
    # 統計量
    mo.md("### 統計量")
    mo.ui.table(df.describe())
    return


@app.cell
def _(alt, df, mo):
    # 数値カラムのヒストグラム (Altair)
    mo.md("### 数値データの分布 (売上高・営業利益)")

    chart_sales = alt.Chart(df).mark_bar().encode(
        x=alt.X('売上高', bin=True),
        y='count()'
    ).properties(title='売上高の分布')

    chart_profit = alt.Chart(df).mark_bar().encode(
        x=alt.X('営業利益', bin=True),
        y='count()'
    ).properties(title='営業利益の分布')

    # 横に並べて表示
    chart_dist = chart_sales | chart_profit

    return (chart_dist,)


@app.cell
def _(chart_dist, mo):
    mo.ui.altair_chart(chart_dist)
    return


@app.cell
def _(alt, df, mo):
    # 年ごとの売上高推移（全体） (Altair)
    mo.md("### 年ごとの売上高推移（合計）")

    if 'YEAR' in df.columns:
        # 集計はAltair側でもできるが、データ量削減のため事前に集計してもよい
        # ここではAltairの集計機能を使う例
        chart_year = alt.Chart(df).mark_bar().encode(
            x='YEAR:O',  # 名義尺度(Ordinal)として扱う
            y='sum(売上高):Q'
        ).properties(
            title='年別売上高合計',
            width=600
        )
    else:
        mo.md("YEARカラムが存在しません")
        chart_year = None
    return (chart_year,)


@app.cell
def _(chart_year, mo):
    if chart_year:
        mo.ui.altair_chart(chart_year)
    return


if __name__ == "__main__":
    app.run()
