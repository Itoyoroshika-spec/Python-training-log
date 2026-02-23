# ーーーリストの作成ーーー
members = ["工藤", "松埼", "浅木"]
print(members)

# ーーーリストから参照ーーー

print(members[0])
'''
添え字は0からはじまる。
'''

# ーーーリスト要素の計算ーーー
scores = [70, 80, 97]
total = sum(scores)
print(f"合計は{total}点です。")
'''
sumでリスト内の要素を合計できる
'''

# ーーーlen関数を利用して平均を求めるーーー
scores = [79, 86, 98]
total= sum(scores)
avg = total // len(scores)
print(f"平均点は{avg}点です。")
'''
lenで要素数が分かる
'''

# ーーーリスト要素の追加・削除ーーー
scores = [78, 89, 94]
scores.append(65)
scores.append(79)
print(scores)
'''
リスト名.appendで要素を追加できる。
末尾に追加される
'''
scores.remove(65)
print(scores)
'''
リスト名.removeで要素を削除できる。
'''

# ーーー要素の変更ーーー
scores = [76, 89, 65]
scores[2] = 43
print(scores)
'''
添え字で指定することで内容を変更できる。
'''

# ーーーsliceによる範囲の指定ーーー
scores = [45, 75, 87, 63, 98, 56]
print(scores[0:2])
print(scores[2:]) # 添え字が2以上
print(scores[:3]) # 添え字が3未満
scores[0:2] = 54, 67
print(scores)
scores.pop(3) # popを使うと、変数として利用しつつ削除できる
math = scores.pop(0) # 変数として利用する場合
print(scores)
print(math)
'''
print(0:2)このように書いてしまった
正しくはprint(scores[0:2])
sliceの指定では [X:Y] のとき、X以上Y未満となる(添え字が)
remove では slice は使えなかった
'''

# ーーー負の数による指定ーーー
scores = [54, 76, 78, 98]
print(scores[-1])
'''
末尾が-1で指定できる。末尾から二番目は-2になる。
'''