from .print_news import get_news
from ..utils.cc_rt import clickcommand_rt


def exec_cmd_news():
    name = clickcommand_rt["args"]["name"]
    print(f"Hello, {name}! ")

    flag_news = clickcommand_rt["args"]["flag_news"]
    if flag_news:
        print("Bing News!")
        for item in get_news():
            print(item)
        return

    print("Good Night!")
