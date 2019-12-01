# белый король,  белая ладья, черный король
position = ['a1','a3','c3']

d = {'a8': [1,1], 'b8': [1,2],'c8': [1,3],'d8': [1,4],'i8': [1,5],'f8': [1,6],'g8': [1,7],'h8': [1,8],
     'a7': [2, 1], 'b7': [2, 2], 'c7': [2, 3], 'd7': [2, 4], 'i7': [2, 5], 'f7': [2, 6], 'g7': [2, 7], 'h7': [2, 8],
     'a6': [3,1], 'b6': [3,2],'c6': [3,3],'d6': [3,4],'i6': [3,5],'f6': [3,6],'g6': [3,7],'h6': [3,8],
     'a5': [4,1], 'b5': [4,2],'c5': [4,3],'d5': [4,4],'i5': [4,5],'f5': [4,6],'g5': [4,7],'h5': [4,8],
     'a4': [5, 1], 'b4': [5, 2], 'c4': [5, 3], 'd4': [5, 4], 'i4': [5, 5], 'f4': [5, 6], 'g4': [5, 7], 'h4': [5, 8],
     'a3': [6, 1], 'b3': [6, 2], 'c3': [6, 3], 'd3': [6, 4], 'i3': [6, 5], 'f3': [6, 6], 'g3': [6, 7], 'h3': [6, 8],
     'a2': [7,1], 'b2': [7,2],'c2': [7,3],'d2': [7,4],'i2': [7,5],'f2': [7,6],'g2': [7,7],'h2': [7,8],
     'a1': [8, 1], 'b1': [8, 2], 'c1': [8, 3], 'd1': [8, 4], 'i1': [8, 5], 'f1': [8, 6], 'g1': [8, 7], 'h1': [8, 8]}

newPosition = [d[position[0]], d[position[1]], d[position[2]]]

def strange(newPosition):
    if newPosition[2][0] == newPosition[0][0] and abs(newPosition[2][1] - newPosition[0][1]) == 1 or newPosition[2][1] == newPosition[0][1] and abs(newPosition[2][0] - newPosition[0][0]) == 1:
        flag = True
    else:
        flag = False
    return flag

def normal(newPosition):
    if newPosition[2][0] != newPosition[0][0] or newPosition[2][1] != newPosition[0][1] or (newPosition[2][0] == newPosition[0][0] and abs(newPosition[2][1] - newPosition[0][1]) != 1) or (newPosition[2][1] == newPosition[0][1] and abs(newPosition[2][0] - newPosition[0][0]) != 1) or newPosition[1][0] == newPosition[2][0] or newPosition[1][1] == newPosition[2][1]:
        flag = True
    else:
        flag = False
    return flag

def shah(newPosition):
    if strange(newPosition) == True and normal(newPosition) == False:
        flag = True
    else:
        flag = False
    return flag

def path(newPosition):
    if newPosition[2][0] !=  newPosition[1][0] and newPosition[2][0] != newPosition[0][0]+1 and newPosition[2][0] != newPosition[0][0]-1 and newPosition[2][1] != newPosition[1][1] and newPosition[2][1] != newPosition[0][1]+1 and newPosition[2][1] != newPosition[0][1]-1:
        flag = True
    else:
        flag = False
    return flag

def mat(newPosition):
    if newPosition[2][0] ==  newPosition[1][0] or newPosition[2][0] == newPosition[0][0]+1 or newPosition[2][0] == newPosition[0][0]-1 or newPosition[2][1] == newPosition[1][1] or newPosition[2][1] == newPosition[0][1]+1 or newPosition[2][1] == newPosition[0][1]-1:
        flag = True
    else:
        flag = False
    return flag

if strange(newPosition) == True:
    print("strange")
elif normal(newPosition) == True:
    print("normal")
elif path(newPosition) == True:
    print("path")
elif mat(newPosition) == True:
    print("mat")
else:
    print("nothing")