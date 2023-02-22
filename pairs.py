# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    B = []
    flag = True
    for x in range (len(A)):
        if x == 0:
            B.append(A[x])
        else:
            for u in range (len(B)):
                # check if within B
                if A[x]==B[u]:
                    # set B[u] to 0
                    B[u] = 0
                    flag = False
            if flag == True: # append
                B.append(A[x])
        flag = True
            
    
    for y in range (len(B)):
        if B[y]!= 0:
            return B[y]
        

    pass