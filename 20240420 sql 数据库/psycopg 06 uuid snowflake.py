from datetime import datetime

import time


class Snowflake(object):
    def __init__(self, customized_time=None, center_id=0, machine_id=0):
        # 时间戳的偏移量，以 customized_time 为基础
        # 如果无指定 customized_time，使用当前时间作为基准时间，并转换为时间戳
        if customized_time is None:
            customized_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 如果有指定 customized_time，使用指定时间作为基准时间，并转换为时间戳
        self.epoch = int(
            time.mktime(
                time.strptime(
                    customized_time, "%Y-%m-%d %H:%M:%S"
                )
            ) * 1000
        )

        # 数据中心 ID 和机器 ID
        self.center_id = center_id
        self.machine_id = machine_id

        # Bit lengths for each part of the ID
        """
        1 bit 符号位
        + 41 bits 时间戳
        + 5 bits 数据中心 ID
        + 5 bits 机器 ID
        + 12 bits 序列号
        """
        self.timestamp_bits = 41
        self.center_id_bits = 5
        self.machine_id_bits = 5
        self.sequence_bits = 12

        # Maximum values for data center ID, machine ID, and sequence
        self.max_center_id = (1 << self.center_id_bits) - 1
        self.max_machine_id = (1 << self.machine_id_bits) - 1
        self.max_sequence = (1 << self.sequence_bits) - 1

        # Left shift amounts for each part of the ID
        self.center_id_shift = self.sequence_bits + self.machine_id_bits
        self.timestamp_shift = self.center_id_shift + self.center_id_bits
        self.machine_id_shift = self.sequence_bits

        # Initialize parameters
        self.sequence = 0
        self.last_timestamp = -1

        # Check if data center and machine IDs are within bounds
        if not (0 <= center_id <= self.max_center_id):
            raise ValueError(f"Data center ID must be between 0 and {self.max_center_id}")
        if not (0 <= machine_id <= self.max_machine_id):
            raise ValueError(f"Machine ID must be between 0 and {self.max_machine_id}")

        # set the id of the cener and machine
        self.data_center_id = center_id
        self.machine_id = machine_id

    @staticmethod
    def _current_timestamp():
        """ Get the current timestamp in milliseconds """
        return int(time.time() * 1000)

    def _wait_for_next_millisecond(self, last_timestamp):
        """ Wait until the next millisecond """
        timestamp = self._current_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._current_timestamp()
        return timestamp

    def id_generator(self):
        """ Generate a unique ID using the Snowflake algorithm """
        timestamp = self._current_timestamp()

        if timestamp < self.last_timestamp:
            raise Exception("Clock moved backwards. Refusing to generate ID.")

        if timestamp == self.last_timestamp:
            # Same millisecond: increase sequence
            self.sequence = (self.sequence + 1) & self.max_sequence
            if self.sequence == 0:
                # Sequence overflow, wait for next millisecond
                timestamp = self._wait_for_next_millisecond(self.last_timestamp)
        else:
            # New millisecond: reset sequence
            self.sequence = 0

        # record the last timestamp
        self.last_timestamp = timestamp

        # Generate ID by shifting and combining parts
        snowflake_id = (
                ((timestamp - self.epoch) << self.timestamp_shift) |
                (self.data_center_id << self.center_id_shift) |
                (self.machine_id << self.machine_id_shift) |
                self.sequence
        )
        print(
            f"Timestamp: {timestamp}, "
            f"Center ID: {self.data_center_id},"
            f"Machine ID: {self.machine_id},"
            f"Sequence: {self.sequence}"
        )
        return snowflake_id


def main():
    """ Main function """
    customized_date = "2021-01-01"
    customized_time = "00:00:00"
    customized_stamp = customized_date + " " + customized_time
    center_id = 1
    machine_id = 2
    snowflake = Snowflake(customized_stamp, center_id, machine_id)

    volume = 10
    for i in range(volume):
        print(f"The {i + 1:{len(str(volume))}} ID: {snowflake.id_generator()}")


if __name__ == "__main__":
    main()
