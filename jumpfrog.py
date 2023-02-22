# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    ans = int(((Y-X)/D))
    if (Y-X)%D != 0:
        ans +=1
    return ans
    pass