#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute(['scrapy','crawl','ershoufang'])
# cmdline.execute(['scrapy','crawl','ershoufang','-s','LOG_FILE=ershoufang.log'])