# Enter your code here. Read input from STDIN. Print output to STDOUT

mydict = {}
l = []

n = int(input())
for i in range(n):
    name, phone = map(str, input().split())
    mydict[name] = phone
l = []
while True:
    try:
        l.append(input())
    except EOFError:
        break

for i in range(len(l)):
    val = ""
    val = mydict.get(l[i])
    if l[i] in mydict:
        print(str(l[i])+"="+str(val))
    else:
        print("Not found")
    
