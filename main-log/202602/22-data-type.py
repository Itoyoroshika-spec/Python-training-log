# ーーーデータ型ーーー

x = "砂糖"
y = 23
z = 123.4
print(x)
print(y)
print(z)

# ーーーデータ型を調べるーーー

print(type(x))
print(type(y))
print(type(z))
'''
データ型
int = 整数
float = 小数
str = 文字列
bool = 真偽値（true, false)
'''

# ーーーデータ型の変換ーーー

y = float(y)
z = int(z)

# ーーー文字列に数字をformat関数で埋め込むーーー

print("{}を{}g入れた後に、小麦粉を{}g加えてください"
      .format(x, y, z))
'''
.formatのカッコは{}ではなく()
'''

# ーーー割り勘プログラムの改良ーーー

price = int(input("合計金額を入力してください："))
number = int(input("人数を入力してください："))
payment = int(price / number)
print("一人当たりの支払金額は{}円です".format(payment))
'''
回答を整数にしたいときは//を使う（整数の割り算でも）
'''

# ーーーf-stringでの書き方ーーー

name = "bob"
age = 23
tall = 186.7
print(f"彼の名前は{name}です。年齢は{age}歳で、身長は{tall}cmです。")
'''
分かりやすい！
'''
hp, maxhp = 20, 100
print(f"{hp} / {maxhp}")
print(f"{hp = } / {maxhp = }")
print(f"{hp / maxhp = }")
'''
f-stringで末尾に = を付ければ、式の表示もできる（ないと答えの表示）
printなしでも使える。
計算してそのまま埋め込める。
'''

# ーーー練習問題ーーー
'''
BMIを計算するプログラム
'''
tall = float(input("あなたの身長を入力してください："))
weight = float(input("あなたの体重を入力してください"))
tall *= 0.01
bmi = weight / tall /tall
print(bmi)
'''
tall = float(input("あなたの身長を入力してください：")) / 100
にすると、計算も同時にできる。

tall, weight = float(input("あなたの身長を入力してください：")) / 100 \
               float(input("あなたの体重を入力してください："))
print(f'{weight / tall / tall = }です')
アンパック代入,f-stringを使う方法もある
'''