
def partitionLabels(s:str) -> list[int]:
    index_memory = {}
    intervals = []
    i = 0
    for c in s:
        if(index_memory.get(c, None)== None):
            intervals.append([i,i])
            index_memory[c] = len(intervals)-  1
        else:
            idx = index_memory.get(c)
            intervals[idx][1] = i 
        i+=1
    
    if len(intervals) == 1:
        return [len(intervals[0])]

    res_intervals = []
    slow = 0
    fast = slow +1 
    temp = intervals[slow]
    while(fast < len(intervals)):
        b = intervals[fast]
        isLeft = temp[1] < b[0]
        isRight = temp[0] > b[1]
        if (not isLeft and not isRight):
            temp[0] = min(temp[0], b[0])
            temp[1] = max(temp[1],b[1])
        else:
            res_intervals.append(temp)
            temp = b
        fast+=1
    res_intervals.append(temp)
    res = [i[1]-i[0]+1 for i in res_intervals]
    return res 

def partitionLabels2(s: str) -> list[int]:
    dict_ends_idx = {c:i for i,c in enumerate(s)}

    slow, fast = 0, 0
    i = 0
    ans = []
    while(i < len(s)):
        fast = max(fast, dict_ends_idx[s[i]])
        if i == fast:
            ans.append(fast - slow +1)
            slow = fast +1
        i+=1
    return ans

