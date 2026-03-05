initial = "K"
if initial == "K":
    print(initial)

point = 67
if 256 > point >= 80:
    print(point)

bmi = 12
if bmi < 20 or bmi >25:
    print(bmi)

year = 2024
if year % 4 <= 0:
    print(year)

day = 21
if day not in (28, 30, 31):
    print(day)

isError = bool(input("エラーですか？"))
Errorcode = int(input("エラーコードを入力してください"))
if isError == False and Errorcode < 100:
    print("マニュアルを参照してください")

number = int(input("数字を入力してください"))
if number % 2 == 0:
    print("偶数です")
else:
    print("奇数です")

greeting = str(input("こんにちは"))
if greeting == "こんにちは":
    print("今日は何をしますか？")
elif greeting == "おはようございます":
    print("今日も一日がんばりましょう！")
elif greeting == "こんばんは":
    print("一日お疲れ様でした")
else:
    print("こんにちは")

