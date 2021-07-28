# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3

class LaughterjokesPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = sqlite3.connect("myjokes.db")
        self.cursor = self.con.cursor()
        
    def create_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS tbl_jokes """)
        self.cursor.execute(""" create table tbl_jokes (title text, like text, dislike text) """)
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.cursor.execute(""" insert into tbl_jokes values (?,?,?) """ , (item['title'][0],item['like'][0],item['dislike'][0]) )
        self.con.commit()



