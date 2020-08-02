class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    # 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead_1(listNode):
    """使用逆序"""
    if not listNode:
        return []
    res = []
    while listNode:
        res.append(listNode.val)  # 顺序存入列表
        listNode = listNode.next
    return res[::-1]  # 返回时不是链表，而是list

def printListFromTailToHead_2(listNode):
    """使用栈"""
    if not listNode:
        return []
    res = []
    temp = []  # 栈
    while(listNode):
        temp.append(listNode.val)  #进栈
        listNode = listNode.next
    while(temp):
        res.append(temp.pop())  # 出栈
    return res

def FindKthToTail( head, k):
    """双指针法"""
    # write code here
    if head==None or k<=0:
        return None
    #设置两个指针，p2指针先走（k-1）步，然后再一起走，当p2为最后一个时，p1就为倒数第k个 数
    p2=head
    p1=head
    #p2先走，走k-1步，如果k大于链表长度则返回 空，否则的话继续走
    while k>1:
        if p2.next!=None:
            p2=p2.next
            k-=1
        else:
            return None
#两个指针一起 走，一直到p2为最后一个,p1即为所求
    while p2.next!=None:
        p1=p1.next
        p2=p2.next
    return p1

