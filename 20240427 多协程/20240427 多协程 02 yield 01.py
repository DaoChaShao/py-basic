#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 17:09
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 02 yield 01.py
# @Desc     : 

def indicator():
    """ Indicator Function """
    yield 1
    yield from demonstrator()
    yield 2


def demonstrator():
    """ Demonstrator Function """
    yield 3
    yield 4


def main() -> None:
    """ Main Function """
    indicator_gen = indicator()

    for item in indicator_gen:
        print(item)


if __name__ == "__main__":
    main()
