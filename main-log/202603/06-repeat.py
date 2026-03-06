# ーーーwhileーーー
count = 0
while count < 0:
    count += 1
    print(f"ひつじが{count} 匹")
print("おやすみなさい")

is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f"ひつじが{count}匹")
    key = input("もう眠りそうですか？(y/n)>>")
    if key == "y":
        is_awake = False
print("おやすみなさい")

# ーーーリストの作成ーーー
count = 0
student_num = int(input("学生の数を入力>>"))
score_list = list()
while count < student_num:
    count += 1
    score = int(input(f"{count}人目の試験の得点を入力"))
    score_list.append(score)
print(score_list)
total = sum(score_list)
avg = total / len(score_list)
print(f"平均点は{avg}点です")
# リストの参照
count = 0
while count < len(score_list):
    if score_list[count] >= 60: # countを添え字として使用
        print("合格")
    else:
        print("不合格")
    count += 1