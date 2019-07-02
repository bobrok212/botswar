#utf_8 *lineX [prankBots Creator]
from Rank.lineX import *
from Rank.service.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from datetime import datetime
from threading import Thread
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
#from gtts import gTTS
_session = requests.session()
botStart = time.time()
#gmails = codecs.open("gmail.json","r","utf-8")
#gmail = json.load(gmails)
settingsOpen = codecs.open("JhailBots.json","r","utf-8")
JhailBots = json.load(settingsOpen)
settingsOpen = codecs.open("JhailAbouts.json","r","utf-8")
Abouts = json.load(settingsOpen)
# MASUKIN TOKEN DISINI GUYS
me= LINE ("uc1a17c17772aec197a457dfed00b2bda:aWF0OiAxNTUzNTY5NjExODQ2Cg==..ihccRGialDrcv+OlEzb+ify+jmY=")
kk1 = LINE ("u09f57b5c61573c7586d17f44fc5a1b7f:aWF0OiAxNTUzNTY4MzkzMzA3Cg==..Whc06doypa6tySXDvK1VgeQ7V4Y=")
kk2 = LINE ("u6fa3a484aa09f868de93e241301196fc:aWF0OiAxNTUzNTY4NjQ0NDIyCg==..kIR0/cy6NxcpfW1EE1Hdp46rUoU=")
kk3 = LINE ("u7d6668e5f1347cb4de0148e6ba41cb35:aWF0OiAxNTUzNTY4OTAxMDk2Cg==..InE96S+/jP9I9MDa2FwHZwfScuI=")
kk4 = LINE ("u5b4938a13b4565f88f96e634eb8c0cee:aWF0OiAxNTUzNTY5MDk2Mjg3Cg==..Lb8esfvKYR+kIuxBisaXfx9ud3M=")
kk5 = LINE ("u8e9101f38cff9f81e92ee8b0489f6cd6:aWF0OiAxNTUzNTY5MzI0OTkyCg==..pgfthuJuVhM8vY8aJEpyr1KMFr4=")
jss = LINE("u803c079b12b0242eb65386f4dce7ddc4:aWF0OiAxNTUzNTY4MjAxODcwCg==..+Hno9fONi/aRU/XuNT1nU4/EiaA=")
#__________________________
runnerResponse = "\n\n•«☠»••«☠»••«☠»••«☠»••«☠»••«☠»••«☠»•\n\n•«☠»••«☠»•SUCCES LOGIN•«☠»••«☠»•\n\n•«☠»••«☠»••«☠»••«☠»••«☠»••«☠»••«☠»•"
me.log(runnerResponse)
meProfile = me.getProfile()
meM = me.getProfile().mid
meSettings = me.getSettings()
kk1Profile = kk1.getProfile()
kk2Profile = kk2.getProfile()
kk3Profile = kk3.getProfile()
kk4Profile = kk4.getProfile()
kk5Profile = kk5.getProfile()
jssProfile = jss.getProfile()
meM = meProfile.mid
kk1Rank = kk1Profile.mid
kk2Rank = kk2Profile.mid
kk3Rank = kk3Profile.mid
kk4Rank = kk4Profile.mid
kk5Rank = kk5Profile.mid
jssRank = jssProfile.mid
oepoll = OEPoll(me)
Admin = JhailBots["MID"]
Owner = ["uc1a17c17772aec197a457dfed00b2bda","u945e817cbdb14360333950f3ff5b06a1"]
Stiles = "│○☠⇉"
BotWar = [meM,kk1Rank,kk2Rank,kk3Rank,kk4Rank,kk5Rank,jssRank]
allrepositories = [me,kk1,kk2,kk3,kk4,kk5,jss]
msg_dict = {}
msg_dict1 = {}
respontags = {
    "Auto_text": "\n╭────────────────╮\n┃💢↳Apaan Sich ngetag mulu ...❢❢┃\n╰────────────────╯"
}
Sid={
    "Tar":{},
    "Red":{},
    "Reason":{}
}
mid = me.getProfile().mid
JhailBots["myProfile"]["displayName"] = meProfile.displayName
JhailBots["myProfile"]["statusMessage"] = meProfile.statusMessage
cont = me.getContact(meM)
JhailBots["myProfile"]["pictureStatus"] = meProfile.pictureStatus
coverId = me.getProfileDetail()["result"]["objectId"]
apikey_com = "u0ac948397fbc732bd3bc5ca273faa698"
coverId = me.getProfileDetail()["result"]["objectId"]
JhailBots["myProfile"]["coverId"] = coverId
Extr = meProfile.displayName
all_Square = ["uf7aec322baf0b1ec1e033319fdfd2e52","ud6e4cc7303ff0573962c1128b1a8a907","u864bb709a442b6329c42672cb17ab146","u89d8f38f583525642f53c1a94200b93d","u47a6ac87c0981e2600671249876f0f4c","ub9cbfe79dac0cb5f8e6a702e6749084f"]
for busht in allrepositories:
    for anding in all_Square:
        try:
            busht.findAndAddContactsByMid(anding)
        except:pass
    for botKickers in BotWar:
        try:
            busht.findAndAddContactsByMid(botKickers)
        except:pass
def backupData():
    try:
        backup = JhailBots
        f = codecs.open('JhailBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Abouts
        f = codecs.open('JhailAbouts.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        ErrorX(error)
        return False
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@JhailBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def Run_Xp():
    print ("RESTART")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
Devert = "My name is "+cont.displayName+"\nMy git your bots"
mulai = time.time()
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(meM).statusMessage if me.getContact(meM).statusMessage != '' else 'creator By meMots |ID LINE|\nlos.rhewel', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(meM).displayName,}
    return me.sendMessage(to, me.getContact(meM).displayName, contentMetadata, 19)
def ErrorX(text):
    me.log("data: " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@JhailBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ErrorX(error)
        me.sendMessage(to, "Error\n\n" + str(error))
extras = Stiles+"ᴍʏ ɴᴀᴍᴇ: "+Extr+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = me.getAllContactIds()
        gid = me.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = me.getContact(meM)
        me.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nᴄʀᴇᴀᴛᴏʀ ʙʏ : ᴘʀᴀɴᴋʙᴏᴛs. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
warKey  = """
     ╭────••«☠»••────╮  
            •«☠»• ◈ key
            •«☠»• ◈ me
            •«☠»• ◈ add
            •«☠»• ◈ bots 
            •«☠»• ◈ join[.]
            •«☠»• ◈ out [,]
            •«☠»• ◈ speed
            •«☠»• ◈ respon
            •«☠»• ◈ banlist
            •«☠»• ◈ clearban
            •«☠»• ◈ ceplok @
            •«☠»• ◈ ceplokin @
    ╰────••«☠»••────╯
                  (─••«☠»••─)
    ◈──[✮ᴊʜᴀɪʟ ᴛᴇᴀᴍ ᴮᴼᵀʟɪɴᴇ ✯ 
    ◈─[✮ ᴅɪɴᴀsᴛʏ ɴᴅ❍ᴋ ᴄᴇᴘʟ❍ᴋ ✯
        •«☠»ʙ❍ᴛsWar version«☠»•
"""
def SqL_R(text):
    R_SQL = text.lower()
    if JhailBots["key"] == True:
        if R_SQL.startswith(JhailBots["text"]):
            JhailBotsData = R_SQL.replace(JhailBots["text"],"")
        else:
            JhailBotsData = "Undefined command"
    else:
        JhailBotsData = text.lower()
    return JhailBotsData
def serviceX(rank):
    global groupParam
    opps1 = rank.param1
    opps2 = rank.param2
    opps3 = rank.param3
    try:
        if rank.type == 0:
            return
        if rank.type == 19 or rank.type == 32:
            if meM in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk1.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                        me.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk2.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                            me.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk3.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                                me.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk4.kickoutFromGroup(opps1,[opps2])
                                    me.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk5.inviteIntoGroup(opps1,[opps3])
                                        kk5.kickoutFromGroup(opps1,[opps2])
                                        me.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(opps1)
                                            grup = jss.getGroup(opps1)
                                            grup.preventedJoinByTicket = False
                                            jss.updateGroup(grup)
                                            Ti = reissueGroupTicket(opps1)
                                            for all in allrepositories:
                                                all.acceptGroupInvitationByTicket(opps1, Ti)
                                            jss.leaveGroup(opps1)
                                            kk1.inviteIntoGroup(opps1,[opps3])
                                        except:pass
            if kk1Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk2.inviteIntoGroup(opps1,[opps3])
                        kk2.kickoutFromGroup(opps1,[opps2])
                        kk1.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk3.inviteIntoGroup(opps1,[opps3])
                            kk3.kickoutFromGroup(opps1,[opps2])
                            kk1.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk4.inviteIntoGroup(opps1,[opps3])
                                kk4.kickoutFromGroup(opps1,[opps2])
                                kk1.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk5.inviteIntoGroup(opps1,[opps3])
                                    kk5.kickoutFromGroup(opps1,[opps2])
                                    kk1.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk1.inviteIntoGroup(opps1,[opps3])
                                        kk1.kickoutFromGroup(opps1,[opps2])
                                        me.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(opps1)
                                            grup = jss.getGroup(opps1)
                                            grup.preventedJoinByTicket = False
                                            jss.updateGroup(grup)
                                            Ti = reissueGroupTicket(opps1)
                                            for all in allrepositories:
                                                all.acceptGroupInvitationByTicket(opps1, Ti)
                                            jss.leaveGroup(opps1)
                                            kk2.inviteIntoGroup(opps1,[opps3])
                                        except:pass
            if kk2Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk3.inviteIntoGroup(opps1,[opps3])
                        kk3.kickoutFromGroup(opps1,[opps2])
                        kk2.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk4.inviteIntoGroup(opps1,[opps3])
                            kk4.kickoutFromGroup(opps1,[opps2])
                            kk2.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk5.inviteIntoGroup(opps1,[opps3])
                                kk5.kickoutFromGroup(opps1,[opps2])
                                kk2.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    me.inviteIntoGroup(opps1,[opps3])
                                    me.kickoutFromGroup(opps1,[opps2])
                                    kk2.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk1.inviteIntoGroup(opps1,[opps3])
                                        kk1.kickoutFromGroup(opps1,[opps2])
                                        kk2.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(opps1)
                                            grup = jss.getGroup(opps1)
                                            grup.preventedJoinByTicket = False
                                            jss.updateGroup(grup)
                                            Ti = reissueGroupTicket(opps1)
                                            for all in allrepositories:
                                                all.acceptGroupInvitationByTicket(opps1, Ti)
                                            jss.leaveGroup(opps1)
                                            kk3.inviteIntoGroup(opps1,[opps3])
                                        except:pass
            if kk3Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk4.inviteIntoGroup(opps1,[opps3])
                        kk4.kickoutFromGroup(opps1,[opps2])
                        kk3.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk5.inviteIntoGroup(opps1,[opps3])
                            kk5.kickoutFromGroup(opps1,[opps2])
                            kk3.acceptGroupInvitation(opps1)
                        except:
                            try:
                                me.inviteIntoGroup(opps1,[opps3])
                                me.kickoutFromGroup(opps1,[opps2])
                                kk3.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk1.inviteIntoGroup(opps1,[opps3])
                                    kk1.kickoutFromGroup(opps1,[opps2])
                                    kk3.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk2.inviteIntoGroup(opps1,[opps3])
                                        kk2.kickoutFromGroup(opps1,[opps2])
                                        kk3.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(opps1)
                                            grup = jss.getGroup(opps1)
                                            grup.preventedJoinByTicket = False
                                            jss.updateGroup(grup)
                                            Ti = reissueGroupTicket(opps1)
                                            for all in allrepositories:
                                                all.acceptGroupInvitationByTicket(opps1, Ti)
                                            jss.leaveGroup(opps1)
                                            kk4.inviteIntoGroup(opps1,[opps3])
                                        except:pass
            if kk4Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk5.inviteIntoGroup(opps1,[opps3])
                        kk5.kickoutFromGroup(opps1,[opps2])
                        kk4.acceptGroupInvitation(opps1)
                    except:
                        try:
                            me.inviteIntoGroup(opps1,[opps3])
                            me.kickoutFromGroup(opps1,[opps2])
                            kk4.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk1.inviteIntoGroup(opps1,[opps3])
                                kk1.kickoutFromGroup(opps1,[opps2])
                                kk4.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk2.inviteIntoGroup(opps1,[opps3])
                                    kk2.kickoutFromGroup(opps1,[opps2])
                                    kk4.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        kk3.inviteIntoGroup(opps1,[opps3])
                                        kk3.kickoutFromGroup(opps1,[opps2])
                                        kk4.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(opps1)
                                            grup = jss.getGroup(opps1)
                                            grup.preventedJoinByTicket = False
                                            jss.updateGroup(grup)
                                            Ti = reissueGroupTicket(opps1)
                                            for all in allrepositories:
                                                all.acceptGroupInvitationByTicket(opps1, Ti)
                                            jss.leaveGroup(opps1)
                                            kk5.inviteIntoGroup(opps1,[opps3])
                                        except:pass
            if kk5Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk3.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                        kk5.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk1.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                            kk5.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk2.inviteIntoGroup(opps1,[opps3])
                                kk4.kickoutFromGroup(opps1,[opps2])
                                kk5.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk3.kickoutFromGroup(opps1,[opps2])
                                    kk5.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        me.inviteIntoGroup(opps1,[opps3])
                                        me.kickoutFromGroup(opps1,[opps2])
                                        kk5.acceptGroupInvitation(opps1)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(opps1)
                                            grup = jss.getGroup(opps1)
                                            grup.preventedJoinByTicket = False
                                            jss.updateGroup(grup)
                                            Ti = reissueGroupTicket(opps1)
                                            for all in allrepositories:
                                                all.acceptGroupInvitationByTicket(opps1, Ti)
                                            jss.leaveGroup(opps1)
                                            me.inviteIntoGroup(opps1,[opps3])
                                        except:pass
            if jssRank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    JhailBots["blacklist"] = True
                    try:
                        kk1.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk2.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk3.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk4.kickoutFromGroup(opps1,[opps2])
                                except:
                                    try:
                                        kk5.inviteIntoGroup(opps1,[opps3])
                                        kk5.kickoutFromGroup(opps1,[opps2])
                                    except:
                                        try:
                                            me.inviteIntoGroup(opps1,[opps3])
                                            me.inviteIntoGroup(opps1,[opps3])
                                        except:pass
        if rank.type == 17:
            if opps2 in JhailBots["blacklist"]:
                try:
                    kk1.kickoutFromGroup(opps1,[opps2])
                except:
                    try:
                        kk2.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk3.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk4.kickoutFromGroup(opps1,[opps2])
                            except:
                                try:
                                    kk5.kickoutFromGroup(opps1,[opps2])
                                except:pass
            else:pass
        if rank.type == 13:
            if opps2 in JhailBots["blacklist"]:
                try:
                    kk5.kickoutFromGroup(opps1,[opps2])
                except:
                    try:
                        kk4.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk3.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk2.kickoutFromGroup(opps1,[opps2])
                            except:
                                try:
                                    kk1.kickoutFromGroup(opps1,[opps2])
                                except:pass
            else:pass
        if rank.type == 26 or rank.type == 25:
            msg = rank.message
            Id = msg.id
            R = msg.to
            D = msg._from
            Proses_message = msg.text
            if Proses_message == "Active" or Proses_message == "On":
                if D in Owner or D in meM:
                    JhailBots["bot"] = True
                    me.sendMessage(R,"✔Bot active")
                    me.sendMessage(R,"╭─━━━░★░━━━─╗\n    ◈☞ᴀᴄᴛɪᴠᴇ sᴇʟғ ʙ❍ᴛs\n             ✔ ᴅᴏɴᴇ sᴜᴄᴄᴇs\n╚─━━━░★░━━━─╯")
                    JhailBots["Conection"] = R
                    Run_Xx()
                    
            if Proses_message == "Non active" or Proses_message == "Off":
                print ("NOTIF BOT NON ACTIVE")
                if D in Owner or D in meM:
                    JhailBots["bot"] = False
                    me.sendMessage(R,"Bot Non Active")
                    me.sendMessage(R,"╭─━━░★░━━─╗\n     ɴ❍ɴ ᴀᴄᴛɪᴠᴇ \n     sᴇʟғ ʙ❍ᴛs\n      ✔ ᴅᴏɴᴇ sᴜᴄᴄᴇs\n╚─━━░★░━━─╯")
                
        if rank.type == 25 or rank.type == 26:
          if JhailBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            Gr = opps1
            OperJhailBotsData = JhailBots["text"].title()
            if JhailBots["key"] == False:
                 OperJhailBotsData = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if D != me.profile.mid:
                        to = D
                    else:
                        to = R
                elif msg.toType == 1:
                    to = R
                elif msg.toType == 2:
                    to = R
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        JhailBotsData = SqL_R(text)
                        if JhailBotsData == Abouts["1"]:
                          if D in Owner or D in meM:
                            Res= extras+Stiles+Abouts["0"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["1"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["2"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["3"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["4"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["5"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["6"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["7"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["8"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["9"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["10"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["11"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["12"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["13"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["14"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["15"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["16"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["17"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["18"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["19"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["20"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["21"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["22"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["23"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["24"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["25"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["26"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["27"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["28"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["29"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["30"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["31"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["32"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["33"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["34"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["35"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["36"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["37"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["73"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["74"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["75"]+"\n"
                            Res+= Stiles+"◈. "+OperJhailBotsData+Abouts["76"]+"\n"
                            Res+= Stiles+"_ᴅɪɴᴀsᴛʏ ɴᴅ❍ᴋ ᴄᴇᴘʟ❍ᴋ_\n"
                            if JhailBots["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if JhailBots["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if JhailBots["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            Res+= Stiles+"____________________\n"
                            Res+= Stiles+"______SelfName______\n"+Stiles+meProfile.displayName+"\n"
                            me.sendMessage(apikey_com,Devert)
                            me.sendMessage(R, str(Res)+Stiles+"ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs\n"+Stiles+"ᴅɪɴᴀsᴛʏ ɴᴅ❍ᴋ ᴄᴇᴘʟ❍ᴋ")
                        if JhailBotsData == Abouts["2"]:
                          if D in Owner or D in meM:
                            try:
                                me.findAndAddContactsByMid("u239b3bcf13a3b0fae950b94c5eb2f9c6")
                                Musik(R)
                                RunTheRun(apikey_com, D, "_______RESULT______\n")
                            except:Musik(R)
                        if JhailBotsData == Abouts["3"]:
                          if D in Owner or D in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "My id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            me.sendMessage(R,My_Id)
                        if JhailBotsData == Abouts["4"]:
                          if D in Owner or D in meM:
                            me.leaveGroup(R)
                        if JhailBotsData == Abouts["5"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            cu = me.getProfileCoverURL(D)          
                            path = str(cu)
                            me.sendImageWithURL(R, path)
                        if JhailBotsData.startswith(Abouts["10"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            me.sendMessage(R, "teman di tambahkan")
                        if JhailBotsData == Abouts["11"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Selesai.!!")
                            JhailBots["Conection"] = R
                            Run_Xp()
                        if JhailBotsData.startswith(Abouts["12"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            txt = teks.split("/")
                            bag1 = txt[0]
                            bag2 = txt[1]
                            bag3 = txt[2]
                            angka = ["1","2","3","4","5"]
                            latar = random.choice(angka)
                            nomor = ["1","2","3","4"]
                            background = random.choice(nomor)
                            url = "https://ari-api.herokuapp.com/retro?bg="+latar+"&txt="+background+"&text1="+bag1+"&text2="+bag2+"&text3="+bag3
                            me.sendImageWithURL(R, url)
                        if JhailBotsData.startswith(Abouts["13"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=jhail212"
                            me.sendImageWithURL(R, url)
                        if JhailBotsData == Abouts["14"]:
                          if D in Owner or D in meM:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            me.sendMessage(R, "━━━━━╦RUNTIME BOTS╦━━━━━\n ┣━╦[ {}".format(str(runtime)))
                        if JhailBotsData == Abouts["15"]:
                          if D in Owner or D in meM:
                            start = time.time()
                            me.sendMessage(R, "gooo...")
                            elapsed_time = time.time() - start
                            me.sendMessage(R,format(str(elapsed_time)))
                        if JhailBotsData == Abouts["16"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendMessage(R,h.mid)
                        if JhailBotsData == Abouts["17"]:
                          if D in Owner or D in meM:
                            contact = me.getContact(D)
                            cover = me.getProfileCoverURL(D)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            me.sendImageWithURL(R, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            me.sendImageWithURL(R, str(cover))
                            me.sendMessage(R, str(result))
                        if JhailBotsData == Abouts["18"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendVideoWithURL(R,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        if JhailBotsData.startswith(Abouts["19"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                me.sendMessage(R, str(ret_))
                        if JhailBotsData.startswith(Abouts["20"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus
                                    me.sendImageWithURL(R, str(path))
                        if JhailBotsData.startswith(Abouts["21"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus + "/vp"
                                    me.sendVideoWithURL(R, str(path))
                        if JhailBotsData.startswith(Abouts["22"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Namanya\n{}".format(str(contact.displayName)))
                        if JhailBotsData.startswith(Abouts["23"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Status kontak\n\n{}".format(str(contact.statusMessage)))
                        if JhailBotsData.startswith(Abouts["24"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    mi_d = contact.mid
                                    me.sendContact(R, mi_d)
                        if JhailBotsData.startswith(Abouts["73"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        me.kickoutFromGroup(R, [ls])
                                    except:
                                       me.sendMessage(R, "Limited !")
                        if JhailBotsData.startswith(Abouts["74"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        kk1.kickoutFromGroup(R, [ls])
                                    except:
                                        kk1.sendMessage(R, "Limited !")
                        if JhailBotsData.startswith(Abouts["75"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        me.kickoutFromGroup(R, [ls])
                                        me.inviteIntoGroup(R, [ls])
                                        me.cancelGroupInvitation(R,[ls])
                                        time.sleep(5)
                                        me.inviteIntoGroup(R, [ls])
                                    except:
                                       me.sendMessage(R, "Limited !")
                            me.sendMessage(R, msgs)
                        if JhailBotsData == Abouts["39"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(R, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        me.sendMessage(R, str(ret_))
                        if JhailBotsData == Abouts["44"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(R)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                        if JhailBotsData == Abouts["45"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    me.sendMessage(R, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil membuka Qr")
                        if JhailBotsData == Abouts["46"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == True:
                                    me.sendMessage(R, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil menutup Qr")
                        if JhailBotsData == Abouts["47"]:
                          if D in Owner or D in meM:
                            JhailBots["Add"] = True
                            me.sendMessage(R, "Already on")
                        if JhailBotsData == Abouts["48"]:
                          if D in Owner or D in meM:
                            JhailBots["Add"] = False
                            me.sendMessage(R, "Already ff")
                        if JhailBotsData == Abouts["49"]:
                          if D in Owner or D in meM:
                            JhailBots["Join"] = True
                            me.sendMessage(R, "Already on")
                        if JhailBotsData == Abouts["50"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = False
                            me.sendMessage(R, "Already off")
                        if JhailBotsData == Abouts["51"]:
                          if D in Owner or D in meM:
                            JhailBots["Read"] = True
                            me.sendMessage(R, "Already on")
                        if JhailBotsData == Abouts["52"]:
                          if D in Owner or D in meM:
                            JhailBots["Read"] = False
                            me.sendMessage(R, "Already off")
                        if JhailBotsData == Abouts["59"]:
                          if D in Owner or D in meM:
                            JhailBots["Respon"] = True
                            me.sendMessage(R, "Already on")
                        if JhailBotsData == Abouts["60"]:
                          if D in Owner or D in meM:
                            JhailBots["Respon"] = False
                            me.sendMessage(R, "Already off")
                        if JhailBotsData == Abouts["61"]:
                          if D in Owner or D in meM:
                                try:
                                    del Sid['Red'][R]
                                    del Sid['Reason'][R]
                                    del Sid['Tar'][R]
                                except:
                                    pass
                                Sid['Red'][R] = Id
                                Sid['Reason'][R] = ""
                                Sid['Tar'][R]=True
                                me.sendMessage(R, "di aktifkan untuk grup\n"+g.name)
                        if JhailBotsData == Abouts["62"]:
                          if D in Owner or D in meM:
                            if R in Sid['Red']:
                                Sid['Tar'][R]=False
                                me.sendMessage(R, "Daftar yang terlihat\n"+Sid['Reason'][msg.to])
                                me.sendMessage(R, "Already off")
                            else:
                                me.sendMessage(R, "aktifkan dulu beb")
                        if JhailBotsData == Abouts["63"]:
                         if D in Owner or D in meM:
                          group = me.getGroup(R)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠. @!".format(str(no))
                                  ret_ += "\n╚══════════════".format(str(len(dataMid)))
                                  sendMeention(R, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe)
                        if JhailBotsData == Abouts["64"]:
                          if D in Owner or D in meM:
                            try:
                                JhailBots["Add"] = True
                                JhailBots["Join"] = True
                                JhailBots["Wc"] = True
                                JhailBots["Read"] = True
                                me.findAndAddContactsByMid("u239b3bcf13a3b0fae950b94c5eb2f9c6")
                                me.sendMessage(R,"SETTING ALL IN ONLINE")
                            except:me.sendMessage(R,"SETTING ALL IN ONLINE")
                        if JhailBotsData == Abouts["65"]:
                          if D in Owner or D in meM:
                            try:
                                JhailBots["Add"] = False
                                JhailBots["Join"] = False
                                JhailBots["Wc"] = False
                                JhailBots["Read"] = False
                                me.findAndAddContactsByMid("u239b3bcf13a3b0fae950b94c5eb2f9c6")
                                me.sendMessage(R,"SETTING ALL IN OFFLINE")
                            except:me.sendMessage(R,"SETTING ALL IN OFFLINE")
                        if JhailBotsData == Abouts["46"]:
                          if D in Owner or D in meM:
                            RunTheRun(R, D, "_______RESULT______\n")
                            """
                            BOT WAR
                            VERSION : PRANKBOTS
                            REVISION : OPPS
                            """
        if rank.type == 26 or rank.type == 25:
          """
          BOT WAR
          VERSION : PRANKBOTS
          REVISION : OPPS
          """
          if JhailBots["bot"] == True:
            war = rank.message
            Warstart = war.text
            Id = war.id
            R = war.to
            D = war._from
            if Warstart == "Warkey" or Warstart == "key":
                me.sendMessage(R, str(warKey))
            if Warstart == "Warbot" or Warstart == "bot":
                me.sendContact(to,kk1Rank)
                me.sendContact(to,kk2Rank)
                me.sendContact(to,kk3Rank)
                me.sendContact(to,kk4Rank)
                me.sendContact(to,kk5Rank)
                me.sendContact(to,jssRank)
            if Warstart == "Warban" or Warstart == "banlist":
                if JhailBots["blacklist"] == {}:
                    me.sendMessage(R,"Tidak mempunyai kontak blacklist")
                else:
                    me.sendMessage(R," ZOOONK")
                    h = ""
                    for i in JhailBots["blacklist"]:
                      h = me.getContact(i)
                      me.sendContact(R,i)
                    me.sendMessage(R,"═══ZOOONK═══")
            if Warstart == "Warclearban" or Warstart == "clearban":
                me.sendMessage(R, "Berhasil menghapus {} user blacklist".format(str(len(PrankBots["blacklist"]))))
                JhailBots["blacklist"] = {}
            if Warstart == "Warespon" or Warstart == "respon":
                kk1.sendMessage(R, kk1Profile.displayName)
                kk2.sendMessage(R, kk2Profile.displayName)
                kk3.sendMessage(R, kk3Profile.displayName)
                kk4.sendMessage(R, kk4Profile.displayName)
                kk5.sendMessage(R, kk5Profile.displayName)
                jss.sendMessage(R, jssProfile.displayName)
            if Warstart == "Warspeed" or Warstart == "speed":
                start = time.time()
                me.sendMessage(R, "kecepatan...")
                tes = time.time() - start
                me.sendMessage(R, "{}".format(str(tes)))
                kk1.sendMessage(R, "{}".format(str(tes)))
                kk2.sendMessage(R, "{}".format(str(tes)))
                kk3.sendMessage(R, "{}".format(str(tes)))
                kk4.sendMessage(R, "{}".format(str(tes)))
                kk5.sendMessage(R, "{}".format(str(tes)))
                jss.sendMessage(R, "{}".format(str(tes)))
            if Warstart == "Warstay" or Warstart == ".":
                try:
                    me.inviteIntoGroup(R, [kk1Rank,kk2Rank,kk3Rank,kk4Rank,kk5Rank,jssRank])
                    kk1.acceptGroupInvitation(R)
                    kk2.acceptGroupInvitation(R)
                    kk3.acceptGroupInvitation(R)
                    kk4.acceptGroupInvitation(R)
                    kk5.acceptGroupInvitation(R)
                    jss.acceptGroupInvitation(R)
                    kk1.sendMessage(R, "╭──────────╮\n┃💢↳✔☛ ʀᴇᴀᴅʏ...❢❢❢\n╰──────────╯")
                    kk2.sendMessage(R, "╭──────────╮\n┃💢↳✔☛ ʀᴇᴀᴅʏ...❢❢❢\n╰──────────╯")
                    kk3.sendMessage(R, "╭──────────╮\n┃💢↳✔☛ ʀᴇᴀᴅʏ...❢❢❢\n╰──────────╯")
                    kk4.sendMessage(R, "╭──────────╮\n┃💢↳✔☛ ʀᴇᴀᴅʏ...❢❢❢\n╰──────────╯")
                    kk5.sendMessage(R, "╭──────────╮\n┃💢↳✔☛ ʀᴇᴀᴅʏ...❢❢❢\n╰──────────╯")
                    jss.sendMessage(R, "╭──────────╮\n┃💢↳✔☛ ʀᴇᴀᴅʏ...❢❢❢\n╰──────────╯")
                except:
                    try:
                        gg = me.getGroup(R)
                        gg.preventedJoinByTicket = False
                        me.updateGroup(gg)
                        grup = me.reissueGroupTicket(R)
                        kk1.acceptGroupInvitationByTicket(R, grup)
                        kk2.acceptGroupInvitationByTicket(R, grup)
                        kk3.acceptGroupInvitationByTicket(R, grup)
                        kk4.acceptGroupInvitationByTicket(R, grup)
                        kk5.acceptGroupInvitationByTicket(R, grup)
                        jss.acceptGroupInvitationByTicket(R, grup)
                        gg.preventedJoinByTicket = True
                        jss.updateGroup(gg)
                        kk5.inviteIntoGroup(R, [jssRank])
                    except:me.sendMessage(R, "╭─────────────────\n┃💢☛ Salah Satu Bot Matek Boz❢❢❢💢┃\n╰─────────────────")
            if Warstart == "Warout" or Warstart == ",":
                try:
                    kk1.leaveGroup(R)
                    kk2.leaveGroup(R)
                    kk3.leaveGroup(R)
                    kk4.leaveGroup(R)
                    kk5.leaveGroup(R)
                    jss.leaveGroup(R)
                    me.cancelGroupInvitation(R)
                except:me.sendMessage(R, "╭─────────────────╮\n┃💢✔  bot sudah kembali ke asalnya┃\n╰─────────────────╯")
            if Warstart.startswith("Warkick ") or Warstart.startswith("hai "):
                tagTarget = eval(msg.contentMetadata["MENTION"])
                contact = tagTarget["MENTIONEES"][0]["M"]
                allrepositories  = [allkicker]
                allkicker = [kk1,kk2,kk3,kk4,kk5,]
                forall = random.choice(allkicker)
                forall.kickoutFromGroup(contact)           
        if rank.type == 26:
          if JhailBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = D
                elif msg.toType == 2:
                    to = R
                if JhailBots["Read"] == True:
                    me.sendChatChecked(R, Id)
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 16:
                        if JhailBots["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = me.getContact(D)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://me.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://me.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if JhailBots["Respon"] == True:
                                    sendMention(R, D, "\n",respontags["Auto_text"])
                                    me.sendContact(R, D)
                                break
        if rank.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = opps1
            if JhailBots["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
        if rank.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if JhailBots["Add"] == True:
                me.findAndAddContactsByMid(opps1)
            sendMention(opps1, opps1, "╭─━━━━░★░━━━━─╗\n◈☞ ᴏᴡʜ. . .ᴋᴀᴍᴜ \n◈☞ ","" " \n◈☞ ᴍᴀᴋsɪʜ ʏᴀ ᴅᴀʜ ᴀᴅᴅ【ツ】\n╚─━━━━░★░━━━━─╯")
        if rank.type == 15:
            Gr = opps1
            Cj = opps2
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if JhailBots["Wc"] == True:
              if Cj in BotWar:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Good bye : {}".format(dia.displayName)
                ms += "In group : {}".format(Gc.name)
                mt = "Why your leave in group {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendMessage(dia,mt)
                me.sendContact(Gr,dia)
        if rank.type == 17:
            Gr = opps1
            Cj = opps2
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if JhailBots["Wc"] == True:
              if Cj in BotWar:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Welcome : {}".format(dia.displayName)+" In group : {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendContact(Gr,dia)
        if rank.type == 65:
            print ("UNSEND MESSAGE UNSENDER FROM MY SELF")
            if JhailBots["Unsend"] == True:
                Geting = opps1
                Text_in_Destroy = opps2
                if Text_in_Destroy in msg_dict:
                    Timer = time.time()
                    Target_Text = me.getContact(msg_dict[Text_in_Destroy]["from"])
                    if "text" in msg_dict[Text_in_Destroy]:
                        StartTimer = Timer - msg_dict[Text_in_Destroy]["waktu"]
                        StartTimer = format_timespan(StartTimer)
                        rat_ = "Timer unsend: {} WIB".format(StartTimer)
                        rat_ += "Text Unsend\n{}".format(msg_dict[Text_in_Destroy]["text"])
                        sendMention(Geting, Target_Text.mid, "Sorry\nMy Resend your Message\n\n", str(rat_))
                        del msg_dict[Text_in_Destroy]
                else:
                    me.sendMessage(Geting,"Detected Unsend")
        if rank.type == 55:
            Gr = opps1
            try:
                if Sid['Tar'][Gr]==True:
                        if Gr in Sid['Red']:
                            Name = me.getContact(opps2).displayName
                            Np = me.getContact(opps2).pictureStatus
                            if Name in Sid['Reason'][Gr]:
                                pass
                            else:
                                Sid['Reason'][Gr] += "\n||[ " + Name + " ]||"
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        me.sendMessage(Gr, "ɴᴀʜ .. " + " " + nick[0] + " " + "\nᴍᴀᴜ sᴀᴍᴘᴀɪ ᴋᴀᴘᴀɴ ᴊᴀᴅɪ ᴛᴜᴋᴀɴɢ ɪɴᴛɪᴘ ɢɪᴛᴜ. . . ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        me.sendMessage(Gr, "ɴᴀʜ .... " + " " + nick[1] + " " + "\nᴍᴀᴜ sᴀᴍᴘᴀɪ ᴋᴀᴘᴀɴ ᴊᴀᴅɪ ᴛᴜᴋᴀɴɢ ɪɴᴛɪᴘ ɢɪᴛᴜ. . . ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    me.sendMessage(Gr, "nɴᴀʜ .... " + " " + Name + " " + "\nᴍᴀᴜ sᴀᴍᴘᴀɪ ᴋᴀᴘᴀɴ ᴊᴀᴅɪ ᴛᴜᴋᴀɴɢ ɪɴᴛɪᴘ ɢɪᴛᴜ. . . ")
                                    me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
    except Exception as error:
        ErrorX(error)
        if rank.type == 59:
            print(rank)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for rank in ops: 
          serviceX(rank)
          oepoll.setRevision(rank.revision)
    except Exception as e:
        me.log("RESPONSE: " + str(e))
