#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 17:02
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 01 greenlet 01.py
# @Desc     :

from greenlet import greenlet


def indicator() -> None:
    """ Indicator Function """
    print("1")
    jerry.switch()
    print("2")
    jerry.switch()


def demonstrator() -> None:
    """ Demonstrator Function """
    print("3")
    tom.switch()
    print("4")


def main() -> None:
    """ Main Function """
    global tom, jerry

    tom = greenlet(indicator)
    jerry = greenlet(demonstrator)

    tom.switch()


if __name__ == "__main__":
    main()
