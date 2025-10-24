#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 16:02
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 13 lock 04 with lock.py
# @Desc     :

from threading import Thread, Lock

NUMBER: int = 0


def addition(amount: int, lock: Lock, thread_name: str) -> None:
    """ Addition Function """
    for _ in range(amount):
        with lock:
            global NUMBER
            NUMBER += 1

    print(f"{thread_name} : {NUMBER}")


def adder(amount: int, lock: Lock, thread_name: str) -> None:
    """ Adder Function """
    for _ in range(amount):
        with lock:
            global NUMBER
            NUMBER += 1
    print(f"{thread_name} : {NUMBER}")


def main() -> None:
    """ Main Function """

    AMOUNT_DATA: int = 1_000

    lock: Lock = Lock()

    tom = Thread(target=addition, args=(AMOUNT_DATA, lock, "Tom"))
    jerry = Thread(target=adder, args=(AMOUNT_DATA, lock, "Jerry"))

    tom.start()
    jerry.start()


if __name__ == "__main__":
    main()
