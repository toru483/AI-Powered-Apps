def generate_problem():
    prompt = """
あなたは競技プログラミングの問題作成者です。
アルゴリズム力を問う問題を1つ作成してください。

【要件】
・入力形式と出力形式を明確に書く
・制約（Constraints）を書く
・例（Sample Input/Output）を書く
・難易度は初級〜中級
・文章は簡潔に
"""
    response = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]