# ーーーforーーー
scores = [34, 78, 90, 87]
for data in scores:
    if data >= 60:
        print("合格")
    else:
        print("不合格")

for num in range(3):
    print("楽しい")
# 繰り返す回数のめどが立つときに使おう

ages = [23, 43, 21, 67, 53, 13, 23, 45, 33, 27, 70, 54, 31, 29]
num = 5
samples = list()
for age in ages:
    if 20 <= age < 30:
        if len(samples) < num:
            samples.append(age)
print(samples)

# breakで強制終了する方法

ages = [23, 43, 21, 67, 53, 13, 23, 45, 33, 27, 70, 54, 31, 29]
num = 5
samples = list()
for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)

# breakで処理をスキップ

ages = [23, 43, 21, "ひみつ", 53, 13, "無回答", 20, 33, 27, 70, 54, 31, 29]
samples = list()
for data in ages:
    if not isinstance(data,int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)
# breakは繰り返しを属座に中断する。
# continueは実行中の周回のみを中断し、繰り返しは継続する。