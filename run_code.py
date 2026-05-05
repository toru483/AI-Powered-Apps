import subprocess
import ollama

from testcase_generator import generate_testcases


# 1. AI にコードを生成させる
def generate_code(task: str, language: str = "python") -> str:
    prompt = f"""
あなたは競技プログラミングとアルゴリズム設計に精通した熟練エンジニアです。
以下の要件に従ってコードを生成してください。

【目的】
競技プログラミングの問題に対して、正確で効率的なアルゴリズムを実装する。

【制約】
・指定された言語で実行可能なコードのみを書くこと
・Markdown のコードブロック（```）は使わないこと
・説明文はコード内のコメントとして記述すること
・外部ライブラリは使用しないこと（標準ライブラリのみ）
・入力形式と出力形式を厳密に守ること
・不要な print やデバッグ出力は禁止

【アルゴリズム要件】
・最適なデータ構造を選択すること
・時間計算量と空間計算量を最小化すること
・計算量（Big-O）を必ずコメントで明記すること
・ボトルネックとなる処理をコメントで説明すること
・エッジケース（0, 空入力, 最大値, 最小値）を考慮すること

【出力形式】
1. 完成したコードのみ
2. コード内にコメントで計算量とアルゴリズムの説明を記述

【タスク】
{task}
"""
    response = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# 2. 生成したコードを code.py に保存
def save_code(code: str):
    with open("code.py", "w", encoding="utf-8") as f:
        f.write(code)


# 3. Docker でコードを実行
def run_in_docker(input_data=""):
    cmd = [
        "docker", "run", "--rm",
        "-i",
        "-v", "/home/pc_user/workspace/AI-Powered-apps:/app",
        "code-runner"
    ]

    result = subprocess.run(
        cmd,
        input=input_data,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return result.stdout, result.stderr


# 4. 修正依頼プロンプト
def fix_code(original_code: str, error_log: str, language: str = "python") -> str:
    prompt = f"""
あなたは熟練したソフトウェアエンジニアです。
以下のコードは実行時にエラーが発生しました。
エラー内容を参考に、コードを修正してください。

【元のコード】
{original_code}

【エラーログ】
{error_log}

修正後のコードのみを出力してください。
"""
    response = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# 5. コード抽出（コードブロックがある場合のみ）
def extract_code(raw: str) -> str:
    if "```" in raw:
        parts = raw.split("```")
        if len(parts) >= 2:
            return parts[1].replace("python", "").strip()
    return raw.strip()


# メイン処理
if __name__ == "__main__":

    # ① 問題文
    task = """
整数 N が与えられたとき、
1 から N の総和を求めよ。
"""

    # ② コーディングAIでコード生成
    code_raw = generate_code(task)
    code = extract_code(code_raw)
    print("=== 生成されたコード ===")
    print(code)
    save_code(code)

    # ③ テストケース生成
    testcases = generate_testcases(task, num_cases=10)
    print("=== 生成されたテストケース ===")
    print(testcases)

    # ④ テスト実行
    for case in testcases.splitlines():
        stdout, stderr = run_in_docker(case + "\n")
        print(f"入力: {case} → 出力: {stdout.strip()} エラー: {stderr.strip()}")

    # ⑤ 修正ループ（例として1つの入力でチェック）
    stdout, stderr = run_in_docker("10\n")
    attempt = 1
    while stderr:
        print(f"\n=== エラー発生（{attempt}回目の修正） ===")
        print(stderr)

        code = fix_code(code, stderr)
        save_code(code)

        print("\n=== 修正後のコード ===")
        print(code)

        stdout, stderr = run_in_docker("10\n")
        attempt += 1

    print("\n=== 最終実行結果 ===")
    print(stdout)