import subprocess
import ollama

def generate_testcases(task: str, num_cases: int = 10):
    prompt = f"""
あなたは競技プログラミングのテストケース生成を専門とするエンジニアです。
以下の問題に対して、多様で厳しいテストケースを生成してください。

【要件】
・入力形式に従うこと
・エッジケース（最小値、最大値、空、境界値）を含めること
・ランダムケースも含めること
・出力は「入力のみ」を1行ずつ列挙すること
・説明文は書かないこと

【問題文】
{task}

【生成数】
{num_cases}
"""
    response = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


if __name__ == "__main__":
    task = "整数 N が与えられたとき、1 から N の総和を求めよ。"
    print(generate_testcases(task, 10))