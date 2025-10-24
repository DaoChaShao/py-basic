#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 19:35
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 06 uvloop 01.py
# @Desc     : 

import asyncio
import uvloop

# Set the event loop policy to uvloop to speed up the asyncio
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def main() -> None:
    """ Main Function """
    pass


if __name__ == "__main__":
    main()
