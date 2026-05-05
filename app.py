import streamlit as st
import ollama
import subprocess
import tempfile
import os

st.title("AI-Powered Coding System (Web UI)")

# 入力欄
problem_text = st.text_area("問題文を入力してください", height=200)

if st.button("コード生成 & 実行"):
    if not problem_text.strip():
        st.error("問題文を入力してください。")
    else:
        st.write("### 🔧 コード生成中…")

        # LLM にコード生成を依頼
        prompt = f"""
あなたは競技プログラミングのプロです。
次の問題を解く Python コードを生成してください。

問題:
{problem_text}

出力はコードのみ。説明は不要。
"""

        response = ollama.chat(
            model="llama3.1",
            messages=[{"role": "user", "content": prompt}]
        )

        code = response["message"]["content"]

        st.code(code, language="python")

        # 一時ファイルに保存
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode("utf-8"))
            tmp_path = tmp.name

        st.write("### 🐳 Docker で実行中…")

        # Docker 実行
        try:
            result = subprocess.run(
                ["docker", "run", "--rm", "-i",
                 "-v", f"{tmp_path}:/app/code.py",
                 "code-runner"],
                capture_output=True,
                text=True,
                timeout=20
            )

            st.write("### 📤 実行結果")
            st.text(result.stdout)

            if result.stderr:
                st.write("### ⚠️ エラー")
                st.text(result.stderr)

        except Exception as e:
            st.error(f"実行中にエラーが発生しました: {e}")

        finally:
            os.remove(tmp_path)
