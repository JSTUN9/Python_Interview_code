# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    
    # Implement your solution here
    # at least one uppercase
    # no digits
    N = len(S)
    digit = []

    maxSegmentLengths = -1
    # list of all segments
    segments = []
    
    flag = False
    data = list(range(N))
    # longest substring within S as valid password
    # given a0Ba => valid substrings are Ba & B
    #split string up at digits
    # get index of all digits
    for x in range (N):
        if S[x].isnumeric():
            digit.append(x)

    # get list of segments between digits
    
    for x in range(len(digit)):
        start = digit[x-1]+1 if x>0 else 0
        end = digit[x]
        segmented = data[start:end]
        segments.append(segmented)
    segments.append(data[digit[x]+1:])


    while(segments):
        # iterate through all segments

        # segments.pop(0) => gives segments
        temp = segments.pop(0)
        for x in temp:
            if S[x].isupper():
                flag = True
                break
                # if segment has upper case
        if flag ==True:
            # check if 
            if maxSegmentLengths < len(temp):
                maxSegmentLengths = len(temp)

        flag = False
    
    return maxSegmentLengths
    pass

