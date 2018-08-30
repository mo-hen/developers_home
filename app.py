#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, jsonify,render_template,request,redirect,url_for,session
from argparse import ArgumentParser
from peewee import *
import random

import sys;
sys.path.append('./');
from models import *



app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.before_request
def checksession():
    if "admin" in request.path:
        if "role" in session:
            #验证是否是admin
            if session["role"]=="admin":
                pass
            else:
                return redirect(url_for("home"))

        else:
            return redirect(url_for("login"))
    if "user" in request.path:
        #验证是否是user
        pass
@app.route('/')
def home():
    navs = [nav for nav in Nav.select().order_by(Nav.id.desc())]
    tasks = [task for task in Task.select()]
    samples = [sample for sample in Sample.select()]
    banner = [banner for banner in Banner.select()][0]
    document = [document for document in Document.select()][0]
    tools = [tool for tool in Tool.select()]
    videos = [video for video in Video.select()]
    communitys = [community for community in Community.select()]



    return render_template('index.html',banner = banner,navs = navs,tasks = tasks,samples=samples,document=document,tools=tools,videos=videos,communitys=communitys,session=session)
    #return jsonify("no nodes")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        passwd=request.form.get('passwd')

        users= User.select().where(User.username == username)
        if len(users)==1:
            user=users[0]
            if user.passwd == passwd:

                session["username"]=user.username
                session["role"]=user.role
                #以后可以加头像

                return "ok"
            else:
                return "err pass"
        else:
            return "err"

    if request.method == 'GET':
        num = random.randint(1,3)
        return render_template('login.html',num=num)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/navs',methods=['GET'])
def admin_navs():
    query = Nav().select()
    navs = [nav for nav in query]
    return render_template('admin/navs.html',navs = navs)

@app.route('/admin/banner',methods=['GET'])
def admin_banner():
    query = Banner().select()
    banner = [banner for banner in query]
    return render_template('admin/banner.html',banner = banner)
@app.route('/admin/banner/update',methods=['POST'])
def admin_banner_update():
    if request.method == 'POST':
        title=request.form.get('title')
        text=request.form.get('text')
        img=request.form.get('img')
        Banner().update(title=title,text=text,img=img).execute()
        return redirect(url_for("admin_banner"))


@app.route('/admin/documents',methods=['GET'])
def admin_documents():
    query = Document().select()
    document = [document for document in query]
    return render_template('admin/documents.html',document = document)
@app.route('/admin/documents/update',methods=['POST'])
def admin_documents_update():
    if request.method == 'POST':
        title=request.form.get('title')
        text=request.form.get('text')
        img=request.form.get('img')
        url=request.form.get('url')
        Document().update(title=title,text=text,img=img,url=url).execute()
        return redirect(url_for("admin_documents"))


@app.route('/admin/tasks',methods=['GET'])
def admin_tasks():
    query = Task().select()
    tasks = [task for task in query]
    return render_template('admin/tasks.html',tasks = tasks)

@app.route('/admin/tasks/insert',methods=['POST'])
def admin_tasks_insert():
    if request.method == 'POST':

        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')
        users=request.form.get('users')
        status=request.form.get('status')
        url=request.form.get('url')

        task = Task(title=title,text=text,icon=icon,users=users,status=status,url=url)
        query = task.save()
        return redirect(url_for("admin_tasks"))

@app.route('/admin/tasks/update',methods=['POST'])
def admin_taks_update():
    if request.method == 'POST':
        id=request.form.get('id')
        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')
        users=request.form.get('users')
        status=request.form.get('status')
        url=request.form.get('url')

        task = Task()
        query = task.update(title=title,text=text,icon=icon,users=users,status=status,url=url).where(Task.id == id)
        query.execute()
        return redirect(url_for("admin_tasks"))
@app.route('/admin/tasks/delete',methods=['POST'])
def admin_tesks_del():
    if request.method == 'POST':
        id=request.form.get('id')
        task = Task()
        query = task.delete().where(Task.id == id)
        query.execute()
        return redirect(url_for("admin_tasks"))



@app.route('/admin/samples',methods=['GET'])
def admin_samples():
    query = Sample().select()
    samples = [sample for sample in query]
    return render_template('admin/samples.html',samples = samples)

@app.route('/admin/samples/insert',methods=['POST'])
def admin_samples_insert():
    if request.method == 'POST':

        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')
        url=request.form.get('url')

        sample = Sample(title=title,text=text,icon=icon,url=url)
        query = sample.save()
        return redirect(url_for("admin_samples"))

@app.route('/admin/samples/update',methods=['POST'])
def admin_samples_update():
    if request.method == 'POST':
        id=request.form.get('id')
        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')

        url=request.form.get('url')

        sample = Sample()
        query = sample.update(title=title,text=text,icon=icon,url=url).where(Sample.id == id)
        query.execute()
        return redirect(url_for("admin_samples"))

@app.route('/admin/samples/delete',methods=['POST'])
def admin_samples_del():
    if request.method == 'POST':
        id=request.form.get('id')
        sample = Sample()
        query = sample.delete().where(Sample.id == id)
        query.execute()
        return redirect(url_for("admin_samples"))




@app.route('/admin/tools',methods=['GET'])
def admin_tools():
    query = Tool().select()
    tools = [tool for tool in query]
    return render_template('admin/tools.html',tools = tools)

@app.route('/admin/tools/insert',methods=['POST'])
def admin_tools_insert():
    if request.method == 'POST':

        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')
        url=request.form.get('url')

        tools = Tool(title=title,text=text,icon=icon,url=url)
        query = tools.save()
        return redirect(url_for("admin_tools"))

@app.route('/admin/tools/update',methods=['POST'])
def admin_tools_update():
    if request.method == 'POST':
        id=request.form.get('id')
        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')

        url=request.form.get('url')

        tools = Tool()
        query = tools.update(title=title,text=text,icon=icon,url=url).where(Tool.id == id)
        query.execute()
        return redirect(url_for("admin_tools"))

@app.route('/admin/tools/delete',methods=['POST'])
def admin_tools_del():
    if request.method == 'POST':
        id=request.form.get('id')
        tools = Tool()
        query = tools.delete().where(Tool.id == id)
        query.execute()
        return redirect(url_for("admin_tools"))



@app.route('/admin/videos',methods=['GET'])
def admin_videos():
    query = Video().select()
    videos = [video for video in query]
    return render_template('admin/videos.html',videos = videos)

@app.route('/admin/videos/insert',methods=['POST'])
def admin_videos_insert():
    if request.method == 'POST':

        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')
        url=request.form.get('url')

        video = Video(title=title,icon=icon,text=text,url=url)
        query = video.save()
        return redirect(url_for("admin_videos"))

@app.route('/admin/videos/update',methods=['POST'])
def admin_videos_update():
    if request.method == 'POST':
        id=request.form.get('id')
        title=request.form.get('title')
        text=request.form.get('text')
        icon=request.form.get('icon')

        url=request.form.get('url')

        videos = Video()
        query = videos.update(title=title,icon=icon,text=text,url=url).where(Video.id == id)
        query.execute()
        return redirect(url_for("admin_videos"))

@app.route('/admin/videos/delete',methods=['POST'])
def admin_videos_del():
    if request.method == 'POST':
        id=request.form.get('id')
        videos = Video()
        query = videos.delete().where(Videos.id == id)
        query.execute()
        return redirect(url_for("admin_videos"))


@app.route('/admin/communitys',methods=['GET'])
def admin_communitys():
    communitys = [community for community in Community().select()]
    return render_template('admin/communitys.html',communitys = communitys)

@app.route('/admin/communitys/insert',methods=['POST'])
def admin_communitys_insert():
    if request.method == 'POST':

        title=request.form.get('title')
        icon=request.form.get('icon')
        url=request.form.get('url')

        communitys = Community(title=title,icon=icon,url=url)
        query = communitys.save()
        return redirect(url_for("admin_communitys"))

@app.route('/admin/communitys/update',methods=['POST'])
def admin_communitys_update():
    if request.method == 'POST':
        id=request.form.get('id')
        title=request.form.get('title')
        icon=request.form.get('icon')
        url=request.form.get('url')

        communitys = Community()
        query = communitys.update(title=title,icon=icon,url=url).where(Community.id == id)
        query.execute()
        return redirect(url_for("admin_communitys"))

@app.route('/admin/communitys/delete',methods=['POST'])
def admin_communitys_del():
    if request.method == 'POST':
        id=request.form.get('id')
        communitys = Community()
        query = communitys.delete().where(Community.id == id)
        query.execute()
        return redirect(url_for("admin_communitys"))





@app.route('/admin/navs/insert',methods=['POST'])
def admin_navs_insert():
    if request.method == 'POST':

        title=request.form.get('title')
        url=request.form.get('url')
        nav = Nav(title=title,url=url)
        query = nav.save()
        return redirect(url_for("admin_navs"))

@app.route('/admin/navs/update',methods=['POST'])
def admin_navs_update():
    if request.method == 'POST':
        id=request.form.get('id')
        title=request.form.get('title')
        url=request.form.get('url')
        nav = Nav()
        query = nav.update(title=title,url=url).where(Nav.id == id)
        query.execute()
        return redirect(url_for("admin_navs"))

@app.route('/admin/navs/delete',methods=['POST'])
def admin_navs_del():
    if request.method == 'POST':
        id=request.form.get('id')
        nav = Nav()
        query = nav.delete().where(Nav.id == id)
        query.execute()
        return redirect(url_for("admin_navs"))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
