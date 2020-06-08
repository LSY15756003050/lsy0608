class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None

class DLinkList(object):
    """双向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def seach(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self,pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.pre = cur
            node.next = cur.next
            cur.next.pre = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self.__head
            if cur.next == item:
                if cur.next == None:
                   self.__head = None
                else:
                    cur.next.pre = None
                    self.__head = cur.next
                    return

            while cur != None:
                if cur.item ==item:
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                    break
                cur = cur.next











