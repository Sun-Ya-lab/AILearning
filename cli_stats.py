
number=[1,12,23,34,4,5]
a = number[0]
b = number[0]
sum = 0.0
for i in number:
    if i > a:
        a = i
    if i < b:
        b = i
    sum = sum + i
average = sum / len(number)
print(a)
print(b)
print(sum)
print(average)
