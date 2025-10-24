from snowflake import SnowflakeGenerator, Snowflake
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import time


def epoch_builder(year, month, day, hour, minute, second):
    """ Build an epoch time from datetime """
    epoch = int(datetime(year, month, day, hour, minute, second).timestamp() * 1000)
    # print(f"Epoch time stamp: {epoch}")
    return epoch


def timestamp_builder(year, month, day, hour, minute, second):
    """ Build a timestamp from datetime """
    timestamp = int(datetime(year, month, day, hour, minute, second).timestamp() * 1000)
    # print(f"Timestamp time stamp: {timestamp}")
    return timestamp


class CusSnowflakeID(object):
    """ Custom Snowflake class """

    def __init__(self, center_id=0, sequence=0, epoch=0, timestamp=None):
        self.center_id = center_id
        self.sequence = sequence
        self.epoch = epoch
        self.timestamp = timestamp

        # Get current timestamp if not provided
        current_timestamp = int(time.time() * 1000)

        self.generator = SnowflakeGenerator(
            instance=self.center_id,
            seq=self.sequence,
            epoch=self.epoch,
            timestamp=self.timestamp if self.timestamp is not None else current_timestamp,
        )

    def __iter__(self):
        return self

    def __next__(self):
        # Generate a unique ID using Snowflake algorithm
        snowflake_id = next(self.generator)
        # Update sequence number
        self.sequence = (self.sequence + 1) % 4095
        return snowflake_id


def id_parser(snowflake_id):
    """ Analyze the ID using Snowflake algorithm """
    result = Snowflake.parse(snowflake_id)
    utc_time = datetime.fromtimestamp((result.timestamp / 1000), timezone.utc)
    location = "Pacific/Auckland"
    local_time = utc_time.astimezone(ZoneInfo(location))
    print(f"The ID: {snowflake_id}")
    print(f"Timestamp: {result.timestamp}")
    print(f"Date and time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Instance ID: {result.instance}")
    print(f"Seq: {result.seq}")


def main():
    """ Main function """
    # Build an epoch time from datetime

    # Build a timestamp from datetime

    # Generate unique IDs using Snowflake algorithm
    center_id = 1  # 0 < center_id < 1023
    sequence = 0  # 0 <= sequence < 4095
    snowflake_generator = CusSnowflakeID()

    volume = 10
    for i in range(volume):
        print(f"The {i + 1:0{len(str(volume))}d} ID: {next(snowflake_generator)}")


if __name__ == "__main__":
    main()
