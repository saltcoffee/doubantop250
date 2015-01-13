# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class TutorialPipeline(object):
    
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='doubanmovies')
        #self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        self.insert_data(item)
        #self.conn.close()
        return item


    def insert_data(self, item):   
        for i in xrange(0, 25):
            cur = self.conn.cursor()
            sql = "insert into top250 (title, link, rank) values ('%s', '%s', '%s')" % (item['title'][i], item['link'][i], item['rank'][i])
            cur.execute(sql)
            self.conn.commit()
        #self.conn.close()
