from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.linemanager import LineManager
import os

token = 'Y484Uowhl0mb5Bmq3wI4Zgfxia81t4giez8jAQByvmc'

if __name__ == '__main__':
    messenger = LineManager(token)
    if os.path.isdir("db"):
        if os.path.isfile("db/xmarks.csv"):
            os.remove("db/xmarks.csv")
    else:
        os.mkdir("db")
    process = CrawlerProcess(get_project_settings())
    process.crawl("xbot")
    process.start()
    messenger.xmarkfilter()
    messenger.xmarktdsum()
    messenger.xmarkbody()