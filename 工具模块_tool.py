"""
1. Search搜索数据中对应的位置和值
"""


class Search:
    @staticmethod
    def search_normal(data, target):    # 普通数据搜索并找到对应位置
        index = 0
        for i in data:
            if i == target:
                break
            index += 1
        return print("已找到目标参数,下标为：%d" % index)

    @staticmethod
    def search_json(data, key):   # 字典数据搜索key并找到对应value和位置
        index = 0
        for k, v in data.items():    # 还有种写法只遍历key可以写成data.keys()
            if k == key:
                print(key + ':' + data[key])
                break
            index += 1
        return print("下标为：%s" % index)


if __name__ == '__main__':
    # TestLink().test_insert()
    # print("------------")
    data = {"userName": "testyto",
            "password": "111111",
            "validateCodeKey": "700233df-30c6-4412-92cd-6eebd24af07a",
            "validateCode": "K5UW",
            "platform": "134160222D87"}
    Search().search_json(data=data, key="platform")

