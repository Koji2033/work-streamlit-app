# Work Streamlit App

このWork専用のPython / Streamlitアプリ開発リポジトリです。

## 構成
ChatGPT Workのクラウド環境で編集・検証 → GitHubに保存 → Streamlit Community Cloudで実行。
ローカルPCへのインストールは不要です。

## 配置設定
https://share.streamlit.io/ にサインインしてGitHubを連携し、次の設定で配置します。

- Repository: Koji2033/work-streamlit-app
- Branch: main
- Main file path: streamlit_app.py
- Python: 3.12（Advanced settings）

Deploy後に発行されるstreamlit.appのURLで使用します。Cloud側の配置・認証はこのひな型作成時点では未確認です。

## ファイル
- streamlit_app.py: 画面と処理
- requirements.txt: Python依存関係
- .streamlit/config.toml: 画面テーマと起動設定
- .gitignore: 仮想環境・認証情報などの除外

## クラウドWorkで検証
```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run streamlit_app.py --server.headless=true
```
Work内のlocalhostは内部確認用です。端末から利用するにはCommunity Cloudで発行されたURLを使います。

## 開発の進め方
このWorkでアプリの目的、入力、表示結果、保存の要否を指定してください。アシスタントが実装・検証し、このリポジトリに保存します。新しいWork環境ではリポジトリからソースを取得して依存関係を再導入します。

## 秘密情報
APIキーはソースに書かず、Community CloudのSecretsに設定します。

## 公式資料
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
