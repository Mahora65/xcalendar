import scrapy
from scrapy_selenium import SeleniumRequest


class XbotSpider(scrapy.Spider):
    name = 'xbot'

    def start_requests(self):
        yield SeleniumRequest(
            url=f"https://www.set.or.th/set/xcalendar.do?eventType=&index=0&language=en&country=US",
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        table = response.xpath("//div[@class='set-tab-gray separate-content']")
        month = table.xpath(".//ul/li[@class='active first']/a/text()").get()
        rows = table.xpath(".//div/div/table/tbody/tr")
        for row in rows:
            columns = row.xpath(".//td")
            for column in columns:
                day = str(column.xpath(".//div[1]/strong/text()").get())
                contents = column.xpath(".//div/a/text()").getall()
                if any(map(str.isdigit, day)):
                    isnum = [int(s) for s in day.split() if s.isdigit()]
                    date = str(isnum[0]) + " " + str(month)
                    content = list(map(str.split, contents))
                    for xsymbol in content:
                        yield {
                            "date": date,
                            "symbol": xsymbol[0],
                            "mark": xsymbol[2]
                        }
        navbar = table.xpath(".//ul/li/a/@href").getall()
        print(navbar)
        gen = (i for i, x in enumerate(navbar) if x == "#")
        for i in gen: print(i)
