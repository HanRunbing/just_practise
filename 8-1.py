def minIncrementForUnique(A):
    """思路-独创：排序后，小于或者相等，加一"""
    if not A:
        return 0
    A.sort()
    count = 0
    for i in range(len(A) - 1):
        while A[i + 1] <= A[i]:
            A[i + 1] += 1
            count += 1
    return count





def minIncrementForUnique_2(A):
    """好难好难，哈希线性探测+路径优化，画图
    https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/ji-shu-onxian-xing-tan-ce-fa-onpai-xu-onlogn-yi-ya/"""
    pos = [-1] * 80000  # 位置记录初始值设为-1.表示为空

    def finders(a):
        b = pos[a]  # b 为当前这个数字的位置记录
        if (b == -1):  # 当b为空
            pos[a] = a  # 放入对应位置值
            return a
        else:
            b = finders(b + 1)  # 否则，当前位置有数了，移到下一个位置，此时新的finders函数框架中 a = b+1，
            # 直到a不断增加。当找到空位，a被返回，作为b pos【a】 = b，就是新位置的a，
            # 由于else return b，因此之前递归的框架中 b都被更新，但a不变并 将pose之前位置都改变，
            pos[a] = b  #
            return b

    move = 0
    for a in A:  # 遍历A中所有数字，找到对应的映射（位置），其位置和数字本身的差值即为move
        b = finders(a)  # 找位置的函数
        move += b - a
    return move

def surfaceArea(grid):
    if len(grid) == 1:
        return grid[0][0] * 4 + 2  # 特殊情况
    rows = len(grid)
    area = 0
    side = 0
    for i in range(rows):  # 先计算横排重叠情况
        for j in range(rows-1):
            if grid[i][j]:  # 当有一个以上的格子时
                area = area + grid[i][j] * 4 + 2
            side = side + min(grid[i][j + 1], grid[i][j]) * 2  # 重叠的部分是相邻两个各自中小的哪一个，并*2
            if j == rows - 2 and grid[i][j+1]:  # 最后一个各自也要加上
                area += grid[i][j+1] * 4 + 2
    for i in range(rows):  # 再计算列重叠情况
        for j in range(rows-1):
            side = side + min(grid[j + 1][i], grid[j][i]) * 2
    area = area - side
    return area

def Find(target, array):
    """review 1"""
    rows = len(array)
    cols = len(array[0])
    def whether(row,col):
        flag = False
        if row < 0 or col > cols-1:
            return flag
        if array[row][col] == target:
            flag = True
            return flag
        if target < array[row][col]:
            return whether(row - 1, col)
        else:
            return whether(row, col + 1)
    return whether(rows - 1,0)

def printMatrix( matrix):
    result = []
    result = result + matrix[0]
    matrix.pop(0)
    def rotate(matrix):
        rotate_mat=[]
        for i in range(len(matrix[0])-1,-1,-1):
            rotate_mat_col = []
            for j in range(len(matrix)):
                rotate_mat_col.append(matrix[j][i])
            rotate_mat.append(rotate_mat_col)
        return rotate_mat
    while(matrix):
        result = result + rotate(matrix)[0]
        matrix = rotate(matrix)
        matrix.pop(0)
    return result

def FindGreatestSumOfSubArray( array):
    if not array:
        return 0
    res = array[0]
    cur_sum = array[0]
    for i in range(1,len(array)):
        cur_sum = cur_sum + array[i]
        cur_sum = max(cur_sum,array[i])
        res = max(res,cur_sum)
    return res






