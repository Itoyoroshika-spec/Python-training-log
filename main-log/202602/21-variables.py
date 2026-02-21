# ーーーアンパック代入ーーー

name, age = "佐藤", 23
# 同時に代入できる
# 来年の年齢を出力するプログラム ↓
name, age = "佐藤", 23
print(name, "さんは今年", age, "歳です。")
age = age + 1
print("来年は", age, "歳です。")

# ーーー複合代入演算子ーーー

age = 24
age += 1

# これで age = age + 1 と同じらしい
score = 1500
score *= 2
print(score)

# ーーーインプットーーー

age = input("年齢を入力してください")
print(age)

# 挨拶プログラム ↓

name = input("imput your name : ")
print("Welcome to Python", name)
'''
 NameError: name 'cathy' is not defined
 なんか挨拶プログラムでエラーが出た
 原因：対話モードで2行実行してた 
 対処：一行ずつ実行する

 >>> print("Welcome to Python", name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print("Welcome to Python", name)
    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'tuple' object is not callable
原因：printに間違えて変数を代入してしまい、関数として呼び出そうとした
対処：exit() → python をターミナルで入力し、再実行
'''

# ーーー総復習　割り勘プログラムーーー

number = input("人数を入力してください：")
sum = input("合計金額を入力してください：")
number = int(number)
sum = int(sum)
payment = sum / number
print("1人あたりの支払額は", payment, "円です")

# 答えに小数点がついちゃう！
# / はfloat（小数）を返す　→　//を使う（切り捨て）
# sumは組み込み関数だからtotalがよい
# number = int(input("人数を入力してください："))　→　整数型でインプットできる


# 修正版


number = int(input("人数を入力してください："))
total = int(input("合計金額を入力してください："))
payment = total // number
print("1人あたりの支払額は", payment, "円です")

# 動いた！