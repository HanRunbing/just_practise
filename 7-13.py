
def twoSum(self, nums, target):
    """
    return the index of the two numbers in the nums,
    and the target is the sum of those two numbers
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[j]==target-nums[i]):
                return i,j
    return "No sum solution"


"""
Q:在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
/* 思路
* 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
* 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
* 要查找数字比左下角数字小时，上移
*/"""

def Find(target, array):
    row = len(array)-1
    cols = len(array[0])#turn lengh to index
    col = 0#row=rows and col=0 located at  lower left
    while(col < cols and row>=0):
        if (target < array[row][col]):
            row = row - 1
        elif(target > array[row][col]):
            col = col + 1
        else:
            return True
    return False

   #problem1: 将行数或者列数作为index查询列表时，应-1
   #problem2: 先行后列，rows = len(array) cols = len(array[0])
   #problem3: 边界情况，包不包含0， 这道题中col不包含，因为col是lenth没有-1，而row-1 本身就是index最小情况是0
   #sum： 思路上，如果是有序2维列表，可以观察规律，从一角开始查询

"""
Q:把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
解法一：按照旋转规则，查询到后面的元素均小于前面元素，且递增，因此返回第一个小于list[0]的元素即可 """

def minNumberInRotateArray_1(rotateArray):
    if len(rotateArray) == 0:
        return 0#when the size of array is 0 return 0
    for item in rotateArray:
        if item < rotateArray[0]:#find the first item which smaller than array[0]
            return item
    return rotateArray[0]#Maybe the first item is minimum

"""解法2： 二分查找，一个left指针指向第一个元素，一个right指针指向最后一个元素，若中间元素大于array[0]，则属于前增序列
left指向mid，若mid小于array[0]，right指向mid，二分下去，知道两个指针相邻"""

def minNumberInRotateArray_2(rotateArray):
    left = 0
    right = int(len(rotateArray)-1)
    if len(rotateArray) == 0:
        return 0#when the size of array is 0 return 0
    while (rotateArray[left] >= rotateArray[right]):
        mid = int(left + (right - left) / 2)
        if right - left == 1:
            break
        elif(rotateArray[mid] > rotateArray[left]):#situation 1
            left = mid
        elif(rotateArray[mid] < rotateArray[left]):#situation 2
            right = mid
    return rotateArray[right]

print(minNumberInRotateArray_2([3,4,5,1,2]))



