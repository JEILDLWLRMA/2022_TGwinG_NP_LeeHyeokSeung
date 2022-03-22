# 문제 1번
from audioop import reverse


def sum(a,b):
    sum=a+b
    return sum

# 문제 2번
def sub(a,b):
    sub=a-b
    return sub

# 문제 3번
def mul(a,b):
    mul=a*b
    return mul

# 문제 4번
def div(a,b):
    div=a-b
    return div

# 문제 5번
def distance(x1,y1,x2,y2):
    distance=(((x1-x2)**2)+((y1-y2)**2))**1/2
    return distance

# 문제 6번
def short():
    lylic = "life is short art is long"
    return lylic[8:13]

# 문제 7번
def myReverse(string):
    myReverse=string[::-1]
    return myReverse

# 문제 8번
def letMeIntroduceMyself():
    name=input("이름을 입력하시오:")
    hobby=input("취미를 입력하시오:")
    college=input("재학 중인 대학을 입력하시오:")
    birthday=input("생일을 입력하시오(예시: 981128):")
    birthday_month=birthday[2:4]
    birthday_day=birthday[4:6]
    introduce="제 이름은 %s입니다. 제 취미는 %s이구요, 저는 %s을 다니고 있습니다. 제 생일은 %s월 %s일 입니다." % (name, hobby, college, birthday_month, birthday_day)
    return introduce

# 문제 9번
def calcAI():
    firstnum=int(input("첫 번째 숫자를 입력하시오:"))
    secondnum=int(input("두 번째 숫자를 입력하시오:"))
    calcAI="두 수의 합은 %d입니다."%(firstnum+secondnum)
    return calcAI
