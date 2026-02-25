# ーーータプルーーー
scores = (70, 80, 55)
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
'''
タプルは()で定義する。
添え字が適用されるが、要素の追加や削除はできない。
'''

# －－－要素数が1つのリストとディクショナリーーー
members = ["マツダ"]
scores = {"network:76"}

# ーーー要素数が1つのタプルーーー
members = ("マツダ")
print(type(members))
'''
members = 'マツダ' と解釈され、文字列になる。
'''
members = ("マツダ", )
print(type(members))
'''
これで要素数1のタプルになる
'''

# －－－セットーーー
'''
重複不可
添え字やキーの概念がない
順序がない
apendではなくadd関数で追加する
'''
scores = {70, 80, 90, 55}
scores.add(66)
print(scores)
