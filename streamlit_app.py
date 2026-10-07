import streamlit as st

st.set_page_config(page_title="Work Webアプリ", page_icon="🛠️", layout="wide")
st.title("Work Webアプリ")
st.caption("GitHub + Streamlit 開発用ひな型")
st.write("この画面を起点に、必要な機能を実装します。")
with st.form("startup_check"):
    name = st.text_input("動作確認用の名前", value="Koji")
    submitted = st.form_submit_button("動作を確認")
if submitted:
    st.success(f"{name.strip() or 'ユーザー'}さん、入力と処理が動作しています。")
