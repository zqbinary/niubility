# -*- coding: utf-8 -*-
import os 
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

from werobot.robot import werobot
from werobot.session.saekvstorage import SaeKVDBStorage
from douban import client

session_storage = SaeKVDBStorage()

robot = werobot.WeRoBot(token="freesz", enable_session=True,
                        session_storage=session_storage)

@robot.filter("大牛")
def person(message, session):
    session['last'] = message.content
    return "大牛列表,请输入TED牛人序号"

@robot.filter("书名")
def bookname(message, session):
    session['last'] = message.content
    return "请输入书名"

@robot.text
def douban(message, session):
    last  = session.get('last', 0)
    print message.content
    if last == u"书名":
        # client.book.search(q, tag, start, count)  
        # ret = client.book.search(message.content, 0, 0, 3)
        #print ret
        return message.content

@robot.text
def hello(message, session):
    count = session.get("count", 0) + 1
    session["count"] = count
    return "请输入'大牛', 你累计发了 %s 条消息" % count

@robot.subscribe
def subscribe(message):
        return "Weclome to niubility! 输入'大牛','书名',有惊喜哦！"


