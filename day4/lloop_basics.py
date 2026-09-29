#1. for+range
print("1到5:")
for i in range(1,6):
    print(i)

#2. fpr 遍历列表
fruits = ["苹果","香蕉","橙子"]
for fruit in fruits:
   print(f"水果:{fruit}")

#3. while 循环
count = 0
while count < 3:
  print(f"count = {count}")
  count +=1

#4.break
print("break示列:")
for i in range(1,10):
  if i == 5:
    break
  print(i)

#5.continue
print("continue示列:")
for i in range(1,6):
  if i == 6:
    continue
  print(i)

#6.循环嵌套
print("嵌套循坏:")
for i in range(1,3):
  for j in range(1,3):
    print(f"i={i}, j={j}")
    