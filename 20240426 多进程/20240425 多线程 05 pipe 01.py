#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 00:32
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 多线程 05 pipe 01.py
# @Desc     :

from faker import Faker
from multiprocessing import Pipe, Process
from random import randint, uniform
from time import sleep


def producer(faker: Faker, sender: Pipe, amount: int, delays: list[float]) -> None:
    for i in range(amount):
        phone_number = faker.phone_number()
        sender.send(phone_number)
        print(f"Producing {i + 1:>02d}: {phone_number}.")
        sleep(delays[i])


def consumer(reader, amount, delays):
    for i in range(amount):
        phone_number = reader.recv()
        print(f"{phone_number} is consumed.")
        sleep(delays[i])


def main() -> None:
    """ Main Function """
    AMOUNT_DATA = 10
    SECOND_MIN = 0
    SECOND_MAX = 1
    DELAYS = [uniform(SECOND_MIN, SECOND_MAX) for _ in range(AMOUNT_DATA)]

    data_faker = Faker()

    pi_send, pi_recv = Pipe()
    sender = Process(target=producer, args=(data_faker, pi_send, AMOUNT_DATA, DELAYS))
    reader = Process(target=consumer, args=(pi_recv, AMOUNT_DATA, DELAYS))

    sender.start()
    reader.start()

    sender.join()
    reader.join()

    sender.terminate()
    reader.terminate()


if __name__ == "__main__":
    main()
