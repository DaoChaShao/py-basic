import faker
import random


class Scraper(object):
    @staticmethod
    def gen_transformer(nor_list: list) -> iter:
        """ 生成器表达式 """
        for item in nor_list:
            yield item

    def info_scraper(self):
        names = [faker.Faker().last_name() for _ in range(10)]
        print(f"姓名包 类型：{type(names)}, 内容：{names}")
        grades = [random.randint(1, 100) for _ in range(10)]
        print(f"成绩包 类型：{type(grades)}, 内容：{grades}")

        print(f"姓名：{next(iter(names))}, 成绩：{next(iter(grades))}")


def main():
    scraper = Scraper()
    scraper.info_scraper()


if __name__ == "__main__":
    main()
