# problem_classifier.py
# 自然言語の問題文から「問題タイプ」を推定する分類器
# 今後キーワード追加やLLM分類に拡張できる構造にしている

def classify_problem(text: str) -> str:
    """
    自然言語の問題文から問題タイプを推定する。
    最初はキーワードベースで分類し、後でLLM分類に拡張可能。
    """

    # 前処理：全角→半角、ひらがな→カタカナなどの正規化も後で追加可能
    t = text.strip()

    # --- 累積和系 ---
    cumulative_keywords = ["合計", "足し算", "累積", "総和", "和を求め", "sum", "加算"]
    if any(k in t for k in cumulative_keywords):
        return "累積和"

    # --- 条件分岐系 ---
    condition_keywords = ["場合", "条件", "if", "else", "判定", "分類"]
    if any(k in t for k in condition_keywords):
        return "条件分岐"

    # --- 配列処理系 ---
    array_keywords = ["配列", "リスト", "array", "list", "要素", "並び替え", "ソート"]
    if any(k in t for k in array_keywords):
        return "配列処理"

    # --- 文字列処理系 ---
    string_keywords = ["文字列", "string", "部分文字列", "回文", "置換", "検索"]
    if any(k in t for k in string_keywords):
        return "文字列処理"

    # --- 数学系 ---
    math_keywords = ["素数", "gcd", "最大公約数", "最小公倍数", "数学", "数論"]
    if any(k in t for k in math_keywords):
        return "数学"

    # --- 探索系 ---
    search_keywords = ["探索", "dfs", "bfs", "幅優先", "深さ優先", "最短経路"]
    if any(k in t for k in search_keywords):
        return "探索"

    # --- fallback（分類できない場合） ---
    return "一般"
