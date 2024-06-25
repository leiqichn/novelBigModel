# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class NovelCrawlerPipeline:
    def __init__(self) -> None:
        self.file = open('banbijiang.json', 'w')
        self.file.write("[\n")
        self.first_item = True  # 记录是否为第一个 item

    def __del__(self) -> None:
        self.file.write("\n]")
        self.file.close()  # 关闭文件

    def process_item(self, item, spider):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(",\n")  # 写入逗号分隔
        line = json.dumps(
            dict(item),
            ensure_ascii=False,
            indent=4
        )
        self.file.write(line)  # 写入JSON对象
        return item
