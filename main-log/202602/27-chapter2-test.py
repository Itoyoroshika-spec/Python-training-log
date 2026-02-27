# ーーー練習問題ーーー
scores = []
scores.append (int(input("国語の点数を入力してください")))
scores.append (int(input("数学の点数を入力してください")))
scores.append (int(input("社会の点数を入力してください")))
scores.append (int(input("理科の点数を入力してください")))
scores.append (int(input("英語の点数を入力してください")))
total = sum(scores)
avg = total / len(scores)
print(avg)




member_hobbies = {
    "member1" : {"料理", "映画", "読書", "旅行", "音楽"},
    "member2" : {"料理", "映画", "睡眠", "旅行", "ゲーム"},
}
input("心の準備ができたらEnterを押してください")
common_hobbies = member_hobbies["member1"] & member_hobbies["member2"]
print(common_hobbies)