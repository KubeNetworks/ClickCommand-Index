from helloworld.utils.dep import check_and_install

check_and_install("requests")


from helloworld.cmds.exec_cmd_news import exec_cmd_news
from helloworld.utils.cc_rt import clickcommand_rt


if clickcommand_rt["cmd"] == "main":
    print("Hello, world!")
elif clickcommand_rt["cmd"] == "hello":
    print(f"Hello, {clickcommand_rt['args']['name']}!")
elif clickcommand_rt["cmd"] == "news":
    exec_cmd_news()
