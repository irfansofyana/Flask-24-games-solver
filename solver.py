import itertools
import time

operator = ['+', '-', '*', '/']
undef = -100000000000
eps = 1e-12

def compute(a, op, b):
    if (op == '+'):
        return a+b
    elif (op == '-'):
        return a-b
    elif (op == '*'):
        return a*b;
    else:
        if (abs(b) < eps):
            return undef
        else:
            return a/b;

def preProcess(numbers):
    combList = []
    for i in range(0, 7):
        if (i <= 3):
            if (len(str(numbers[i])) == 0):
                return []
            else:
                combList.append(numbers[i])
        elif (i == 4):
            combList.append('a')
        elif (i == 5):
            combList.append('b')
        else:
            combList.append('c')
    return combList      

def replace_at_index(tup, idx, val):
    lst = list(tup)
    lst[idx] = val
    return tuple(lst)

def calculatePostFix(lis):
    stack = []
    for item in lis:
        if (item != '+' and item != '-' and item != '/' and item != '*'):
            stack.append(item)
        else:
            b1 = 0.0
            b2 = 0.0
            if (not stack):
                return undef
            else:
                b1 = float(stack.pop())
            if (not stack):
                return undef
            else:
                b2 = float(stack.pop())
            if (item == '/' and abs(b1) < eps):
                return undef
            else:
                stack.append(float(compute(b2, item, b1)))
    if (not stack):
        return undef
    else:
        return float(stack.pop())

def convertPostFix(lis):
    stack = []
    for item in lis:
        if (item != '+' and item != '-' and item != '*' and item != '/'):
            stack.append(item)
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append("(" + str(t2) + " " + item + " "+ str(t1) + ")")
    result = stack.pop()
    sz = len(result)
    result = result[1 : sz-1 :]
    return result

def findPossibleOperator(lis, idx):
    if (idx == 7):
        # itung
        result = calculatePostFix(lis)
        if (abs(result-24) < eps):
            candidateSolution = convertPostFix(lis)
            if (solutions.count(candidateSolution) == 0):
                solutions.append(candidateSolution)
        # if (result != undef):
        #     print convertPostFix(lis)
    else:
        if (lis[idx] == 'a' or lis[idx] == 'b' or lis[idx] == 'c'):
            for op in operator:
                lis = replace_at_index(lis, idx, op)
                findPossibleOperator(lis, idx+1)
        else:
            findPossibleOperator(lis, idx+1)
        
    

def findAllSolution(arr):
    if (len(arr) == 0):
        return []
    else:
        x = list(itertools.permutations(arr))
        global solutions
        solutions = []
        for lis in x:
            findPossibleOperator(lis, 0)
        return solutions