# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import sqlite3

class QuoteWebScrapingPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = sqlite3.connect('allmyquotes.db')
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS tbl_demo """)
        self.cursor.execute("""  create table tbl_demo (desc text ,author text,tag text) """)

        
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.cursor.execute("""insert into tbl_demo values (?,?,?)""",(item['desc'][0],item['author'][0],item['tag'][0]))
        self.con.commit()



