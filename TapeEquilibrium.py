# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # if N is odd
    N = len(A)
    sum1 = A[0]
    sum2 = 0
    
    # start from P = 1 
    #P =2 => +=2*(i-1)
    
    
    for i in range (1,N):
        sum2 = sum2+A[i] 

    Val = sum1-sum2
    # left side has 0, right side has 1 -> N-1
    # add 1 -> N-1
    minVal = abs(Val)
    for i in range(1,N-1):
        Val += 2*A[i]
        if abs(Val)< minVal:
            minVal = abs(Val)
    return minVal

    pass