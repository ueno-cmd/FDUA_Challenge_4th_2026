# 第4回金融データ活用チャレンジ (FDUA Challenge 4th)

## コンペティション概要 (Overview)
**テーマ: 生成AIをバディ（相棒）として活用し、データに基づいた価値ある提案書を作成する**

### 背景・目的
地域金融機関において、取引先企業の持続的成長を支援することは重要な使命です。
しかし、財務データのみならず、業界動向や地域特性、技術トレンドといった非財務情報までを網羅的に分析し、有益な提案を行うには高度な専門性と多大な時間を要します。
本コンペティションでは、生成AIを活用した金融実務の高度化と、新しい「事業性評価」の形を模索します。

## アプローチ方針 (Approach)
本プロジェクトでは、以下の役割分担で分析とレポート作成を進めます。

1.  **データ処理・詳細分析 (Analytics)**
    *   **Dataiku** を活用して、データの加工、特徴量エンジニアリング、および詳細な分析を行います。
    *   レポーティングに必要な図表やインサイトの抽出はDataiku上で行います。

2.  **簡易EDA (Preliminary EDA)**
    *   初期段階のデータ傾向把握として、ローカル環境のPython (Marimo, Altair) を使用しました。
    *   主な確認事項: データの基本統計量、欠損値、主要変数（売上高などを）の分布確認。

3.  **レポート作成 (Reporting)**
    *   LLMを活用し、Dataikuで得られたインサイトを元にレポート文章を生成・推敲します。

## 技術スタック (Tech Stack)
*   **Analysis Platform**: Dataiku DSS
*   **Local Python Environment**:
    *   Language: Python
    *   Package Manager: uv
    *   EDA Tools: Marimo, pandas, Altair
    *   Visualization: Altair
*   **Report Generation**: LLM (Azure OpenAI gpt-5.2, gpt-5-mini, text-embedding-3-large)

## ディレクトリ構成
*   `01_input/`: 配布データ (financial_data.csv、securities_report(有価証券報告書フォルダ))→コンペ終了後削除
*   `02_output/`: 生成物
*   `03_notebook/`: ローカルEDA用Notebook
*   `04_others/`: その他資料
