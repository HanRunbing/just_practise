def PrintMinNumber(numbers):
    """输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。"""
    if len(numbers) == 0:  # special condition
        return ""
    else:
        numbers.sort()
        num = [str(i) for i in numbers]  # turn every items in numbers to str type
        res = [num[0]]  # initialize res
        for i in range(len(num) - 1):
            a = [res[i], num[i + 1]]  # res[i] is the memory
            b = [num[i + 1], res[i]]
            if int(''.join(a)) < int(''.join(b)):  # join the adjacent items and turn to int type
                res.append(int(''.join(a)))
                res = [str(i) for i in res]  # turn to str type for the next compare
            else:
                res.append(int(''.join(b)))
                res = [str(i) for i in res]
        return res[-1]


""" 思路： 把数组排序，排序后从第一个值开始，假如有元素a和元素b，
若ab > ba 则 a应该处于b之后；若ab < ba 则a应该处于b之前；若ab = ba 则 a = b；解释说明：比如 “3” 和 
"31"比较谁先谁后， “331” > “313”，‘31’应该处于‘3’之前。
 pro1: 组合数字，方法先转成字符连接起来，再转成数据类型
 https://blog.csdn.net/chouzhou9701/article/details/102179257 
 join method https://www.runoob.com/python/att-string-join.html
 pro2：动态规划，将res记录下来，每次迭代更新"""


def IsContinuous_1(numbers):
    """题目：判断列表内元素是否有序，其中0可以代替任何数
    思路：制造标准列表用于判断，标准列表为已给列表第一个非0元素起的递增列表
    剔除原始列表的0 并记录0的个数，再和标准列表进行判断
    判断分两种情况：1、元素不够时，补充0  2、元素不同时插入0
    如果补充或者插入的0个数大于所给序列0个数则False,反之True"""
    if numbers == []:
        return False
    num = [i for i in numbers if i != 0]
    zero_num = len(numbers) - len(num)
    num.sort()
    stand = []
    item = num[0]
    for i in range(len(numbers)):
        stand.append(item)
        item += 1
    for i in range(len(stand)):
        if i == len(num):
            num.append(0)
            zero_num -= 1
        elif num[i] != stand[i] or i == len(num):
            num.insert(i, 0)
            zero_num -= 1
    if zero_num < 0:
        return False
    return True


"""pro1:没有考虑元素少的情况，"""


def IsContinuous_2(numbers):
    """思路：除0以外没有数字重复；除0外最大值和最小值之间误差小于5"""
    if numbers == []:
        return False
    num = [i for i in numbers if i != 0]  # remove all the items of 0
    num.sort()  # since the result of set method is sorted, the num list need to be sorted too
    set_numbers = list(set(num))  # since the result of set method a disc, it should be turn into list
    if set_numbers != num:
        return False
    elif max(num) - min(num) >= 5:
        return False
    return True


"""pro1: set method https://www.runoob.com/python3/python3-set.html
1、输出有序，2、输出为字典形式"""


def duplicate(numbers, duplication):
    """题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，
    但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
    例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
    思路：排序后和剔除元素后的列表对比，第一个不相同元素输出"""
    numbers.sort()
    set_numbers = list(set(numbers))
    print(numbers, set_numbers)
    for i in range(len(set_numbers)):
        if set_numbers[i] != numbers[i]:
            duplication[0] = numbers[i]
            print(duplicate[0])
            return True
    if len(numbers) > len(set_numbers):  # 当第一个重复元素再末尾的情况
        duplication[0] = set_numbers[-1]
        return True
    return False


"""这个答案不对，该代码只能输出最小的重复元素"""


def duplicate_hash(numbers, duplication):
    """哈希法：链接：https://www.nowcoder.com/questionTerminal/623a5ac0ea5b4e5f95552655361ae0a8
1、由于所有元素值是有范围的，因此可以用一个长度为n的数组，下标表示序列中的每一个值，下标对应的值表示该下标出现的次数，即建立key-value对应关系，key-索引（值）： value-次数。
2、只需扫描一次原序列，就统计出所有元素出现的次数；
3、再扫描一次哈希数组，找到一个出现次数大于1的值即可。"""
    hash_list = [0] * len(numbers)  # initialize hash_list
    for i in range(len(numbers)):
        hash_list[numbers[i]] += 1  # the index is the value,and the times of the value increase
    for i in range(len(hash_list)):  # find the first item in hash_list is not equal to 1, means the first duplication
        if hash_list[i] > 1:
            duplication[0] = i
            return True
    return False


"""哈希原理"""


def duplicate_3(numbers, duplication):
    """3.题目里写了数组里数字的范围保证在0 ~ n-1 之间，所以可以利用现有数组设置标志，
    当一个数字被访问过后，可以设置对应位上的数 + n，之后再遇到相同的数时，
    会发现对应位上的数已经大于等于n了，那么直接返回这个数即可。
    通过索引改变值，如果数字重复出现，就会找到之前的索引，那么值一定被改变了
    思路上图！！"""
    for i in range(len(numbers)):
        index = numbers[i] % len(numbers)  # %len(numbers)是因为该值numbers【i】可能已经修改，经过该处理后还原该值
        if numbers[index] >= len(numbers):
            duplication[0] = index
            return True
        numbers[index] += len(numbers)  #
    return False


def multiply(A):
    """给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
     其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
     （注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
思路：按上图把每行被1分割的两部分乘积都计算出来，
这样可以从首尾分别用累乘算出两个列表，然后两个列表首尾相乘就是B的元素"""
    head = [1]
    tail = [1]
    for i in range(len(A)-1):  # 已设定初始值，后面是不断添加，因此迭代次数-1
        head.append(A[i]*head[i])  # 由于是不断添加，head【i】即为前一个从前累加元素！！！
        tail.append(A[-i-1]*tail[i])  # 逆着从后面乘过来 同样tail【i】即为前一个从后累加元素
    return [head[j]*tail[-j-1] for j in range(len(A))]

"""有图，思路有点像二分法 https://www.nowcoder.com/questionTerminal/94a4d381a68b47b7a8bed86f2975db46"""





