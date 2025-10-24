#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/31 21:50
# @Author   : Shawn
# @Version  : Version 1.0
# @Fime     : 20240419 20 request 01.py
# @Desc     :

from dataclasses import dataclass, field
from fake_useragent import UserAgent
from requests import get


@dataclass
class WebRequester(object):
    """
    This function is used to send web requests
    Dependencies:
    - pip3 install requests
    - pip3 install fake_useragent
    """
    _URL: str
    _FAKE_USERAGENT: UserAgent = field(default=UserAgent(), repr=False)
    _code: int = field(init=False, repr=False)
    _description: str = field(init=False, repr=False)

    def __post_init__(self):
        headers = {
            "User-Agent": self._FAKE_USERAGENT.random,
            "content-type": "text/html; charset=utf-8",
        }

        self._response = get(url=self._URL, headers=headers, stream=True)
        self._code = self._response.status_code
        self._description = self._status(self._code)

    @staticmethod
    def _status(code: int) -> str:
        status_dict = {
            200: "OK / 客户端请求成功",
            301: "Moved Permanently / 资源被永久移动到新地址",
            400: "Bad Request / 客户端不能被服务器所理解",
            401: "Unauthorized / 请求未经授权",
            403: "Forbidden / 服务器拒绝提供服务",
            404: "Not Found / 请求资源不存在",
            500: "Internal Server / 服务器发生不可预期的错误",
            503: "Service Unavailable / 服务器当前不能处理客户端的请求",
        }
        return status_dict.get(code, "其他未知问题")

    def __str__(self):
        return f"Response Code: {self._code} - {self._description}"


def main() -> None:
    """ Main Function """
    URL: str = "https://www.examword.com/elementary-word/kindergarten"

    web_requester = WebRequester(URL)
    print(web_requester)


if __name__ == "__main__":
    main()
