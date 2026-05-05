# 計算量: O(N) (時間), O(1) (空間)
def sum_of_numbers(n):
    # ボトルネックとなる処理: 1からnまでの合計計算
    # エッジケース: n=0, n=-1, n=最大値を考慮する
    if n <= 0:
        return "Invalid input"
    
    sum = 0
    for i in range(1, n+1):
        # 計算量: O(1)
        sum += i
    
    return sum

# テストケース
n = int(input("Nを入力してください: "))
print(sum_of_numbers(n))