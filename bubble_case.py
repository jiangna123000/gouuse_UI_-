
class TestBubble:
    def __init__(self, data, except_data):
        self.data = data
        self.except_data = except_data

    def bubble_sort(self):
        size = len(self.data)
        for i in range(size-1):  # 外层循环（0-size）所以需要-1
            for j in range(size-i-1):   # 内层循环是倒序排列
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

    def bubble(self):   # 为了断言期望值与实际值是否相等t
        assert self.except_data == self.bubble_sort()  # 结果为None则表示断言成功，否则会告知失败AssertionError


if __name__ == '__main__':
    B = [1, 3, 5, 4, 2]
    b = [1, 2, 3, 4, 5]
    x = TestBubble(B, b)
    print(x.bubble_sort())







