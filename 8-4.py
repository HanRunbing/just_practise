#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    if not pHead:
        return None
    pre = None  # 注意空链表的创建直接用None即可
    while(pHead):
        pnext = pHead.next  # 首先将当前节点的后面存在next中
        pHead.next = pre  # 当前指针的下一个结点指向pre，更新pre
        pre = pHead  # 移动pre指向当前结点，便于循环
        pHead = pnext  # 向后移动
    return pre  #pre中及是反转链表
def ReverseList_recursion(pHead):
    if (pHead == None or pHead.next == None):
        return pHead
    new_head = ReverseList_recursion(pHead.next)
    pHead.next.next = pHead
    pHead.next = None
    return new_head

def Merge(pHead1, pHead2):
    if pHead1 == None:
        return pHead2  # phead1 遍历完，将phead2直接挂上去
    if pHead2 == None:
        return pHead1
    if (pHead1.val <= pHead2.val):  # 如果phead1小，返回phead1,遍历下一个phead1.next
        pHead1.next = Merge(pHead1.next,pHead2)
        return pHead1
    else:
        pHead2.next = Merge(pHead1,pHead2.next)
        return pHead2

def Merge_2(pHead1, pHead2):
    if pHead1 == None:
        return pHead2  # phead1 遍历完，将phead2直接挂上去
    if pHead2 == None:
        return pHead1
    if (pHead1.val <= pHead2.val):  # 用一个新的链表来装结果
        pHead1.next = Merge(pHead1.next,pHead2)
        res = pHead1  # 指向小的值
    else:
        pHead2.next = Merge(pHead1,pHead2.next)
        res = pHead2  # 指向小的值

    return res

def Merge_3(pHead1, pHead2):  # 非递归方法
    temp = ListNode(-1)  # 初始化temp指针
    res_pHead = temp
    while(pHead1 and pHead2):
        if (pHead1.val <= pHead2.val):
            temp.next = pHead1
            pHead1 = pHead1.next
        else:
            temp.next = pHead2
            pHead2 = pHead2.next
        temp = temp.next  # 指针自身向下
    if pHead1 == None:  # 当其中一个链表遍历完
        temp.next = pHead2
    if pHead2 == None:
        temp.next = pHead1
    return res_pHead.next

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
def Clone(pHead):
    if pHead == None:
        return None
    cur = pHead
    # 1、复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
    while(cur):
        # 不断接入新的结点
        node = RandomListNode(cur.label)  # 将当前值付给node
        node.next = cur.next
        cur.next = node  # node接到cur.next的后面
        cur = cur.next  # 转到下一个
    # 2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
    cur = pHead
    while(cur):
        copy = cur.next  # 由于隔一个是一个复制
        if (cur.random):
            copy.random = cur.random.next  # A1.random = A.random.next;
        cur = cur.next

    # 3、拆分链表，将链表拆分为原链表和复制后的链表
    clone_head = pHead
    cur = pHead
    while(cur.next):
        # 分开相邻列表
        temp = cur.next
        cur.next = temp.next   # cur 让绕过temp
        cur = temp  # 下次temp改变时，temp被删除
    return clone_head

def FindFirstCommonNode( pHead1, pHead2):
    """长的先走，直到和短的相同长度，然后两个一起走，直至相等。"""
    if not pHead1 or not pHead2:
        return None
    p1 = pHead1
    p2 = pHead2
    len1 = 0
    len2 = 0
    while(p1):  # 计算p1的长度
        p1 = p1.next
        len1 += 1
    while(p2):  # 计算p2的长度
        p2 = p2.next
        len2 += 1
    p1 = pHead1  # 由于没有改变pHead1, pHead2，因此pHead1, pHead2没有变
    p2 = pHead2
    if len1 >= len2:
        len3 = len1 - len2
        while(len3):
            p1 = p1.next
            len3 -= 1
    else:
        len3 = len2 - len1
        while(len3):
            p2 = p2.next
            len3 -= 1
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next
    return p1




l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
p = ListNode(2)
p.next = ListNode(3)
p.next.next = ListNode(5)





