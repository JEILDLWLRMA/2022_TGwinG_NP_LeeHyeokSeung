import math

def calcCircleArea(r):
    pi=math.pi
    result = float((r**2)*pi)
    '''[2]'''
    return "{:.2f}".format(result)
def calcLog(a, b):
    if a=='e':
        result=float(math.log(b))
    else:
        result = float(math.log(float(a), b))
    '''[3]'''
    return "{:.2f}".format(result)
def calcSin(x):
    result = float(math.sin(x))
    '''[4]'''
    return "{:.2f}".format(result)
def calcFactorial(x):
    result = int(math.factorial(x))
    '''[5]'''
    return result
def calcCombination(n, r):
    result = int(math.comb(n, r))
    '''[6]'''
    return result

def calculator(order):
    answer = 0
    ls = list(order.split(":"))

    if(ls[0] == "원넓이"):
        answer = calcCircleArea(float(ls[1].strip()))
    elif(ls[0] == "로그"):
        answer = calcLog(list(ls[1].split())[0], float(list(ls[1].split())[1]))
    elif(ls[0] == "사인"):
        answer = calcSin(float(ls[1].strip()))
    elif(ls[0] == "팩토리얼"):
        answer = calcFactorial(float(ls[1].strip()))
    elif(ls[0] == "조합"):
        answer = calcCombination(int(list(ls[1].split())[0]), int(list(ls[1].split())[1]))
    

    return answer