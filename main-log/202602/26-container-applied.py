# ーーーコンテナの相互変換ーーー

scores = {"network":60, "security":76, "database":90}
members = ["松崎", "佐藤", "工藤"]
print(tuple(members)) # リストmemberをtupleに変換
print(list(scores)) # scoresのキーをリストに変換
print(set(scores.values())) # scoresの値をセットに変換して表示
'''
list()のようにすると空のコンテナを作成できる
ディクショナリへの変換は、キーのリストと値のリストが必要
dict(zip(keylist, numberlist))
'''

# ーーーコンテナのネストーーー

matsuda_scores = {"network":56, "database":86, "security":68}
asagi_scores = {"network":84, "database":98, "security":45}
members_scores = {
    "松田": matsuda_scores, 
    "浅木": asagi_scores, 
}
print(members_scores)
print(members_scores["松田"])

# ーーーディクショナリにセットをネストーー

members_hobbies = {
    "松田": {"SNS", "料理", "自転車"}, 
    "浅木": {"食べ歩き", "ゲーム", "数学"}
}
print(members_hobbies)
print(members_hobbies["松田"]) # 松田の趣味だけ表示できる
'''
ディクショナリのキーにはコンテナは使わない
'''

# ーーー二次元リストーーー

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b] # aを0番目、bを1番目と定義する2次元リストc
print(c)
print(c[1][2]) # リストcの1番目(リストb)の2番目を参照

# ーーー集合演算ーーー

# 1.共通項を求める
members_hobbies = {
    "松田": {"SNS", "料理", "自転車"}, 
    "浅木": {"食べ歩き", "SNS", "数学"}
}
common_hobbies = members_hobbies["松田"] & members_hobbies["浅木"]
print(common_hobbies)

'''
集合演算子
print(A | B) # 和集合
print(A & B) # 積集合
print(A - B) # 差集合
print(A ^ B) # 対象差
'''


