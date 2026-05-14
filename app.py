import streamlit as st
import ollama
import subprocess
import tempfile
import os

# コードクリーンアップ関数を追加
def clean_code(raw: str) -> str:
    text = raw.replace("```python", "").replace("```", "")
    text = text.replace("[/CODE]", "").replace("[/EXPLANATION]", "")
    return text.strip()


# コードと説明文を分離する関数
def split_response(raw: str):
    code = ""
    explanation = ""

    # タグが両方ある場合のみ処理
    if "[CODE]" in raw and "[EXPLANATION]" in raw:
        # [CODE] と [EXPLANATION] の間をコードとして抽出
        code = raw.split("[CODE]")[1].split("[EXPLANATION]")[0].strip()
        # [EXPLANATION] 以降を説明文として抽出
        explanation = raw.split("[EXPLANATION]")[1].strip()

    return code, explanation


# タイトル（日本語）
st.title("コード生成アシスタント")

# 言語選択プルダウン
language = st.selectbox(
    "出力するプログラミング言語を選択してください",
    ["Python", "C++", "Rust", "JavaScript", "Go", "Java"],
    index=0
)

# 問題文入力欄
problem_text = st.text_area("問題文を入力してください", height=200)

if st.button("コード生成 & 実行"):
    if not problem_text.strip():
        st.error("問題文を入力してください。")
    else:
        st.write("### 🔧 コード生成中…")

        # LLM に渡すプロンプト
        prompt = f"""
あなたは競技プログラミングのプロです。
次の問題を解く {language} のコードを生成してください。

【厳守する出力形式】
以下のテンプレートを **そのまま** 使用して出力してください。
タグ名は絶対に変更しないでください。

[CODE]
<ここにコードのみを書く。コードブロック（```）は禁止>

[EXPLANATION]
<ここに説明文を書く。最後に必ず計算量（Big-O）を書く>

【禁止事項】
- [CODE] の前に説明文を書かない
- [EXPLANATION] の前にコードを書かない
- タグ名（[CODE], [EXPLANATION]）を変更しない
- **閉じタグ（[/CODE], [/EXPLANATION]）を絶対に出力しない**
- コードブロック（```）を絶対に使わない

問題:
{problem_text}

"""

        response = ollama.chat(
            model="llama3.1",
            messages=[{"role": "user", "content": prompt}]
        )

        code_raw = response["message"]["content"]
        response_text = response["message"]["content"]

        # ① コードと説明文を分離
        code_raw, explanation = split_response(response_text)

        # ② コード部分だけクリーンアップ
        code = clean_code(code_raw)

        # ③ UI に表示
        st.subheader("🧩 生成されたコード")
        st.code(code, language=language.lower())

        st.subheader("📘 説明（計算量つき）")
        st.write(explanation)



        # Python 以外はまだ実行できないので注意
        if language != "Python":
            st.warning(f"{language} の実行環境はまだ未対応です。コード生成のみ行いました。")
            st.stop()

        # Python のみ Docker 実行
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode("utf-8"))
            tmp_path = tmp.name

        st.write("### 🐳 Docker で実行中…")

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
