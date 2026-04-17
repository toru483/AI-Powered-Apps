# run.py
# このファイルは AI が生成したコードを実行するためのテンプレートです。

import sys

# 実行したいコードをファイルから読み込む
with open("code.py", "r", encoding="utf-8") as f:
    code = f.read()

# 実行
try:
    exec(code)
except Exception as e:
    print("ERROR:", e, file=sys.stderr)
