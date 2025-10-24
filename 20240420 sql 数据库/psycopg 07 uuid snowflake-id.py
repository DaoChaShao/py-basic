# pip3 install snowflake-id

from datetime import datetime, timezone
from snowflake import SnowflakeGenerator, Snowflake
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


def ids_generator(volume, center_id=0, sequence=0, epoch=0, timestamp=None):
    """ Generate a unique ID using Snowflake algorithm """
    # Get current timestamp if not provided
    current_timestamp = int(time.time() * 1000)

    # Initialize the generator
    generator = SnowflakeGenerator(
        instance=center_id,
        seq=sequence,
        epoch=epoch,
        timestamp=timestamp if timestamp is not None else current_timestamp,
    )
    for i in range(volume):
        print(f"The {i + 1:0{len(str(volume))}d} ID: {next(generator)}")


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
    print(f"Datetime: {result.datetime}")


def main():
    """ Main function """
    # Build an epoch time from datetime
    epoch_year = 1985
    epoch_month = 10
    epoch_day = 27
    epoch_hour = 3
    epoch_minute = 11
    epoch_second = 3
    epoch = epoch_builder(epoch_year, epoch_month, epoch_day, epoch_hour, epoch_minute, epoch_second)

    # Build a timestamp from datetime
    ts_year = 2024
    ts_month = 10
    ts_day = 27
    ts_hour = 15
    ts_minute = 23
    ts_second = 15
    timestamp = timestamp_builder(ts_year, ts_month, ts_day, ts_hour, ts_minute, ts_second)

    # Generate unique IDs using Snowflake algorithm
    center_id = 1  # 0 < center_id < 1023
    sequence = 0  # 0 <= sequence < 4095
    volume = 10
    # ids_generator(volume, center_id, sequence, epoch, timestamp)
    ids_generator(volume)

    # Analyze the ID using Snowflake algorithm
    snowflake_id = 7265687626261200900
    # snowflake_id = 5171952320933531650
    id_parser(snowflake_id)


if __name__ == "__main__":
    main()
