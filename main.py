a=int(input())
b=int(input())
c=int(input())
n=a//2
m=b//2
g=c//2
if a%2==0 and b%2==0 and c%2==0 :
    print(n+m+g)
elif a%2==1 and b%2==0 and c%2==0 :
    print(n+m+g+1)
elif b%2==1 and a%2==0 and c%2==0 :
    print(n + m + g + 1)
elif c%2==1 and b%2==0 and a%2==0 :
    print(n + m + g + 1)
elif a%2!=0 and b%2!=0 and c%2==0 :
    print(n+m+g+2)
elif a % 2 != 0 and c % 2 != 0 and b%2==0:
    print(n+m+g+2)
elif c % 2 != 0 and b % 2 != 0 and a%2==0:
    print(n + m + g + 2)
elif a%2!=0 and b%2!=0 and c%2!=0:
    print(n+m+g+3)
a=int(input())
if a%4==0 and a%100!=0 or a%400==0 :
    print('yes')
else:
    print('no')
n=int(input())
m=int(input())
if m%n==0:
    print(m//n)
else:
    print(m // n+1)