from decimal import Decimal, InvalidOperation, localcontext
import streamlit as st

st.set_page_config(page_title="計算機", page_icon="🧮", layout="centered")
st.title("🧮 計算機")
st.caption("数字を2つ入力して、計算方法を選んでください。")

with st.form("calculator"):
    left = st.text_input("1つ目の数字", value="10", placeholder="例：12.5")
    operation = st.selectbox("計算方法", ["＋", "−", "×", "÷"])
    right = st.text_input("2つ目の数字", value="2", placeholder="例：3")
    submitted = st.form_submit_button("計算する", type="primary", use_container_width=True)

if submitted:
    try:
        a, b = Decimal(left.strip()), Decimal(right.strip())
        if not a.is_finite() or not b.is_finite():
            raise InvalidOperation
        if operation == "÷" and b == 0:
            st.error("0で割ることはできません。2つ目の数字を変更してください。")
        else:
            with localcontext() as context:
                context.prec = 28
                if operation == "＋":
                    result = a + b
                elif operation == "−":
                    result = a - b
                elif operation == "×":
                    result = a * b
                else:
                    result = a / b
            st.metric("計算結果", str(result))
            st.caption(f"{a} {operation} {b} = {result}")
    except (InvalidOperation, ValueError, OverflowError):
        st.error("有効な数字を入力してください。小数点とマイナスも使えます。")

st.caption("計算は最大28桁の有効数字で行います。")
