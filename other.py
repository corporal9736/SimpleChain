"""
本文件中包含了其他文件中需要用到的一些工具性的组件
包括：
InsufficientError类：当余额不足时会抛出该异常
"""
class InsufficientError(Exception):
    def __init__(self):
        self.__name__ = "InsufficientError"
    def __str__(self):
        return "the balance of the wallet is not enough"