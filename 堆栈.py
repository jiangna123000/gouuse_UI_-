class Link:
    def __init__(self, data=None):   # 默认一个参数可传可不传
        self.data = data
        self.next = None    # next永远指向是下一个节点

    def append(self, data=None):
        item = self
        while item.next is not None:
            item = item.next
        item.next = Link(data)
        return self

    def travel(self):
        item = self
        while item.next is not None:
            print(item.data)
            item = item.next

    def search(self, data):
        item = self
        index = 0
        while item is not None:
            if item.data == data:
                return index
            else:
                index += 1
                item = item.next
        return -1

    def insert(self, pos, data):
        item = self
        index = 0
        while item is not None:    # 为了找到需要插入的位置，找到了就跳出
            if index == (pos - 1):
                break
            index += 1
            item = item.next

        node = Link(data)
        node.next = item.next   # 插入的数据
        item.next = node


class TestLink:
    def __init__(self):
        self.l = Link(0)
        self.l.append(1)
        self.l.append(2).append(3).append(4).append(5)

    # def test_add(self):
    #     self.l = Link(0)
    #     self.l.append(1)
    #     self.l.append(2).append(3).append(4).append(5)
    #     self.l.travel()

    def test_insert(self):
        self.l.insert(3, 2.5)   # 在原来列表3的下标位置替换成2.5，原来的数据依次向后移一位
        self.l.travel()

    def test_search(self):
        print(self.l.search(3))
        print(self.l.search(0))


if __name__ == '__main__':
    TestLink().test_insert()
    print("----------------")
