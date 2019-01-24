"""
程序设计的范式(理念)：
1. 指令式程序设计 - 汇编语言
2. 面向过程程序设计 - 把一组指令封装成一个过程，需要执行这组指令时调用这个过程即可 - C
3. 面向对象程序设计 - 将数据和操作数据的函数从逻辑上组织成了对象 - C++ / Java
4. 函数式程序设计 - 函数是一等对象(一等公民) - Haskell

面向对象程序设计步骤:
1. 定义类 - 抽象过程 - 数据抽象(静态特征-属性)/行为抽象(动态特征-方法)
2. 创建对象 - 构造器 - 初始化(__init__)
3. 给对象发消息 - 对象引用.对象方法(参数)

面向对象的三大支柱 - 封装 / 继承 / 多态

类与类(对象与对象)之间的关系:
1. is-a: 继承
2. has-a: 关联 / 聚合 / 合成
3. use-a: 依赖

面向对象的设计原则/SOLID原则:
1. 单一职责原则 - 类的设计要高内聚
2. 开闭原则 - 接受扩展不接受修改 - 抽象是关键/用继承封装可变性
3. 依赖倒转原则 - 面向抽象编程
4. 里氏替换原则 - 任何时候都可以使用子类型对象替换父类型对象
5. 接口隔离原则
6. 合成聚合复用原则 - 优先考虑用强关联而不是继承去复用代码
7. 最少知识原则(迪米特法则) - 不要跟陌生人讲话

GoF设计模式 - 23种场景(Python中有16中已经被弱化)
- 单例、工厂、原型、适配器、观察者、策略
"""
from enum import Enum
from enum import unique

import random

# 经验: 符号常量优于字面常量
# 枚举类型是定义符号常量的最佳选择
# 如果一个变量的值只有有限多个选项那么最好使用枚举
@unique
class Suite(Enum):
    """花色"""

    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3


class Card():
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌的花色和点数"""
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = [
            '', 'A', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', 'J', 'Q', 'K'
        ]
        return f'{suites[self.suite.value]} {faces[self.face]}'

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        temp = self.cards[self.index]
        self.index += 1
        return temp

    @property
    def has_more(self):
        """是否有牌可以发"""
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def drop_one(self, index):
        """打出一张牌"""
        return self.cards.remove(index)

    def get_many(self, more_cards):
        """摸多张牌"""
        self.cards += more_cards

    def drop_cards(self):
        """扔掉所有牌"""
        self.cards.clear()

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort(key=lambda x: (x.suite.value, x.face))


def main():
    """主函数"""
    poker = Poker()
    poker.shuffle()
    players = [
        Player("东邪"), Player("西毒"),
        Player("南帝"), Player("北丐")
    ]
    for _ in range(3):
        for player in players:
            if poker.has_more:
                player.get_one(poker.deal())
    for player in players:
        player.arrange()
        print(player.name)
        print(player.cards)


if __name__ == '__main__':
    main()
