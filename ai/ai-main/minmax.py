import math

def minimax (curDepth, nodeIndex , maxTurn, values, targetDepth):

    if (curDepth == targetDepth):
        return values[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, False, values, targetDepth),
        minimax(curDepth + 1, nodeIndex * 2 + 1,False, values, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, values, targetDepth),
        minimax(curDepth + 1, nodeIndex * 2 + 1, True, values, targetDepth))
     
values = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(values), 2)
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, values, treeDepth))

