#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/3 21:55
# @Author   : Shawn
# @Version  : Version 1.0
# @Fime     : 20240419 22 exception 01.py
# @Desc     : 

def login():
    password: str = input("Please enter your password: ")
    if len(password) < 6:
        raise ValueError("The password is too short.")

    print(f"Your password is {password}")


def main() -> None:
    """ Main Function """
    login()


if __name__ == "__main__":
    main()
