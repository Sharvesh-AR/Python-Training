a=input()
b=input()

x=len(a)-3
y=len(b)-3

p=a[x:]
q=b[y:]

print(p == q)