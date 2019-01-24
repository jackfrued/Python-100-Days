"""
设计模式 - 策略模式(指定的策略不同执行的算法不同)
"""
from hashlib import md5
from hashlib import sha1
from hashlib import sha256
from hashlib import sha512


class StreamHasher():
    """哈希摘要生成器"""

    def __init__(self, algorithm='md5', size=1024):
        self.size = size
        alg = algorithm.lower()
        if alg == 'md5':
            self.hasher = md5()
        elif alg == 'sha1':
            self.hasher = sha1()
        elif alg == 'sha256':
            self.hasher = sha256()
        elif alg == 'sha512':
            self.hasher = sha512()
        else:
            raise ValueError('不支持指定的摘要算法')

    # 魔法方法: 让对象可以像函数一样被调用
    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的哈希摘要字符串"""
        for data in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()


def main():
    """主函数"""
    hasher = StreamHasher('sha1', 4096)
    with open('Python语言规范.pdf', 'rb') as stream:
        # print(hasher.to_digest(stream))
        print(hasher(stream))


if __name__ == '__main__':
    main()
