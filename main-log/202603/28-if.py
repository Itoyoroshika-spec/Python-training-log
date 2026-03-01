# ーーーif文ーーー
name = input("あなたの名前を教えてください")
print(f"{name}さん、こんにちは。")
food = input(f"{name}さんの好きな食べ物を教えてください。")
if food == "カレー": # コロンを忘れないようにする
    print(f"私も{food}が超大好きですよ！！")
else:
    print(f"そうなんですね、私はカレーが好きです。")
'''
それぞれifブロック、elseブロックという
インデントによりブロック画指定される。
'''

name = input("あなたの名前を入力してください")
japanese = int(input("国語の点数を入力してください"))
math = int(input("数学の点数を入力してください"))
english = int(input("英語の点数を入力してください"))
science = int(input("理科の点数を入力してください"))
social = int(input("社会の点数を入力してください"))
avg = (japanese + math + english + science + social) / 5
if avg >= 80:
    print(f"平均は{avg}点です！よくできました！")
else:
    print("もう少しがんばりましょう")

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－

name = input("あなたの名前を入力してください")
score = []
score.append(int(input("国語の点数を入力してください")))
score.append(int(input("数学の点数を入力してください")))
score.append(int(input("英語の点数を入力してください")))
score.append(int(input("理科の点数を入力してください")))
score.append(int(input("社会の点数を入力してください")))
avg = sum(score) / len(score)
if avg >= 80:
    print(f"平均は{avg}点です！よくできました！")
else:
    print("もう少しがんばりましょう")