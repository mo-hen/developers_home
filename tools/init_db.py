from peewee import *
import sys;
sys.path.append('./');
from models import *

import hashlib


if __name__ == '__main__':
    db.connect()
    db.create_tables([User,Nav,Banner,Document,Task,Sample,Tool,Video,Community])

    passwd="123456"
    passwd_hash=hashlib.sha224("{0}".format(passwd).encode('utf-8')).hexdigest()

    User(username="tom", passwd=passwd_hash,role="user").save()
    User(username="admin", passwd=passwd_hash,role="admin").save()

    Nav(title="Tasks", url="#tasks").save()
    Nav(title="Samples", url="#samples").save()
    Nav(title="Documents", url="#documents").save()
    Nav(title="SDK & Tools", url="#tools").save()
    Nav(title="Videos", url="#videos").save()
    Nav(title="Community", url="#community").save()
    Nav(title="Explorer", url="http://dev.trustnote.org:3000").save()

    banner_text = "Here you will find APIs, sample code and documentation that teaches you how to build a decentralized app running on a fast, scalable, and truly decentralized blockchain powered by TrustNote."
    Banner(title="TrustNote while change the world",text=banner_text,img="/static/images/banner/right.png").save()

    Task(title="build RustSDK on ARM", icon="/static/images/task_icons/1.png",text="",users="",status="",url="").save()
    Task(title="Tasks_2", icon="/static/images/task_icons/2.png",text="",users="",status="",url="").save()
    Task(title="Tasks_3", icon="/static/images/task_icons/3.png",text="",users="",status="",url="").save()

    Sample(title="An iot light for TTT", icon="/static/images/sample_icons/1.png",text="",url="").save()
    Sample(title="A Voting System", icon="/static/images/sample_icons/2.png",text="",url="").save()
    Sample(title=" A web wallet use HeadlessRPC", icon="/static/images/sample_icons/3.png",text="",url="").save()

    Document(title="How to code a Token APP use HeadlessRPC in 2 minutes?",text="With a few simple steps, you can build your tokenized applications from scratch. Develop a truly decentralized app was never so easy!",img="",url="").save()

    Tool(title="title",text="haha",icon="/static/images/tool_icons/1.png",url="").save()
    Tool(title="title",text="haha",icon="/static/images/tool_icons/2.png",url="").save()
    Tool(title="title",text="haha",icon="/static/images/tool_icons/3.png",url="").save()

    Video(title="title",text="haha",icon="/static/images/video_icons/1.jpg",url="").save()
    Video(title="title",text="haha",icon="/static/images/video_icons/2.jpg",url="").save()
    Video(title="title",text="haha",icon="/static/images/video_icons/3.jpg",url="").save()

    Community(title="title",icon="/static/images/community_icons/facebook.png",url="http://facebook.com/trustnote").save()
    Community(title="title",icon="/static/images/community_icons/reddit.png",url="http://reddit.com/trustnote").save()

    db.close()
