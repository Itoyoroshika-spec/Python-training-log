# ーーーディクショナリーーー
scores = {"math":60, "physics":70, "english":78}
print(scores)
'''
ディクショナリにはキーという見出しを付けることができる
数値や文字列など様々な型を利用できる
'''

# ーーーディクショナリの参照ーーー
scores = {"math":60, "physics":70, "english":78}
print(scores["math"])
'''
ディクショナリの定義は{}なのに、参照は[]なのややこしい
'''

# ーーーディクショナリの要素の追加と変更、削除ーーー
scores = {"network":50, "security":87, "database":68}
scores["programming"] = 69 # 追加
scores["security"] = 65 # 変更
del scores["database"] # 削除
print(scores)
'''
間違えてscores["programming":69]と書いてエラーになった
'''

# ーーーディクショナリの合計ーーー
scores = {"network":50, "security":87, "database":68}
total = sum(scores.values())
print(total)

# sumが使えないので、ディクショナリ.valueでキーを除いた値だけの集まりにする。

