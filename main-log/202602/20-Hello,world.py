print("Hello, world")
# 初めてのプログラミングに成功！
print("Hello, world")
print("The first log")

# Chapter 1 演算子のコード

print(1+2)
print(10-8)
print(10//2)
# 演算子の前後は半角スペースがある方がいいみたい
print(34 % 3)

# Chapter 2 文字列と演算子

print('1' + '1')
print('オラ' * 10)
print('Pythonは' + 'とっても' * 2 + '楽しい！')
# 拡張子には優先順位がある
# 前からひとつづつ評価される

#　Chapter 3 エスケープシーケンス

print("初めまして\nプログラミングの世界へ\nようこそ！")
print('''今日はいい天気だ
外でご飯でも
食べたいな''')
#複数行コメントはヒアドキュメントの構文らしい

# Chapter 4 変数

name = "山田"
age = "32"
print(name)
print(age)
# =の前後も半角スペースがあるといいみたい
# 年齢は数値がいい""不要

print("半径3cmの円の直径は、")
dia = 3 * 2
print("円周は")
print(dia * 3.14)
# 円周率も変数に　pi = 3.14

# global = 1
# print(global)
# SyntaxError: invalid syntax
# 変数名に使えないものがあるらしい（予約語）