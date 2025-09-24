from dotenv import load_dotenv

load_dotenv()

import os
"""
### アプリ概要
単一の入力フォームに自由入力したテキストを **LangChain** 経由で **LLM** に渡し、\
回答を画面に表示します。ラジオボタンで **専門家の振る舞い**（A/B）を選べます。


**使い方**
1. 右のラジオボタンで専門家タイプ（A または B）を選ぶ。
2. テキストを入力して「送信」する。
3. 数秒後、下部に回答が表示されます。


> A：キャリア戦略の専門家 / B：グロースマーケ/起業戦略の専門家
"""
)
)


with st.sidebar:
st.header("設定")
st.caption("Streamlit Community Cloud の Secrets か、環境変数 OPENAI_API_KEY を使用します。")
show_model = st.checkbox("詳細設定を表示", value=False)
if show_model:
st.write("モデル: gpt-4o-mini / 温度: 0.3")


# --- 入力フォーム
with st.form(key="expert_form"):
col1, col2 = st.columns([1, 1])
with col1:
selection_value = st.radio(
"専門家タイプの選択",
options=["A", "B"],
index=0,
captions=[EXPERT_PROFILES["A"]["label"], EXPERT_PROFILES["B"]["label"]],
horizontal=True,
)
with col2:
st.write("")
user_text = st.text_area("入力テキスト", placeholder="相談したい内容や質問を書いてください…", height=160)
submitted = st.form_submit_button("送信", use_container_width=True)


if submitted:
if not user_text.strip():
st.warning("テキストを入力してください。")
else:
with st.spinner("LLMに問い合わせ中…"):
try:
answer = ask_expert(user_text, selection_value)
except Exception as e:
st.error(f"エラーが発生しました: {e}")
else:
st.markdown("### 回答")
st.write(answer)


# フッター
st.markdown("---")
st.caption(
"デプロイTips：`Python 3.11` で動作確認済み。`requirements.txt` に `streamlit`, `langchain`, `langchain-openai` を指定し、"
"Secrets に `OPENAI_API_KEY` を設定してください。"
)