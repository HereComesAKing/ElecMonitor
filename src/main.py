#!/bin/python
from time import sleep
import urllib
import watchdog

from config import read_config
from toast import toast_info, toast_warn


xauat_openid = ""
loop_sleep_time = 0
waring_fee = 0
enable_info = False


def get_money(id: str) -> str:
    """
    获取用户充值余额。

    通过发送HTTP GET请求到指定URL，解析响应内容以获取用户的充值余额。

    Returns:
        str: 用户的充值余额，如果获取失败则返回空字符串。
    """
    if not id:
        toast_warn("Openid为空，请检查配置文件！")
        return ""

    url = "http://dk.xauat.edu.cn/wxAccount.aspx?openid={}&method=weixin".format(id)

    try:
        with urllib.request.urlopen(url) as response:
            text = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        toast_warn("网络错误，请检查网络连接！错误信息：{}".format(e))
        return ""

    index_start = text.find("充值余额：¥") + len("充值余额：¥")
    index_end = text.find("</h3>", index_start)

    money = text[index_start:index_end]

    return money


def main_loop():
    money = get_money(xauat_openid)

    try:
        money = float(money)
    except ValueError:
        toast_warn("获取电费余额失败！无效的返回值！")
        return

    if money < waring_fee:
        toast_warn("电费即将告罄！余额：{}".format(money))
    elif enable_info:
        toast_info("电费余额：{}".format(money))


if __name__ == "__main__":
    toast_info("程序启动")

    config = read_config()
    if config == None:
        toast_warn("配置文件读取失败！")
        exit(-1)

    try:
        xauat_openid = config["xauat_openid"]
        loop_sleep_time = float(config["loop_sleep_time"])
        waring_fee = float(config["waring_fee"])
        enable_info = bool(config["enable_info"])
    except KeyError:
        toast_warn("配置文件读取错误！")
        exit(-1)

    while True:
        main_loop()
        sleep(loop_sleep_time)
