"""
混入 - Mix-in
限制字典只有在指定的key不存在时才能设置键值对
原则上能够不使用多重继承的地方都不要用多重继承
MRO - Method Resolution Order - 方法解析顺序
Python2 - 深度优先搜索
Python3 - 类似于广度优先搜索 - C3算法
类.__mro__ / 类.mro()
"""


class SetOnceMappingMixin():
    """混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f'键{str(key)}已经存在')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


def main():
    """主函数"""
    dict1 = SetOnceDict()
    try:
        dict1['username'] = 'jackfrued'
        dict1['username'] = 'hellokitty'
        dict1['username'] = 'wangdachui'
    except KeyError as error:
        print('Error:', error)
    print(dict1)


if __name__ == '__main__':
    main()
