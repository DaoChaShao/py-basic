
from abc import ABCMeta,abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, currency):
        print("这是接口")


class AliPay(Payment):
    def pay(self, currency):
        print(f"支付宝已到账：{currency} 元")


class WeChatPay(Payment):
    def pay(self, currency):
        print(f"微信已到账：{currency} 元")


if __name__ == '__main__':
    AliPay().pay("100")
    WeChatPay().pay("200")
