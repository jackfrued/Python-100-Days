# 练习 1：宠物工厂
# 实现一个 PetFactory，根据用户输入创建不同宠物对象。

# from abc import ABCMeta, abstractmethod


# class Pet(metaclass=ABCMeta):
#     """创建宠物抽象类"""
#     def __init__(self,name):
#         self.name = name
#     @abstractmethod
#     def make_sound(self):
#         pass


# class Dog(Pet):
#     """Dog类"""
#     def make_sound(self):
#         return '汪汪汪'

# class Cat(Pet):
#     """Cat类"""
#     def make_sound(self):
#         return '喵喵喵'

# class Duck(Pet):
#     """Duck类"""
#     def make_sound(self):
#         return '嘎嘎嘎'



# class PetFactory:
#     @staticmethod
#     def create(pet_type, *args, **kwargs):
#         all_pet_type = {'dog':Dog,
#                         'cat':Cat,
#                         'duck':Duck}
#         cls = all_pet_type.get(pet_type.lower())
#         return cls(*args, **kwargs) if cls else None


# def main():
#     pets = [PetFactory.create('dog','Tom'),
#             PetFactory.create('cat','jerry'),
#             PetFactory.create('duck','guagua'),]

#     for pet in pets:
#         print(f'{pet.name}会{pet.make_sound()}.')

# if __name__ == '__main__':
#     main()




# 练习 2：支付方式工厂
# 实现一个支付系统，根据支付方式创建不同支付对象。


from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """创建支付抽象类"""

    @abstractmethod
    def pay(slef, amount):
        pass

class Alipay(Payment):
    """支付宝支付"""
    def pay(self, amount):
        return f'支付宝支付：{amount}元。'

class WeChatPay(Payment):
    """微信支付"""
    def pay(self, amount):
        return f'微信支付：{amount}元。'

class BankCardPay(Payment):
    """银联支付"""
    def pay(self, amount):
        return f'银联支付：{amount}元。'

class PaymentFactory:
    @staticmethod
    def create(payment_type):
        all_payment_type = {'A':Alipay,'W':WeChatPay,'B':BankCardPay}
        cls = all_payment_type.get(payment_type.upper())
        return cls() if cls else None

def main():
    payments = [
        (PaymentFactory.create('A'),10000),
        (PaymentFactory.create('B'),20000),
        (PaymentFactory.create('W'),30000),
    ]
    for payment,amount in payments:
        print(f'{payment.pay(amount)}')

if __name__ == '__main__':
    main()




    