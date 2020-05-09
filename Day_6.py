# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
list1 = []
for _ in range(n):
    ele = input()
    list1.append(ele)
temp_str = " "

for i in range(n):
    str1 = ""
    str2 = ""
    temp_str = str(list1[i])
    for j in range(len(temp_str)):
        if (j%2 == 0):
            str1 += temp_str[j]
        else:
            str2 += temp_str[j]
    print(str1,end = "")
    print(" ", end = "")
    print(str2, end = "")
    print(end = "\n")
                
