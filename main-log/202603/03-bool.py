# ーーーbool型ーーー
score = int(input("試験の点数を入力"))
print(score >= 60)

# ーーー論理演算子ーーー
'''
and or not などを論理演算子と呼ぶ
'''
if not (score < 60, score >100):
    print("不合格")
else:
    print("合格")

# 以下のような条件式も可能だが基本はtrue/falseで評価
score = 0
if score:  # score != 0 と同義
    print("処理")
else:
    print("処理")