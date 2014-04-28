# -*- coding: utf-8 -*-
from flask import Flask, render_template
import urllib2
import json
import string

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
	return '''食用方法：<br>
显示多人游戏签名，用户名使用逗号隔开：osuuserinfo.sinaapp.com/userinfo/<用户名><br>
例子：osuuserinfo.sinaapp.com/userinfo/Grit,Yakumo Yukari,crucify_m_l,Kotono Yuuri<br>
<br>
<a href=/userinfocollege
>显示高校赛队伍与选手信息</a>'''

@app.route("/userinfo/<users>")
def userinfo(users):
        userlist = users.split(',')
        html = "";
        for user in userlist:
                html += "<img src=\"http://osusig.ppy.sh/image1.png?uid="+user+"&m=0\"/>"
	return html

@app.route("/userinfocollege")
def userinfoCollege():
        teamname = '''*五辻魔法饕鬄结社之夏【清华大学】
                    水源三神器【上海交通大学①】
                    不服来草【上海大学】
                    南京建大凤听大奥溶甲苯星微风不艹船亲卫队【南京大学+东南大学+南京理工大学】
                    上海爱白丝幻乐团【同济大学+中南民族大学+东华大学】
                    少打音游多读书【华东理工大学+上海海事大学】
                    贝老师和他的学生们【西安交通大学+西安电子科技大学】
                    求是一轮游【浙江大学】
                    水源大水狗【上海交通大学②】
                    大学城书店【广州大学城】
                    成都旅游观光团【四川大学+西南交通大学】
                    我们去推了紫妈【浙江中医药大学+苏州大学+乌鲁木齐新疆大学+贵州大学+北京信息科技大学】
                    中国恶俗幼儿园附属大学【中国科学技术大学+北京化工大学】
                    超高校级の恶俗【北京航天航空大学】
                    四只沙包飞飞飞【上海财经大学+上海金融学院】
                    天大造纸厂【天津大学】'''
        teamnameList = teamname.split('\n');
        teammember = '''Yakumo Yukari,[ZN],Grit,MoleAkarin,celebi
chickgod,Elinia,- N a n a m i -,P2O5
LegendTX,i am super blue cat,Sakuya san,s i n k,Valkyrie-
hard to freeze,Peach,oohily,IN4001,Okamiroy,nasia
[Sakagami Tomoyo],YY10000,andy_8yue,chihopiaodu250,Takayama Maria
Spring Roll,sasmax,Reclude,-Akimoto Akira-,-Kagami Yuki-
sweetod,Coconron,Ryuuka Toki,uniside,dik2141,nightfiend
lucklychenhan,bakapan,one7th,Ou_Yuki,The_reAsOn
zwsr,[-Lucario-],[Minakami Yuki],leo937549163,yanjiasen4,chinmeitou
supersbj,Leefreud,Sharlo,Active,nadesico
DOM,xcl1989,lv5judgelight,elona_H,mythice
cuo,Nagi awa,yuxi822,weihezhemediao,CHNxE
ichibannobaka,huoyaoyuan,liuyiqiangbu,hyheleh,Remind
Scarlet Rin,Mollon,Operation Skuld,akastu_dck,kingartoria
ZKforever,BloodyValentin,KaNeyome,oyym,biribiris
kamisamaaa,knightkh,haodumiao,azraelim,xiaodingding'''
        teammemberList = teammember.split('\n');
        html = "<head><meta http-equiv=Content-Type content=\"text/html;charset=utf-8\"><title>osu高校赛 </title></head><body>\n"
        for i in range(0,16):
                html += teamnameList[i]+"<br>"
                memberList = teammemberList[i].split(',')
                for member in memberList:
                        html += "<img src=\"http://osusig.ppy.sh/image1.png?uid="+member+"&m=0\"/>"
                html += "<br><br>"
        html += "</body>"
        return html

@app.route("/try")
def trysth():
        url_try = "https://osu.ppy.sh/api/k=978f87e832993744672da5af5bb32a11980e02ec&u=Grit"
        response = urllib2.urlopen(url_try).read()
        #data = json.loads(response)
        return response

if __name__ == "__main__":
	app.run()


