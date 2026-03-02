# ーーー演算子ーーー
'''
== 等しい
!= 等しくない
> 不等号
< 不等号
>= 等しいものも含む
<= 等しいものも含む
'''

# ーーーin演算子ーーー
name = input("あなたの名前を入力してください")
print(f'{name} さんこんにちは')
food = input(f'{name}さん、あなたの好きな食べ物を教えてください')
if 'カレー' in food:
    print("私もカレーが好きです！")
else:
    print("いいですね！")

# ーーーコンテナの併用ーーー
scores = [48, 90, 100, 67]
if 100 in scores:
    print("100点の科目があったんですね！すごい！")
else:
    print("次は100点を目指そう")

# ーーーディクショナリのキーをチェックするーーー
scores = {'network':60, 'security':89}
key = input('追加するキーを選んでください')
if key in scores:
    print(f"すでに{key}は登録されています")
else:
    data = int(input("得点を入力してください"))
    scores[key] = data
print(scores)