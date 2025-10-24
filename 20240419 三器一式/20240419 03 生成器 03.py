
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
        print(f"姓名包：{names}")
        grades = [random.randint(1, 100) for _ in range(10)]
        print(f"成绩包：{grades}")

        # 生成器表达式
        names_gen = self.gen_transformer(names)
        grades_gen = self.gen_transformer(grades)
        print(f"姓名：{next(names_gen)}, 成绩：{next(grades_gen)}")


def main():
    scraper = Scraper()
    scraper.info_scraper()


if __name__ == "__main__":
    main()