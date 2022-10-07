def is_disarium(num):
    temp = 0
    word=str(num)
    leng=len(str(num))
    for i in range(leng):
        temp += int(word[i]) ** (i + 1)
    return temp == num
num=int(input())
print(is_disarium(num))