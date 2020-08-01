def candy_1(ratings):
    """
    Q：有N个小朋友站在一排，每个小朋友都有一个评分，你现在要按以下的规则给孩子们分糖果：
    每个小朋友至少要分得一颗糖果，分数高的小朋友要他比旁边得分低的小朋友分得的糖果多。你最少要分发多少颗糖果？
    思路：同一数组，左边遍历一遍，再右边遍历，先从左往右遍历，如果比左边大加一；再从右往左遍历，如果比右边大，判断当前>右加一，说明已经高了不变，反之，当前=右加一
。"""
    candy_list = [1] * len(ratings)
    for i in range(1, len(ratings)):  # 正序比较
        if ratings[i] > ratings[i - 1]:
            candy_list[i] = candy_list[i - 1] + 1
    sum_candy = candy_list[len(ratings) - 1]  # 初始化sum
    for i in range(len(ratings) - 2, -1, -1):  # 逆序比较，注意range 用法 start ，end（不含end），step
        if ratings[i] > ratings[i + 1]:
            candy_list[i] = max(candy_list[i], candy_list[i + 1] + 1)  # 自生和右边加一取最大
        sum_candy = sum_candy + candy_list[i]  # 累加
    return sum_candy


"""point1: 遍历比较，range（1，len）
point2：逆序比较range（len()-2,-1,-1）如果只是遍历，range（len-1，-1，-1）或 for item in res[::-1]
point3：sum 累加使用动态规划，而不是新建数组"""


def candy_2(ratings):
    left = [1 for _ in range(len(ratings))]  # 初始化left 和right都是1
    right = left[:]
    for i in range(1, len(ratings)):  # 左规则
        if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
    count = left[-1]
    for i in range(len(ratings) - 2, -1, -1):  # 右规则
        if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
        count += max(left[i], right[i])  # 取最大值同时满足左右规则
    return count


"""作者：jyd
链接：https://leetcode-cn.com/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/
两个数组，结果取最大，这个方法很好，思路很清晰"""


def canCompleteCircuit(gas, cost):
    if len(gas)==1 and gas[0] >= cost[0]:  # 特殊情况
        return 0
    cir_gas = gas + gas  # 构造圆
    cir_cost = cost + cost
    for i in range(len(gas)):  # 遍历每一个station 作为起点的情况
        if gas[i] > cost[i]:
            cur_gas = gas[i]  # 当前汽油
            k = i  # 建立站点指针
            while (1):
                cur_gas = cur_gas - cir_cost[k] + cir_gas[k + 1]  # 汽油变化
                k = k + 1  # 到下一站点
                if cur_gas < cir_cost[k]or k > i + len(gas) -1 :  # 站点间距作为终止条件，小于下一站用油就失败
                    break
                elif k == i + len(gas) -1 and cur_gas >= cir_cost[k]:  # 当差一站走完循环，且当前油仍大于或等于所需用油，则成功
                    return i
    return -1


def canCompleteCircuit_2(gas, cost):
    """ 作图法，支付宝还花呗的思想，妙
    https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/ """
    if len(gas) == 1 and gas[0] >= cost[0]:  # 特殊情况
        return 0
    cur_use = [0]*len(gas)
    cost = [i * -1 for i in cost]  # 将所有cost取负
    sum_gas = [0]
    for i in range(len(gas)):
        cur_use[i] = gas[i] + cost[i]  # 计算当前加油站可用（攒）油，相当于发工资了，还了以后剩下的帐，可正可负
        sum_gas.append(cur_use[i] + sum_gas[i])   # 累加每次剩下的帐，如果最后>0说明还清了 动态规划式累加！！！
    return sum_gas.index(min(sum_gas)) if sum_gas[-1] >= 0 else -1 # 从最小的值之前都是欠的，后面都在有盈余，那么从最小时刻开始，就是先攒后欠


def longestConsecutive(nums):
    """Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
思路： 排序后计算连续的个数，存在一个list中，最后返回最大值"""
    if nums == []:
        return 0
    nums.sort()
    count_list = [1]  # 初始值为1，当只有一个值时，返回1
    count = 1
    for i in range(len(nums)-1):
        if nums[i + 1] - nums[i] == 1:
            count += 1
        elif nums[i+1] != nums[i]:  # 跳过连续的值
            count_list.append(count)
            count = 1  # 重置count为1
        count_list.append(count)  # 再加一次是由于可能该数组就是连续数组
    return max(count_list)


def groupAnagrams(strs):
    def orderStr(str_orin):
        return ''.join(sorted(list(str_orin)))   # 注意如果sort 与 sorted 区别：,join 从列表变为字符串
    str_dic = {}
    for str_orin in strs:
        str_list= orderStr(str_orin)
        if str_list in str_dic:  # 字典的key不能是列表
            str_dic[str_list].append(str_orin)
        else:
            str_dic[str_list] = [str_orin]  # 将值作为列表存入，不能用list，因为那会分割字母，因使用[str_orin]
    return list(str_dic.values()) # 字典的值,作为list返回

"""point1:注意如果sort 与 sorted 区别
1.sort 是应用在 list 上的方法，属于列表的成员方法，sorted 可以对所有可迭代的对象进行排序操作。
2.list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
3.sort使用方法为ls.sort()，而sorted使用方法为sorted(ls)
point2.字典的key不能是列表
point3.将字符串转换为列表，不能用list，因为那会分割字母，因使用[str_orin]
point4.字典的值返回方法list(str_dic.values())"""

def firstMissingPositive_1(nums):
    """思路——独创： 动态扩充自然数数组，当前自然数不在就返回"""
    if nums == []:
        return 1
    nature = [1]
    for i in range(len(nums)):
        if nature[-1] in nums:  # 如果使用动态规划即（append）不能用nature【i】否则会超索引，而用nature【-1】控制当前自然数
            nature.append(nature[-1] + 1)
    return nature[-1]
def firstMissingPositive_2(nums):
    """原地哈希表法, 确定开头，或者说有一个标准表"""
    if nums == []:
        return 1
    for i in range(len(nums)):
        while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:  # 如果不在对应位置，交换当前数和它应该在的位置，
            # 每个数都应该在自己数值-1 的索引下,注意溢出情况  使用while是由于交换回来的数也要交换到它自己的位置
            temp = nums[i]  # 交换
            nums[i] = nums[nums[i]-1]
            nums[temp-1] = temp
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1
    return len(nums) + 1 # 全部排好，说明不缺，返回长度

"""point1:交换回来的数仍然要交换，才能规整好，因此使用while
point2:用哈希索引时，注意数值应在（0，len（nums））之间"""


def thirdMax(nums):
    """思路-独创：先用set去重，再移除两次最大后剩下的最大"""
    num_set = set(nums)
    if len(num_set) <= 2:
        return max(nums)
    for i in range(2):
        num_set.remove(max(num_set))
    return max(num_set)








