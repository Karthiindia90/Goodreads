# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_quotation(value):
    return value.replace(u"\u201d",'').replace(u"\u201c",'').replace(u"\u00ef","'").replace("\n",'')

class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field(
        input_processor= MapCompose(str.strip,remove_quotation),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor = MapCompose(remove_quotation,str.strip,remove_tags),
        output_processor = TakeFirst()
    )
    tags = scrapy.Field(
        input_processor = MapCompose(remove_tags,remove_quotation),
        output_processor= Join(',')
    )
