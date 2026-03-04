# ーーーelif構文ーーー
score = int(input("点数を入力してください"))
if score < 0 or score > 100:
    print("点数が異常です")
elif score > 60:
    print("合格")
else:
    print("不合格")

# ーーーif文のネストーーー
print("あなたにおすすめのカメラをお勧めします")
budget = int(input("予算を教えてください"))
print("次の質問にはyかnで答えてください")
movie = (input("動画性能は必要ですか？"))
photo = (input("写真性能は必要ですか？"))
if budget < 0 or movie not in ("y","n") or photo not in ("y","n"):
    print("いずれかの入力値が異常です")
if budget < 300000:
    print("Nikon 5II がおすすめです")
elif budget > 300000 and movie == "y" and photo !="y":
    print("Nikon ZR がおすすめです")
elif movie == "y" and photo == "y":
    print("Nikon Z6III がおすすめです")
    if budget > 500000:
        need = (input("さらに高性能な機種がいいですか？"))
        if need == "y":
            print("Nikon Z7 はいかがですか？")
        else:
            print("了解いたしました")
else:
    print("あなたの要望に合致するカメラが見つかりませんでした")