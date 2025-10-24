
import time


class Timer(object):
    def __enter__(self):
        self.time_start = time.perf_counter()  # 开始时间
        self.time_end = 0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time_end = time.perf_counter()  # 结束时间

    def elapsed(self):
        return self.time_end - self.time_start


with Timer() as timer:
    print("Start")
    time.sleep(2)
    print("End")
    print(f"Elapsed time: {timer.elapsed()} seconds")

