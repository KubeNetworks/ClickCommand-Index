import requests
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flagNews = False
        self.news = []

    def handle_starttag(self, tag, attrs):
        if tag == "section":
            attr_names = [item[0] for item in attrs]
            if "class" in attr_names:
                index = attr_names.index("class")
                val = attrs[index][1]

                if val is not None and "f-col-recent" in val:
                    self.flagNews = True
                    print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        if self.flagNews and tag == "section":
            self.flagNews = False

    def handle_data(self, data):
        if self.flagNews:
            self.news.append(data)
            print("Encountered some data: ", data)


def get_news():
    res = requests.get(
        "https://news.microsoft.com/zh-cn/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        },
    )

    body = res.content.decode()
    # print(body)

    news = []
    parser = MyHTMLParser()

    parser.feed(body)
    for item in parser.news:
        str_replaced = item.replace("\n", "").replace("\t", "")
        if str_replaced and str_replaced != " ":
            news.append(str_replaced)

    return news
