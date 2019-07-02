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
_session = requests.session()
botStart = time.time()
settingsOpen = codecs.open("JhailBots.json","r","utf-8")
JhailBots = json.load(settingsOpen)
Helps = codecs.open("Menu.json","r","utf-8")
Menu = json.load(Helps)
#========================================================================
#========================================================================
print("\n               [SB]")
me = LINE("u9fa5bf27b50f5adf00c81bc3e987fbfc:aWF0OiAxNTYxMjI3MjA5OTU4Cg==..8viWFSvfvLoTbtQYREiHgXBdZPw=")
me.log("Auth Token : " + str(me.authToken))
meProfile = me.getProfile()
meSettings = me.getSettings()
meM = meProfile.mid
print("\n              [kicker1]")
kk1 = LINE("udce6192af460cbf7171cb763b15b679e:aWF0OiAxNTYxMjI2MjQ5NDM2Cg==..Tr/+mONMSSUU8zTCFCYUXIucUDI=")
kk1.log("Auth Token : " + str(kk1.authToken))
kk1Profile = kk1.getProfile()
Jhail1 = kk1Profile.mid
print("\n             [Kicker2]")
kk2 = LINE("u4ed3a529523b48bed97386c2e378f29b:aWF0OiAxNTYxMjI2Njk0Mjg3Cg==..LjvAwEu7Io9X6ZV2mqAT6DDiKn0=")
kk2.log(" Auth Token : " + str(kk2.authToken))
kk2Profile = kk2.getProfile()
Jhail2 = kk2Profile.mid
print("\n              [Kicker3]")
kk3 = LINE("ua12b91d3c5bf4558712e58bb5ffe1579:aWF0OiAxNTYxMjE0MjMxODMxCg==..2tLOyWcTw/5vKqOlc4fBXK5I9YE=")
kk3.log("Auth Token : " + str(kk3.authToken))
kk3Profile = kk3.getProfile()
Jhail3 = kk3Profile.mid
print("\n              [Kicker4]")
kk4 = LINE("u5d4bd0bdc01579423b4a1765b0edfa7f:aWF0OiAxNTYxMjI3MDY0MDEwCg==..YquUbEYCD9AF2fX4Q6+x8m/Hbi4=")
kk4.log("Auth Token : " + str(kk4.authToken))
kk4Profile = kk4.getProfile()
Jhail4 = kk4Profile.mid
print("\n              [Kicker5]")
kk5 = LINE("uc71d77981ebb88256c352d953529d7d3:aWF0OiAxNTYxMjI4MDE1MjY2Cg==..a0FKxpg2vpfuSBH7+xrdm86cVZc=")
kk5.log("Auth Token : " + str(kk5.authToken))
kk5Profile = kk5.getProfile()
Jhail5 = kk5Profile.mid
print("\n              [ANTI JS]")
jss = LINE("u2e931538f06df380bfb327a552531d61:aWF0OiAxNTYxMjI3ODc2NjU3Cg==..YZWDr/gt5KAyQe3l0LnUID02NxY=")
jss.log("Auth Token : " + str(jss.authToken))
jssProfile = jss.getProfile()
Antijs = jssProfile.mid
print("\n=================================================================")
print("ʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2")
print("ʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2")
print("     ᴄʀᴇᴀᴛᴏʀ\n       ʙʏ\n     ⪃⪄")
print("ʙᴏᴛs.ᴠᴇʀsɪᴏɴ ʙᴏᴛᴡᴀʀ")
print("=================================================================")
oepoll = OEPoll(me)
call = me
Admin = JhailBots["MID"]
Owner = ["u945e817cbdb14360333950f3ff5b06a1"]
Stiles = "│○⪃⪄☠⇉"
JhailWars = [meM,Jhail1,Jhail2,Jhail3,Jhail4,Jhail5,Antijs]
Jhail = [me,kk1,kk2,kk3,kk4,kk5,jss]
msg_dict = {}
msg_dict1 = {}
pro = {
    "Pintu": [],
    "Pembunuh": [],
    "Maling": [],
    "Penghasut": [],
    "Pencuri": [],
    "Penyelamat": [],
    "Kuntilanak": []
}
respontags = {
    "Auto_text": "╔⪨⪩┅༐┅͜͡❇║ᴊʜᴀɪʟʙᴏᴛs ║❇͜͡┅༐┅⪨⪩	    \n║✍círí círí σrαng kєѕєpíαn✍\n╠⪨⪩1 ѕukα tαg gα jєlαѕ\n╠⪨⪩2 ѕєlαlu cαrí pєrhαtíαn\n╠⪨⪩3 σrαng nчα nчєвєlín\n║  ﷽⪃⪄⫹⫺⫷⫸⫹⫺⪃⪄﷽\n╚⪨⪩┅༐┅͜͡❇║ᴊʜᴀɪʟʙᴏᴛs ║❇͜͡┅༐┅⪨⪩",
    "Auto_pM": "⪨⪩┅༐┅͜͡❇║ᴊʜᴀɪʟʙᴏᴛs║❇͜͡┅༐┅⪨⪩\n\n       иαмα кυ ∂ ¢євυт мυℓυ\n\n⪨⪩┅༐┅͜͡❇║ᴊʜᴀɪʟʙᴏᴛs ║❇͜͡┅༐┅⪨⪩"
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
Line_Apikey = "u133f7110dd00e635f0776957837055a2"
Extr = meProfile.displayName
Import_Server = ["u945e817cbdb14360333950f3ff5b06a1"]
for Allbots in Jhail:
    for LineX in Import_Server:
        try:
            Allbots.findAndAddContactsByMid(LineX)
        except:pass
    for botKickers in JhailWars:
        try:
            Allbots.findAndAddContactsByMid(botKickers)
        except:pass
def backupData():
    try:
        backup = JhailBots
        f = codecs.open('JhailBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Menu
        f = codecs.open('Menu.json','w','utf-8')
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
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@JhailBots \n"
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
Devert = "Terimakasih kang\nsaya "+cont.displayName+" Login Botmu"
def Run_Xx():
    print ("BOT KEMBALI AKTIF")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
mulai = time.time()
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(meM).statusMessage if me.getContact(meM).statusMessage != '' else 'creator By meMots |ID LINE|\njhail_id', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(meM).displayName,}
    return me.sendMessage(to, me.getContact(meM).displayName, contentMetadata, 19)
def ErrorX(text):
    me.log("data: " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@JhailBots \n"
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
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    me.sendMessage(to, '', contentMetadata, 7)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@JhailBots "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ErrorX(error)
        me.sendMessage(to, "Error\n\n" + str(error))
extras = Extr+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@JhailBots \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2019,5,31)
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
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nJhail_TEAM. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
def attck(grup, target):
    try:
        asd= kk1.kickoutFromGroup(grup, [target])
        asd= kk1.cancelGroupInvitation(grup, [target])
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kk2.kickoutFromGroup(grup, [target])
            asd= kk2.cancelGroupInvitation(grup, [target])
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kk3.kickoutFromGroup(grup, [target])
                asd= kk3.cancelGroupInvitation(grup, [target])
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kk4.kickoutFromGroup(grup, [target])
                    asd= kk4.cancelGroupInvitation(grup, [target])
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= kk5.kickoutFromGroup(grup, [target])
                        asd= kk5.cancelGroupInvitation(grup, [target])
                        if asd != None:
                            mbutfaild
                    except:
                        pass

def ajs(grup, target):
    print("DEP JS KICK MUSUH")
    try:
        asd= jss.acceptGroupInvitation(grup)
        asd= jss.kickoutFromGroup(grup, [op.param2])
        asd= jss.inviteIntoGroup(grup, InexWars)
        if asd != None:
            mbutfaild
    except:
        try:
            asd= jss.acceptGroupInvitation(grup)
            asd= jss.inviteIntoGroup(grup, InexWars)
            asd= jss.kickoutFromGroup(grup, [op.param2])
            if asd != None:
                mbutfaild
        except:
            pass

def cancel(grup, target):
    try:
        asd= kk1.cancelGroupInvitation(grup, [target])
        if asd != None:
            mbutfail
    except:
        try:
            asd= kk2.cancelGroupInvitation(grup, [target])
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kk3.cancelGroupInvitation(grup, [target])
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kk4.cancelGroupInvitation(grup, [target])
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= kk5.cancelGroupInvitation(grup, [target])
                        if asd != None:
                            mbutfaild
                    except:
                        pass

def lockqr(grup):
    G = kk1.getGroup(grup)
    G.preventedJoinByTicket = True
    try:
        asd= kk1.updateGroup(G)
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kk2.updateGroup(G)
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kk3.updateGroup(G)
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kk4.updateGroup(G)
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= kk5.updateGroup(G)
                        if asd != None:
                            mbutfaild
                    except:
                        pass

def invt(grup, target):
    try:
        asd= kk1.inviteIntoGroup(grup, [target])
        asd= me.acceptGroupInvitation(grup)
        asd= kk2.acceptGroupInvitation(grup)
        asd= kk3.acceptGroupInvitation(grup)
        asd= kk4.acceptGroupInvitation(grup)
        asd= kk5.acceptGroupInvitation(grup)
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kk2.inviteIntoGroup(grup, [target])
            asd= kk3.acceptGroupInvitation(grup)
            asd= kk4.acceptGroupInvitation(grup)
            asd= kk5.acceptGroupInvitation(grup)
            asd= me.acceptGroupInvitation(grup)
            asd= kk1.acceptGroupInvitation(grup)
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kk3.inviteIntoGroup(grup, [target])
                asd= kk4.acceptGroupInvitation(grup)
                asd= kk5.acceptGroupInvitation(grup)
                asd= me.acceptGroupInvitation(grup)
                asd= kk1.acceptGroupInvitation(grup)
                asd= kk2.acceptGroupInvitation(grup)
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kk4.inviteIntoGroup(grup, [target])
                    asd= kk5.acceptGroupInvitation(grup)
                    asd= me.acceptGroupInvitation(grup)
                    asd= kk1.acceptGroupInvitation(grup)
                    asd= kk2.acceptGroupInvitation(grup)
                    asd= kk3.acceptGroupInvitation(grup)
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= kk5.inviteIntoGroup(grup, [target])
                        asd= me.acceptGroupInvitation(grup)
                        asd= kk1.acceptGroupInvitation(grup)
                        asd= kk2.acceptGroupInvitation(grup)
                        asd= kk3.acceptGroupInvitation(grup)
                        asd= kk4.acceptGroupInvitation(grup)
                        if asd != None:
                            mbutfaild
                    except:
                        pass

def backp(grup, target):
    try:
        kk1.inviteIntoGroup(grup, [target])
        if target == JhailWars:
            me.acceptGroupInvitation(grup)
            kk2.acceptGroupInvitation(grup)
            kk2.kickoutFromGroup(grup, [rank.param2])
            kk3.acceptGroupInvitation(grup)
            kk3.kickoutFromGroup(grup, [rank.param2])
            kk4.acceptGroupInvitation(grup)
            kk4.kickoutFromGroup(grup, [rank.param2])
            kk5.acceptGroupInvitation(grup)
            kk5.kickoutFromGroup(grup, [rank.param2])
    except:
        try:
            kk2.inviteIntoGroup(grup, [target])
            if target == JhailWars:
                me.acceptGroupInvitation(grup)
                kk1.acceptGroupInvitation(grup)
                kk1.kickoutFromGroup(grup, [rank.param2])
                kk3.acceptGroupInvitation(grup)
                kk3.kickoutFromGroup(grup, [rank.param2])
                kk4.acceptGroupInvitation(grup)
                kk4.kickoutFromGroup(grup, [rank.param2])
                kk5.acceptGroupInvitation(grup)
                kk5.kickoutFromGroup(grup, [rank.param2])
        except:
            try:
                k3.inviteIntoGroup(grup, [target])
                if target == JhailWars:
                    me.acceptGroupInvitation(grup)
                    kk1.acceptGroupInvitation(grup)
                    kk1.kickoutFromGroup(grup, [rank.param2])
                    kk2.acceptGroupInvitation(grup)
                    kk2.kickoutFromGroup(grup, [rank.param2])
                    kk4.acceptGroupInvitation(grup)
                    kk4.kickoutFromGroup(grup, [rank.param2])
                    kk5.acceptGroupInvitation(grup)
                    kk5.kickoutFromGroup(grup, [rank.param2])
            except:
                try:
                    kk4.inviteIntoGroup(grup, [target])
                    if target == JhailWars:
                        me.acceptGroupInvitation(grup)
                        kk1.acceptGroupInvitation(grup)
                        kk1.kickoutFromGroup(grup, [rank.param2])
                        kk2.acceptGroupInvitation(grup)
                        kk2.kickoutFromGroup(grup, [rank.param2])
                        kk3.acceptGroupInvitation(grup)
                        kk3.kickoutFromGroup(grup, [rank.param2])
                        kk5.acceptGroupInvitation(grup)
                        kk5.kickoutFromGroup(grup, [rank.param2])
                except:
                    try:
                        kk5.inviteIntoGroup(grup, [target])
                        if target == JhailWars:
                            me.acceptGroupInvitation(grup)
                            kk1.acceptGroupInvitation(grup)
                            kk1.kickoutFromGroup(grup, [rank.param2])
                            kk2.acceptGroupInvitation(grup)
                            kk2.kickoutFromGroup(grup, [rank.param2])
                            kk3.acceptGroupInvitation(grup)
                            kk3.kickoutFromGroup(grup, [rank.param2])
                            kk4.acceptGroupInvitation(grup)
                            kk4.kickoutFromGroup(grup, [rank.param2])
                    except:
                        pass

def black(target):
    if rank.param2 in JhailBots["blacklist"]:
        ["blacklist"].append(target)
warKey = """   ➢ ᴍᴇɴᴜ
╭━────────────━╮
│➢ ᴛᴀɢ
│➢ ᴘɪɴɢ
│➢ ᴄᴇᴋ
│➢ ᴍʏʙᴏᴛ
│➢ ᴘᴍ ᴏɴ/ᴏғғ
│➢ sᴘᴇᴇᴅ-sᴘ
│➢ ᴋᴇʟᴜᴀʀ(,)
│➢ ᴍᴀsᴜᴋ(.)
│➢ sᴏʀʏ @
│➢ ᴀᴅᴍɪɴᴀᴅᴅ @
│➢ ᴀᴅᴍɪɴᴅᴇʟʟ @
│➢ ʀᴇᴍᴏᴠᴇ ᴄʜᴀᴛ
│➢ ʙᴏᴛ ᴘɪᴄᴛ
│➢ ʙᴏᴛɴᴀᴍᴇ
│➢ ᴘʀᴏ ᴏɴ/ᴏғғ
│➢ ᴊs ɪɴ-ᴏᴜᴛ
│➢ sᴛᴀʏ - sᴛᴀɴʙᴀʏ
│➢ ᴍᴀᴀғ [ᴅɪsᴘʟᴀʏɴᴀᴍᴇ]
╰━────────────━╯
   ━──[ ᴊʜᴀɪʟʙᴏᴛs ]──━
      ᴠᴇʀsɪ ᴘʀᴏᴛᴇᴄᴛᴡᴀʀ"""
def SqL_R(text):
    R_SQL = text.lower()
    if JhailBots["key"] == True:
        if R_SQL.startswith(JhailBots["text"]):
            JhailBotsList = R_SQL.replace(JhailBots["text"],"")
        else:
            JhailBotsList = "Undefined command"
    else:
        JhailBotsList = text.lower()
    return JhailBotsList
def serviceX(rank):
    global groupParam
    Rumahku = rank.param1
    Musuhku = rank.param2
    Temanku = rank.param3
    try:
        if rank.type == 11:
          if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
            if Musuhku in JhailBots["blacklist"]:
                t1 = Thread(target=attck, args=(Rumahku, Musuhku))
                t1.start()
                t2 = Thread(target=lockqr, args=(Rumahku,))
                t2.start()
                t3 = Thread(target=black, args=(Musuhku,))
                t3.start()
                t30 = Thread(target=ajs, args=(Rumahku,Musuhku))
                t30.start()

        if rank.type == 17:
          if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
            if Musuhku in JhailBots["blacklist"]:
                t4 = Thread(target=attck, args=(Rumahku, Musuhku))
                t4.start()
                t5 = Thread(target=lockqr, args=(Rumahku,))
                t5.start()
            if Musuhku in JhailBots["blacklist"]:
                t6 = Thread(target=attck, args=(Rumahku, Musuhku))
                t6.start()
        if rank.type == 13:
          if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
            if Musuhku in JhailBots["blacklist"]:
                t7 = Thread(target=attck, args=(Rumahku, Musuhku))
                t7.start()
                t8 = Thread(target=cancl, args=(Rumahku, Temanku))
                t8.start()
                t9 = Thread(target=black, args=(Musuhku,))
                t9.start()
        if rank.type == 19 or rank.type == 32:
            if Temanku in JhailWars:
                JhailBots["blacklist"][Musuhku] = True
                t10 = Thread(target=attck, args=(Rumahku, Musuhku))
                t10.start()
                t11 = Thread(target=black, args=(Musuhku,))
                t11.start()
                t110 = Thread(target=ajs, args=(Rumahku, Musuhku,))
                t110.start()

            if Temanku in JhailWars:
                t12 = Thread(target=backp, args=(Rumahku, Temanku))
                t12.start()
        if rank.type == 32:
            if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                JhailBots["blacklist"][Musuhku] = True
                t13 = Thread(target=attck, args=(Rumahku, Musuhku))
                t13.start()
                t14 = Thread(target=black, args=(Musuhku,))
                t14.start()
                t140 = Thread(target=ajs, args=(Rumahku, Musuhku,))
                t140.start()
        if rank.type == 0:
            return
        if rank.type == 11:
            if Rumahku in pro["Pintu"]:
                try:
                    if kk1.getGroup(Rumahku).preventedJoinByTicket == False:
                        if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                            kk1.reissueGroupTicket(Rumahku)
                            X = kk1.getGroup(Rumahku)
                            X.preventedJoinByTicket = True
                            kk1.updateGroup(X)
                            kk1.kickoutFromGroup(Rumahku,[Musuhku])
                except:
                    try:
                        if kk2.getGroup(Rumahku).preventedJoinByTicket == False:
                            if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                                kk2.reissueGroupTicket(Rumahku)
                                X = kk2.getGroup(Rumahku)
                                X.preventedJoinByTicket = True
                                kk2.updateGroup(X)
                                kk2.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            if kk3.getGroup(Rumahku).preventedJoinByTicket == False:
                                if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                                    kk3.reissueGroupTicket(Rumahku)
                                    X = kk3.getGroup(Rumahku)
                                    X.preventedJoinByTicket = True
                                    kk3.updateGroup(X)
                                    kk3.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                if kk4.getGroup(Rumahku).preventedJoinByTicket == False:
                                    if Musuhku not in Wars and Musuhku not in Owner and Musuhku not in meM:
                                        kk4.reissueGroupTicket(Rumahku)
                                        X = kk4.getGroup(Rumahku)
                                        X.preventedJoinByTicket = True
                                        kk4.updateGroup(X)
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    if kk5.getGroup(Rumahku).preventedJoinByTicket == False:
                                        if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                                            kk5.reissueGroupTicket(Rumahku)
                                            X = kk5.getGroup(Rumahku)
                                            X.preventedJoinByTicket = True
                                            kk5.updateGroup(X)
                                            kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        if me.getGroup(Rumahku).preventedJoinByTicket == False:
                                            if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                                                Z = me.getGroup(Rumahku)
                                                Z.preventedJoinByTicket = False
                                                Terbuka = me.reissueGroupTicket(Rumahku)
                                                jss.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                                X = jss.getGroup(Rumahku)
                                                X.preventedJoinByTicket = True
                                                jss.updateGroup(X)
                                                jss.sendMessage(Rumahku, "Jangan mainan Qr")
                                                jss.kickoutFromGroup(Rumahku,[Musuhku])
                                                jss.leaveGroup(Rumahku)
                                                me.inviteIntoGroup(Rumahku,[Antijs])
                                    except:
                                        pass
        if rank.type == 19:
            if Rumahku in pro["Pembunuh"]:
                if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                    JhailBots["blacklist"][Musuhku] = True
                    random.choice(Jaka).kickoutFromGroup(Rumahku,[Musuhku])
                else:
                    pass

        if rank.type == 19:
            try:
                if Rumahku in pro["Kuntilanak"]:
                    if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                        G = me.getGroup(Rumahku)
                        G.preventedJoinByTicket = False
                        me.updateGroup(G)
                        invsend = 0
                        Terbuka = me.reissueGroupTicket(Rumahku)
                        jss.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
                        jss.leaveGroup(Rumahku)
                        X = me.getGroup(Rumahku)
                        X.preventedJoinByTicket = True
                        me.updateGroup(X)
            except:
                pass             
                
        if rank.type == 19:
            if Rumahku in pro["Penyelamat"]:
                try:
                  if Temanku in meM:
                    if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                        jss.acceptGroupInvitation(Rumahku)
                        G = jss.getGroup(Rumahku)
                        G.preventedJoinByTicket = False
                        jss.updateGroup(G)
                        Terbuka = jss.reissueGroupTicket(Rumahku)
                        me.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        kk1.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        kk2.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        kk3.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        kk4.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        kk5.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
                        G.preventedJoinByTicket = True
                        jss.updateGroup(G)
                        InexBots["blacklist"][Musuhku] = True
                        jss.leaveGroup(Rumahku)
                        me.inviteIntoGroup(Rumahku,[Antijs])
                        me.inviteIntoGroup(Rumahku,[Owner])
                except:
                    pass
        if rank.type == 32:
            if Rumahku in pro["Pencuri"]:
                if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        if Temanku not in JhailBots["blacklist"]:
                            kk1.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            if Temanku not in JhailBots["blacklist"]:
                                kk2.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                if Temanku not in JhailBots["blacklist"]:
                                    kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    if Temanku not in JhailBots["blacklist"]:
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        if Temanku not in JhailBots["blacklist"]:
                                            kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    except:pass
                return
        if rank.type == 13:
            if Rumahku in pro["Penghasut"]:
                if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        if Temanku not in JhailBots["blacklist"]:
                            group = kk1.getGroup(Rumahku)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                kk1.cancelGroupInvitation(Rumahku,[_mid])
                                kk1.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            if Temanku not in JhailBots["blacklist"]:
                                group = kk2.getGroup(Rumahku)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk2.cancelGroupInvitation(Rumahku,[_mid])
                                    kk2.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                if Temanku not in JhailBots["blacklist"]:
                                    group = kk3.getGroup(Rumahku)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kk3.cancelGroupInvitation(Rumahku,[_mid])
                                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    if Temanku not in JhailBots["blacklist"]:
                                        group = kk4.getGroup(Rumahku)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kk4.cancelGroupInvitation(Rumahku,[_mid])
                                            kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        if Temanku not in JhailBots["blacklist"]:
                                            group = kk5.getGroup(Rumahku)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                kk5.cancelGroupInvitation(Rumahku,[_mid])
                                                kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    except:
                                        pass

        if rank.type == 17:
            if Rumahku in pro["Maling"]:
                if Musuhku not in JhailWars and Musuhku not in Owner and Musuhku not in meM:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        if Temanku not in JhailBots["blacklist"]:
                        	kk5.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            if Temanku not in JhailBots["blacklist"]:
                                kk4.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                if Temanku not in JhailBots["blacklist"]:
                                    kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    if Temanku not in JhailBots["blacklist"]:
                                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        if Temanku not in JhailBots["blacklist"]:
                                            kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                    except:
                                        pass
                return

        if rank.type == 19 or rank.type == 32:
            if meM in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk1.inviteIntoGroup(Rumahku,[Temanku])
                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                        me.acceptGroupInvitation(Rumahku)
                    except:
                        try:
                            kk2.inviteIntoGroup(Rumahku,[Temanku])
                            kk2.kickoutFromGroup(Rumahku,[Musuhku])
                            me.acceptGroupInvitation(Rumahku)
                        except:
                            try:
                                kk3.inviteIntoGroup(Rumahku,[Temanku])
                                kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                me.acceptGroupInvitation(Rumahku)
                            except:
                                try:
                                    kk4.inviteIntoGroup(Rumahku,[Temanku])
                                    kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                    me.acceptGroupInvitation(Rumahku)
                                except:
                                    try:
                                        kk5.inviteIntoGroup(Rumahku,[Temanku])
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                        me.acceptGroupInvitation(Rumahku)
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(Rumahku)
                                            jss.inviteIntoGroup(Rumahku, JhailWars)
                                            me.acceptGroupInvitation(Rumahku)
                                            kk1.acceptGroupInvitation(Rumahku)
                                            kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                            kk2.acceptGroupInvitation(Rumahku)
                                            kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                            kk3.acceptGroupInvitation(Rumahku)
                                            kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                            kk4.acceptGroupInvitation(Rumahku)
                                            kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                            kk5.acceptGroupInvitation(Rumahku)
                                            kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                            jss.leaveGroup(Rumahku)
                                            kk1.inviteIntoGroup(Rumahku,[Antijs])
                                        except:pass

        if rank.type == 19 or rank.type == 32:
            if Jhail1 in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk2.inviteIntoGroup(Rumahku,[Temanku])
                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                        kk1.acceptGroupInvitation(Rumahku)
                    except:
                        try:
                            kk3.inviteIntoGroup(Rumahku,[Temanku])
                            kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            kk1.acceptGroupInvitation(Rumahku)
                        except:
                            try:
                                kk4.inviteIntoGroup(Rumahku,[Temanku])
                                kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                kk1.acceptGroupInvitation(Rumahku)
                            except:
                                try:
                                    kk5.inviteIntoGroup(Rumahku,[Temanku])
                                    kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    kk1.acceptGroupInvitation(Rumahku)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(Rumahku)
                                        jss.inviteIntoGroup(Rumahku, JhailWars)
                                        me.acceptGroupInvitation(Rumahku)
                                        kk1.acceptGroupInvitation(Rumahku)
                                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk2.acceptGroupInvitation(Rumahku)
                                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk3.acceptGroupInvitation(Rumahku)
                                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk4.acceptGroupInvitation(Rumahku)
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk5.acceptGroupInvitation(Rumahku)
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                        jss.leaveGroup(Rumahku)
                                        kk2.inviteIntoGroup(Rumahku,[Antijs])
                                    except:pass

        if rank.type == 19 or rank.type == 32:
            if Jhail2 in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk3.inviteIntoGroup(Rumahku,[Temanku])
                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                        kk2.acceptGroupInvitation(Rumahku)
                    except:
                        try:
                            kk4.inviteIntoGroup(Rumahku,[Temanku])
                            kk4.kickoutFromGroup(Rumahku,[Musuhku])
                            kk2.acceptGroupInvitation(Rumahku)
                        except:
                            try:
                                kk5.inviteIntoGroup(Rumahku,[Temanku])
                                kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                kk2.acceptGroupInvitation(Rumahku)
                            except:
                                try:
                                    kk1.inviteIntoGroup(Rumahku,[Temanku])
                                    kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                    kk2.acceptGroupInvitation(Rumahku)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(Rumahku)
                                        jss.inviteIntoGroup(Rumahku, JhailWars)
                                        me.acceptGroupInvitation(Rumahku)
                                        kk1.acceptGroupInvitation(Rumahku)
                                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk2.acceptGroupInvitation(Rumahku)
                                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk3.acceptGroupInvitation(Rumahku)
                                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk4.acceptGroupInvitation(Rumahku)
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk5.acceptGroupInvitation(Rumahku)
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                        jss.leaveGroup(Rumahku)
                                        kk3.inviteIntoGroup(Rumahku,[Antijs])
                                    except:pass

        if rank.type == 19 or rank.type == 32:
            if Jhail3 in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk4.inviteIntoGroup(Rumahku,[Temanku])
                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                        kk3.acceptGroupInvitation(Rumahku)
                    except:
                        try:
                            kk5.inviteIntoGroup(Rumahku,[Temanku])
                            kk5.kickoutFromGroup(Rumahku,[Musuhku])
                            kk3.acceptGroupInvitation(Rumahku)
                        except:
                            try:
                                kk1.inviteIntoGroup(Rumahku,[Temanku])
                                kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                kk3.acceptGroupInvitation(Rumahku)
                            except:
                                try:
                                    kk2.inviteIntoGroup(Rumahku,[Temanku])
                                    kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                    kk3.acceptGroupInvitation(Rumahku)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(Rumahku)
                                        jss.inviteIntoGroup(Rumahku, JhailWars)
                                        me.acceptGroupInvitation(Rumahku)
                                        kk1.acceptGroupInvitation(Rumahku)
                                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk2.acceptGroupInvitation(Rumahku)
                                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk3.acceptGroupInvitation(Rumahku)
                                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk4.acceptGroupInvitation(Rumahku)
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk5.acceptGroupInvitation(Rumahku)
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                        jss.leaveGroup(Rumahku)
                                        kk4.inviteIntoGroup(Rumahku,[Antijs])
                                    except:pass

        if rank.type == 19 or rank.type == 32:
            if Jhail4 in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk5.inviteIntoGroup(Rumahku,[Temanku])
                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                        kk4.acceptGroupInvitation(Rumahku)
                    except:
                        try:
                            kk1.inviteIntoGroup(Rumahku,[Temanku])
                            kk1.kickoutFromGroup(Rumahku,[Musuhku])
                            kk4.acceptGroupInvitation(Rumahku)
                        except:
                            try:
                                kk2.inviteIntoGroup(Rumahku,[Temanku])
                                kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                kk4.acceptGroupInvitation(Rumahku)
                            except:
                                try:
                                    kk3.inviteIntoGroup(Rumahku,[Temanku])
                                    kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                    kk4.acceptGroupInvitation(Rumahku)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(Rumahku)
                                        jss.inviteIntoGroup(Rumahku, JhailWars)
                                        me.acceptGroupInvitation(Rumahku)
                                        kk1.acceptGroupInvitation(Rumahku)
                                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk2.acceptGroupInvitation(Rumahku)
                                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk3.acceptGroupInvitation(Rumahku)
                                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk4.acceptGroupInvitation(Rumahku)
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk5.acceptGroupInvitation(Rumahku)
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                        jss.leaveGroup(Rumahku)
                                        kk5.inviteIntoGroup(Rumahku,[Antijs])
                                    except:pass

        if rank.type == 19 or rank.type == 32:
            if Jhail5 in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk1.inviteIntoGroup(Rumahku,[Temanku])
                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                        kk5.acceptGroupInvitation(Rumahku)
                    except:
                        try:
                            kk2.inviteIntoGroup(Rumahku,[Temanku])
                            kk2.kickoutFromGroup(Rumahku,[Musuhku])
                            kk5.acceptGroupInvitation(Rumahku)
                        except:
                            try:
                                kk3.inviteIntoGroup(Rumahku,[Temanku])
                                kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                kk5.acceptGroupInvitation(Rumahku)
                            except:
                                try:
                                    kk4.inviteIntoGroup(Rumahku,[Temanku])
                                    kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                    kk5.acceptGroupInvitation(Rumahku)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(Rumahku)
                                        jss.inviteIntoGroup(Rumahku, JhailWars)
                                        me.acceptGroupInvitation(Rumahku)
                                        kk1.acceptGroupInvitation(Rumahku)
                                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk2.acceptGroupInvitation(Rumahku)
                                        kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk3.acceptGroupInvitation(Rumahku)
                                        kk3.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk4.acceptGroupInvitation(Rumahku)
                                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                        kk5.acceptGroupInvitation(Rumahku)
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                        jss.leaveGroup(Rumahku)
                                        kk1.inviteIntoGroup(Rumahku,[Antijs])
                                    except:pass

        if rank.type == 19 or rank.type == 32:
            if Antijs in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk1.inviteIntoGroup(Rumahku,[Antijs])
                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            kk2.inviteIntoGroup(Rumahku,[Antijs])
                            kk2.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                kk3.inviteIntoGroup(Rumahku,[Antijs])
                                kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    kk4.inviteIntoGroup(Rumahku,[Antijs])
                                    kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        kk5.inviteIntoGroup(Rumahku,[Antijs])
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    except:
                                        try:
                                            Z = me.getGroup(Rumahku)
                                            Z.preventedJoinByTicket = False
                                            Terbuka = me.reissueGroupTicket(Rumahku)
                                            kk1.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                            kk2.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                            kk3.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                            kk4.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                            kk5.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                            jss.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                                            X = jss.getGroup(Rumahku)
                                            X.preventedJoinByTicket = True
                                            jss.updateGroup(X)
                                            jss.sendMessage(Rumahku, "Duooobol!")
                                            jss.kickoutFromGroup(Rumahku,[Musuhku])
                                            jss.leaveGroup(Rumahku)
                                            kk.inviteIntoGroup(Rumahku,[Antijs])
                                        except:pass

        if rank.type == 19 or rank.type == 32:
            if Owner in Temanku:
                if Musuhku in JhailWars:
                    pass
                else:
                    JhailBots["blacklist"][Musuhku] = True
                    try:
                        kk1.findAndAddContactsByMid(Rumahku,Owner)
                        kk1.inviteIntoGroup(Rumahku,Owner)
                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            kk2.findAndAddContactsByMid(Rumahku,Owner)
                            kk2.inviteIntoGroup(Rumahku,Owner)
                            kk2.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                kk3.findAndAddContactsByMid(Rumahku,Owner)
                                kk3.inviteIntoGroup(Rumahku,Owner)
                                kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    kk4.findAndAddContactsByMid(Rumahku,Owner)
                                    kk4.inviteIntoGroup(Rumahku,Owner)
                                    kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        kk5.findAndAddContactsByMid(Rumahku,Owner)
                                        kk5.inviteIntoGroup(Rumahku,Owner)
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    except:
                                        try:
                                            jss.acceptGroupInvitation(Rumahku)
                                            jss.inviteIntoGroup(Rumahku,JhailWars)
                                            jss.kickoutFromGroup(Rumahku,[Musuhku])
                                            kk1.acceptGroupInvitation(Rumahku)
                                            kk2.acceptGroupInvitation(Rumahku)
                                            kk3.acceptGroupInvitation(Rumahku)
                                            kk4.acceptGroupInvitation(Rumahku)
                                            kk5.acceptGroupInvitation(Rumahku)
                                            jss.leaveGroup(Rumahku)
                                            me.inviteIntoGroup(Rumahku,[Antijs])
                                            me.findAndAddContactsByMid(Owner)
                                            me.inviteIntoGroup(Rumahku,[Owner])
                                        except:pass

        if rank.type == 17:
            if Musuhku in JhailBots["blacklist"]:
                if Musuhku not in Owner and Musuhku not in meM:
                    try:
                        kk1.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        try:
                            kk2.kickoutFromGroup(Rumahku,[Musuhku])
                        except:
                            try:
                                kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            except:
                                try:
                                    kk4.kickoutFromGroup(Rumahku,[Musuhku])
                                except:
                                    try:
                                        kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    except:
                                        jss.kickoutFromGroup(Rumahku,[Musuhku])
            else:pass
        if rank.type == 13:
            if Musuhku in JhailBots["blacklist"]:
                if Temanku not in Owner and Temanku not in meM:
                    try:
                        kk5.cancelGroupInvitation(Rumahku,[Temanku])
                    except:
                        try:
                            kk4.cancelGroupInvitation(Rumahku,[Temanku])
                        except:
                            try:
                                kk3.cancelGroupInvitation(Rumahku,[Temanku])
                            except:
                                try:
                                    kk2.cancelGroupInvitation(Rumahku,[Temanku])
                                except:
                                    kk1.cancelGroupInvitation(Rumahku,[Temanku])
            if Temanku in JhailBots["blacklist"]:
                if Musuhku not in Owner and Musuhku not in meM:
                    try:
                        kk5.cancelGroupInvitation(Rumahku,[Temanku])
                    except:
                        try:
                            kk4.cancelGroupInvitation(Rumahku,[Temanku])
                        except:
                            try:
                                kk3.cancelGroupInvitation(Rumahku,[Temanku])
                            except:
                                try:
                                    kk2.cancelGroupInvitation(Rumahku,[Temanku])
                                except:
                                    kk1.cancelGroupInvitation(Rumahku,[Temanku])
                else:pass
            if Temanku in JhailBots["blacklist"]:
                if Musuhku not in Owner and Musuhku not in meM:
                    try:
                        kk5.cancelGroupInvitation(Rumahku,[Temanku])
                        kk4.kickoutFromGroup(Rumahku,[Musuhku])
                        me.sendMessage(Rumahku, "Blacklist True")
                    except:
                        try:
                            kk4.cancelGroupInvitation(Rumahku,[Temanku])
                            kk3.kickoutFromGroup(Rumahku,[Musuhku])
                            me.sendMessage(Rumahku, "Blacklist True")
                        except:
                            try:
                                kk3.cancelGroupInvitation(Rumahku,[Temanku])
                                kk2.kickoutFromGroup(Rumahku,[Musuhku])
                                me.sendMessage(Rumahku, "Blacklist True")
                            except:
                                try:
                                    kk2.cancelGroupInvitation(Rumahku,[Temanku])
                                    kk1.kickoutFromGroup(Rumahku,[Musuhku])
                                    me.sendMessage(Rumahku, "Blacklist True")
                                except:
                                    kk1.cancelGroupInvitation(Rumahku,[Temanku])
                                    kk5.kickoutFromGroup(Rumahku,[Musuhku])
                                    me.sendMessage(Rumahku, "Blacklist True")
                else:pass
        if rank.type == 13:
            if meM in Temanku:
                if JhailBots["autoLeave"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                        me.leaveGroup(Rumahku)
                    else:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                        me.sendMessage(Rumahku,str(ginfo.name))

        if rank.type == 13:
            if meM in Temanku:
                if JhailBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                    else:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
            if Jhail1 in Temanku:
                if JhailBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        kk1.acceptGroupInvitation(Rumahku)
                        ginfo = kk1.getGroup(Rumahku)
                        kk1.leaveGroup(Rumahku)
                    else:
                        kk1.acceptGroupInvitation(Rumahku)
                        ginfo = kk1.getGroup(Rumahku)
            if Jhail2 in Temanku:
                if JhailBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        kk2.acceptGroupInvitation(Rumahku)
                        ginfo = kk2.getGroup(Rumahku)
                        kk2.leaveGroup(Rumahku)
                    else:
                        kk2.acceptGroupInvitation(Rumahku)
                        ginfo = kk2.getGroup(Rumahku)
            if Jhail3 in Temanku:
                if JhailBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        kk3.acceptGroupInvitation(Rumahku)
                        ginfo = kk3.getGroup(Rumahku)
                        kk3.leaveGroup(Rumahku)
                    else:
                        kk3.acceptGroupInvitation(Rumahku)
                        ginfo = kk3.getGroup(Rumahku)
            if Jhail4 in Temanku:
                if JhailBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        kk4.acceptGroupInvitation(Rumahku)
                        ginfo = kk4.getGroup(Rumahku)
                        kk4.leaveGroup(Rumahku)
                    else:
                        kk4.acceptGroupInvitation(Rumahku)
                        ginfo = kk4.getGroup(Rumahku)
            if Jhail5 in Temanku:
                if JhailBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in JhailWars:
                        kk5.acceptGroupInvitation(Rumahku)
                        ginfo = kk5.getGroup(Rumahku)
                        kk5.leaveGroup(Rumahku)
                    else:
                        kk5.acceptGroupInvitation(Rumahku)
                        ginfo = kk5.getGroup(Rumahku)

        if rank.type == 26 or rank.type == 25:
            msg = rank.message
            Keluarga = msg.id
            Pesan = msg.to
            Dari = msg._from
            Proses_message = msg.text
            if Proses_message == "Bot on" or Proses_message == "bot on":
                if Dari in Owner or Dari in meM:
                    JhailBots["bot"] = True
                    me.sendMessage(Pesan,"Bot di aktifkan")
                    me.sendMessage(Pesan,"╭─━━░★░━━─╗\n     ᴀᴄᴛɪᴠᴇ \n     sᴇʟғ ʙ❍ᴛs\n      ✔ ᴅᴏɴᴇ sᴜᴄᴄᴇs\n╚─━━░★░━━─╯")
                    JhailBots["Conection"] = Pesan
                    Run_Xx()
                    
            if Proses_message == "Bot off" or Proses_message == "bot off":
                print ("NOTIF BOT NON ACTIVE")
                if Dari in Owner or Dari in meM:
                    JhailBots["bot"] = False
                    me.sendMessage(Pesan,"Bot di matikan")
                    me.sendMessage(Pesan,"╭─━━░★░━━─╗\n     ɴ❍ɴ ᴀᴄᴛɪᴠᴇ \n     sᴇʟғ ʙ❍ᴛs\n      ✔ ᴅᴏɴᴇ sᴜᴄᴄᴇs\n╚─━━░★░━━─╯")
                
        if rank.type == 25 or rank.type == 26:
          if JhailBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Keluarga = msg.id
            Pesan = msg.to
            Dari = msg._from
            Gr = Rumahku
            JhailBotsLists = JhailBots["text"].title()
            if JhailBots["key"] == False:
                 JhailBotsLists = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if Dari != me.profile.mid:
                        to = Dari
                    else:
                        to = Pesan
                elif msg.toType == 1:
                    to = Pesan
                elif msg.toType == 2:
                    to = Pesan
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        JhailBotsList = SqL_R(text)
                        if JhailBotsList == Menu["1"]:
                          if Dari in Owner or Dari in meM:
                            Res= extras+"╭━──────────────━╮\n│➢     ᴍᴇɴᴜ\n╰━──────────────━╯\n╭━──────────────━╮\n"
                            Res+= Stiles+JhailBotsLists+Menu["1"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["2"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["3"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["4"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["5"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["6"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["7"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["8"]+" *porn\n"
                            Res+= Stiles+JhailBotsLists+Menu["9"]+" *judul\n"
                            Res+= Stiles+JhailBotsLists+Menu["10"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["11"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["12"]+" *txt/txt/txt\n"
                            Res+= Stiles+JhailBotsLists+Menu["13"]+" *text\n"
                            Res+= Stiles+JhailBotsLists+Menu["14"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["15"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["16"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["17"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["18"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["19"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["20"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["21"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["22"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["23"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["24"]+" *tags\n"
                            Res+= Stiles+JhailBotsLists+Menu["25"]+" *text\n"
                            Res+= Stiles+JhailBotsLists+Menu["26"]+" *01-02-1995\n"
                            Res+= Stiles+JhailBotsLists+Menu["27"]+" *id ig\n"
                            Res+= Stiles+JhailBotsLists+Menu["28"]+" *id smule\n"
                            Res+= Stiles+JhailBotsLists+Menu["29"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["30"]+" *text\n"
                            Res+= Stiles+JhailBotsLists+Menu["31"]+" *text\n"
                            Res+= Stiles+JhailBotsLists+Menu["32"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["33"]+" *text\n"
                            Res+= Stiles+JhailBotsLists+Menu["34"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["35"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["36"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["37"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["38"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["39"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["40"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["41"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["42"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["43"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["44"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["45"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["46"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["47"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["48"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["49"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["50"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["51"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["52"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["53"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["54"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["55"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["56"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["57"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["58"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["59"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["60"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["61"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["62"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["63"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["64"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["65"]+"\n"
                            Res+= Stiles+JhailBotsLists+Menu["66"]+"\n"
                            Res+= "├━──────────────━─\n├➢➢CHECK BOT\n├━──────────────━─\n"
                            if JhailBots["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if JhailBots["Shared"] == True: Res+= Stiles+" shared->『on』\n"
                            else: Res+= Stiles+" shared->『off』\n"
                            if JhailBots["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if JhailBots["Read"] == True: Res+= Stiles+" autoread->『on』\n"
                            else: Res+= Stiles+" autoread->『off』\n"
                            if JhailBots["Unsend"] == True: Res+= Stiles+" unsend->『on』\n"
                            else: Res+= Stiles+" unsend->『off』\n"
                            if JhailBots["Wc"] == True: Res+= Stiles+" welcome->『on』\n"
                            else: Res+= Stiles+" welcome->『off』\n"
                            if JhailBots["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            Res+= "╰━──────────────━╯\n╭━──────────────━╮\n│ᴅɪɴᴀsᴛʏ ɴᴅ❍ᴋ ᴄᴇᴘʟ❍ᴋ \n╰━──────────────━╯\n╭━──────────────━╮\n"
                            Res+= "├━────[SelfName]───━\n"+Stiles+meProfile.displayName+"\n"
                            me.sendMessage(Line_Apikey,Devert)
                            me.sendMessage(Pesan, str(Res)+Stiles+" ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs \n╰━──────────────━╯")
                            me.sendMessage(Pesan, extras+str(warKey))
                        if JhailBotsList == Menu["2"]:
                          if Dari in Owner or Dari in meM:
                            me.sendContact(Pesan,meM)
                        if JhailBotsList == Menu["3"]:
                          if Dari in Owner or Dari in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "My id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            me.sendMessage(Pesan,My_Id)
                        if JhailBotsList == Menu["4"]:
                          if Dari in Owner or Dari in meM:
                            me.leaveGroup(Pesan)
                        if JhailBotsList == Menu["5"]:
                          if Dari in Owner or Dari in meM:
                            h = me.getContact(Dari)
                            cpu = me.getProfileCoverURL(h)          
                            path = str(cpu)
                            me.sendImageWithURL(Pesan, path)
                        if JhailBotsList == Menu["6"]:
                          if Dari in Owner or Dari in meM:
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "_______CINEMA______\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            me.sendMessage(Pesan, str(hasil))
                        if JhailBotsList == Menu["7"]:
                          if Dari in Owner or Dari in meM:
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(InexBots["userAgent"])
                                r = web.get('http://api-1cak.herokuapp.com/random')
                                data = r.text
                                data = json.loads(data)
                                img = data["img"]
                                me.sendMessage(Pesan,"━═| Daftar cakcak |═━\n━═| Title: %s\n━═| Link: %s\n━═| Id: %s\n━═| Votes: %s\n━═| NSFW: %s\n━═| [ Finish ] |═━" %(str(data["title"].replace('FACEBOOK Comments', ' ')), str(data["url"]), str(data["id"]), str(data["votes"]), str(data["nsfw"])))
                        if JhailBotsList.startswith(Menu["8"]):
                          if Dari in Owner or Dari in meM:
                            separate = text.split(" ")
                            kata = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(InexBots["userAgent"])
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "━═Bokep inimah"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 20:
                                        for s in range(20):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    me.sendMessage(Pesan, str(ret_))
                                except:
                                    me.sendMessage(Pesan, "Tidak ditemukan")
                        if JhailBotsList.startswith(Menu["9"]):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            title = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(InexBots["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y=&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "╭━━═════[ Hasil pencarian film]"
                                hasil += "\n| Informasi : " +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\n| Plot : " +str(data["Plot"])
                                hasil += "\n| Director : " +str(data["Director"])
                                hasil += "\n| Actors : " +str(data["Actors"])
                                hasil += "\n| Release : " +str(data["Released"])
                                hasil += "\n| Genre : " +str(data["Genre"])
                                hasil += "\n| Timer : " +str(data["Runtime"])+"\n╰━──────────────━╯"
                                img = data["Poster"]
                                me.sendImageWithURL(Pesan,img)
                                me.sendMessage(Pesan,hasil)
                        if JhailBotsList.startswith(Menu["10"]):
                          if Dari in Owner or Dari in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            me.sendMessage(Pesan, "teman di tambahkan")
                        if JhailBotsList == Menu["11"]:
                          if Dari in Owner or Dari in meM:
                            me.sendMessage(Pesan, "Selesai.!!")
                            JhailBots["Conection"] = Pesan
                            Run_Xp()
                        if JhailBotsList.startswith(Menu["12"]):
                          if Dari in Owner or Dari in meM:
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
                            me.sendImageWithURL(Pesan, url)
                        if JhailBotsList.startswith(Menu["13"]):
                          if Dari in Owner or Dari in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=JHAIL"
                            me.sendImageWithURL(Pesan, url)
                        if JhailBotsList == Menu["14"]:
                          if Dari in Owner or Dari in meM:
                            timeNow = time.time()
                            rantime = timeNow - botStart
                            runtime = format_timespan(rantime)
                            me.sendMessage(Pesan, "☣️RUNTIME BOTS☣️\n☣️[ {}".format(str(runtime)))
                        if JhailBotsList == "sp":
                          if Dari in Owner or Dari in meM:
                            start = time.time()
                            me.sendMessage(Pesan, "Ngacirr...")
                            elapsed_time = time.time() - start
                            me.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                        if JhailBotsList == Menu["15"]:
                          if Dari in Owner or Dari in meM:
                            start = time.time()
                            me.sendMessage(Pesan, "gooo...")
                            elapsed_time = time.time() - start
                            me.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                            kk1.sendMessage(Pesan, "Ngacirrr...")
                            elapsed_time = time.time() - start
                            kk1.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                            kk2.sendMessage(Pesan, "Ngacirrr...")
                            elapsed_time = time.time() - start
                            kk2.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                            kk3.sendMessage(Pesan, "Ngacirrr...")
                            elapsed_time = time.time() - start
                            kk3.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                            kk4.sendMessage(Pesan, "Ngacirrr...")
                            elapsed_time = time.time() - start
                            kk4.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                            kk5.sendMessage(Pesan, "Ngacirrr...")
                            elapsed_time = time.time() - start
                            kk5.sendMessage(Pesan, "{} detik".format(str(elapsed_time)))
                        if JhailBotsList == Menu["16"]:
                          if Dari in Owner or Dari in meM:
                            h = me.getContact(Dari)
                            me.sendMessage(Pesan,h.mid)
                        if JhailBotsList == Menu["17"]:
                          if Dari in Owner or Dari in meM:
                            contact = me.getContact(Dari)
                            cover = me.getProfileCoverURL(Dari)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs ]"
                            me.sendImageWithURL(Pesan, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            me.sendImageWithURL(Pesan, str(cover))
                            me.sendMessage(Pesan, str(result))
                        if JhailBotsList == Menu["18"]:
                          if Dari in Owner or Dari in meM:
                            h = me.getContact(Dari)
                            me.sendVideoWithURL(Pesan,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        if JhailBotsList.startswith(Menu["19"]):
                          if Dari in Owner or Dari in meM:
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
                                me.sendMessage(Pesan, str(ret_))
                        if JhailBotsList.startswith(Menu["20"]):
                          if Dari in Owner or Dari in meM:
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
                                    me.sendImageWithURL(Pesan, str(path))
                        if JhailBotsList.startswith(Menu["21"]):
                          if Dari in Owner or Dari in meM:
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
                                    me.sendVideoWithURL(Pesan, str(path))
                        if JhailBotsList.startswith(Menu["22"]):
                          if Dari in Owner or Dari in meM:
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
                                    me.sendMessage(Pesan, "Namanya\n{}".format(str(contact.displayName)))
                        if JhailBotsList.startswith(Menu["23"]):
                          if Dari in Owner or Dari in meM:
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
                                    me.sendMessage(Pesan, "Status kontak\n\n{}".format(str(contact.statusMessage)))
                        if JhailBotsList.startswith(Menu["24"]):
                          if Dari in Owner or Dari in meM:
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
                                    me.sendContact(Pesan, mi_d)
                        if JhailBotsList.startswith(Menu["25"]):
                          if Dari in Owner or Dari in meM:
                            me.sendMessage(Pesan, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(InexBots["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                me.sendMessage(Pesan, str(ret_))
                        if JhailBotsList.startswith(Menu["26"]):
                          if Dari in Owner or Dari in meM:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━════[ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs]"
                                me.sendMessage(Pesan, str(ret_))
                            except Exception as error:
                                logError(error)
                        if JhailBotsList.startswith(Menu["27"]):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(InexBots["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                me.sendImageWithURL(Pesan, text1[0])
                                me.sendMessage(Pesan, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        if JhailBotsList.startswith(Menu["28"]):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            me.sendMessage(Pesan, "ini id smulenya kak\n" + smule)
                        if JhailBotsList == Menu["29"]:
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesam)
                                members = [mem.mid for mem in group.members]
                                me.acquireGroupCallRoute(Pesan)
                                me.inviteIntoGroupCall(R, contactIds=members)
                                me.sendMessage(Pesan, "Berhasil")
                        if JhailBotsList.startswith(Menu["30"]):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("hasil.mp3")
                            me.sendAudio(Pesan,"hasil.mp3")
                        if JhailBotsList.startswith(Menu["31"]):
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                X = me.getGroup(Pesan)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                me.updateGroup(X)
                        if JhailBotsList == Menu["32"]:
                          if Dari in Owner or Dari in meM:
                            me.removeAllMessages(Musuhku)
                            kk1.removeAllMessages(Musuhku)
                            kk2.removeAllMessages(Musuhku)
                            kk3.removeAllMessages(Musuhku)
                            kk4.removeAllMessages(Musuhku)
                            kk5.removeAllMessages(Musuhku)
                            jss.removeAllMessages(Musuhku)
                            me.sendMessage(Pesan, "Chat deleted")
                        if JhailBotsList.startswith(Menu["33"]):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = me.groups
                            for group in groups:
                                sendMessageWithFooter(group, "╭━━━━━╦BroadCast ╦━━━━━╮\n{}".format(str(txt))+"\n αɳเɳ∂ყα ɓσƭร")
                            me.sendMessage(Pesan, "Berhasil broadcast ke {} group".format(str(len(groups))))
                        if JhailBotsList == Menu["34"]:
                          if Dari in Owner or Dari in meM:
                            groups = me.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = me.getGroup(gid)
                                ret_ += "\n┣═ {}. {} \n┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                            me.sendMessage(Pesan, str(ret_))
                        if JhailBotsList == Menu["35"]:
                          if Dari in Owner or Dari in meM:
                            contactlist = me.getAllContactIds()
                            kontak = me.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            me.sendMessage(Pesan, msgs)
                        if JhailBotsList == Menu["36"]:
                          if Dari in Owner or Dari in meM:
                            blockedlist = me.getBlockedContactIds()
                            kontak = me.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            me.sendMessage(Pesan, msgs)
                        if JhailBotsList == Menu["37"]:
                          if Dari in Owner or Dari in meM:
                            me.sendMessage(Pesan, "━━━━══[Pembuat Grup]══━━━━")
                            group = me.getGroup(Pesan)
                            GS = group.creator.mid
                            me.sendContact(Pesan, GS)
                            me.sendMessage(Pesan, "━━━━══━━╩━━══━━━━")
                        if JhailBotsList == Menu["38"]:
                          if Dari in Owner or Dari in meM:
                            if Dari in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(Pesan)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    me.sendMessage(Pesan, str(ret_))
                        if JhailBotsList == Menu["39"]:
                          if Dari in Owner or Dari in meM:
                            if Dari in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(Pesan)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(Pesan, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        me.sendMessage(Pesan, str(ret_))
                        if JhailBotsList == Menu["40"]:
                            if Dari in Owner or Dari in meM:
                                group = me.getGroup(Pesan)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://me.me/R/ti/g/{}".format(str(me.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs]"
                                me.sendImageWithURL(Pesan, path)
                                me.sendMessage(Pesan, str(ret_))
                        if JhailBotsList == Menu["41"]:
                          if Dari in Owner or Dari in meM:
                            group = me.getGroup(Pesan)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            me.sendImageWithURL(Pesan, path)
                        if JhailBotsList == Menu["42"]:
                          if Dari in Owner or Dari in meM:
                            gid = me.getGroup(Pesan)
                            me.sendMessage(Pesan, "Name group\n" + gid.name)
                        if JhailBotsList == Menu["43"]:
                          if Dari in Owner or Dari in meM:
                            gid = me.getGroup(Pesan)
                            me.sendMessage(Pesan,gid.id)
                        if JhailBotsList == Menu["44"]:
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesan)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(Pesan)
                                    me.sendMessage(Pesan, "https://me.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(Pesan, "https://me.me/R/ti/g/{}".format(str(ticket)))
                        if JhailBotsList == Menu["45"]:
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesan)
                                if group.preventedJoinByTicket == False:
                                    me.sendMessage(Pesan, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(Pesan, "Berhasil membuka Qr")
                        if JhailBotsList == Menu["46"]:
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesan)
                                if group.preventedJoinByTicket == True:
                                    me.sendMessage(Pesan, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    me.sendMessage(Pesan, "Berhasil menutup Qr")
                        if JhailBotsList == Menu["47"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Add"] = True
                            me.sendMessage(Pesan, "Auto add di aktifkan")
                        if JhailBotsList == Menu["48"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Add"] = False
                            me.sendMessage(Pesan, "Auto add di nonaktifkan")
                        if JhailBotsList == Menu["49"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Join"] = True
                            me.sendMessage(Pesan, "Auto join di aktifkan")
                        if JhailBotsList == Menu["50"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Join"] = False
                            me.sendMessage(Pesan, "Auto join di nonaktifkan")
                        if JhailBotsList == Menu["51"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Read"] = True
                            me.sendMessage(Pesan, "Autoread on")
                        if JhailBotsList == Menu["52"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Read"] = False
                            me.sendMessage(Pesan, "Autoread off")
                        if JhailBotsList == Menu["53"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Unsend"] = True
                            me.sendMessage(Pesan, "Unsend on")
                        if JhailBotsList == Menu["54"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Unsend"] = False
                            me.sendMessage(Pesan, "Unsend off")
                        if JhailBotsList == Menu["55"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Wc"] = True
                            me.sendMessage(Pesan, "Welcome Already on")
                        if JhailBotsList == Menu["56"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Wc"] = False
                            me.sendMessage(Pesan, "Welcome Already off")
                        if JhailBotsList == Menu["57"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Shared"] = True
                            me.sendMessage(Pesan, "Already on")
                        if JhailBotsList == Menu["58"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Shared"] = False
                            me.sendMessage(Pesan, "Already off")
                        if JhailBotsList == Menu["59"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Respon"] = True
                            me.sendMessage(Pesan, "Already on")
                        if JhailBotsList == Menu["60"]:
                          if Dari in Owner or Dari in meM:
                            JhailBots["Respon"] = False
                            me.sendMessage(Pesan, "Already off")
                        if JhailBotsList == Menu["61"]:
                          if Dari in Owner or Dari in meM:
                                try:
                                    del Sid['Red'][Pesan]
                                    del Sid['Reason'][Pesan]
                                    del Sid['Tar'][Pesan]
                                except:
                                    pass
                                Sid['Red'][Pesan] = Keluarga
                                Sid['Reason'][Pesan] = ""
                                Sid['Tar'][Pesan]=True
                                me.sendMessage(Pesan, "inex")
                        if JhailBotsList == Menu["62"]:
                          if Dari in Owner or Dari in meM:
                            if Pesan in Sid['Red']:
                                Sid['Tar'][Pesan]=False
                                me.sendMessage(Pesan, "Daftar yang terlihat\n"+Sid['Reason'][Pesan])
                                me.sendMessage(Pesan, "Already off")
                            else:
                                me.sendMessage(Pesan, "aktifkan dulu coy sidernya")
                        if JhailBotsList == Menu["63"]:
                         if Dari in Owner or Dari in meM:
                          Group = me.getGroup(Pesan)
                          Rmem = [contact.mid for contact in Group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "╭━─────────────────━╮\n│ Daftar Jones\n╰━─────────────────━╯\n╭━─────────────────━╮"
                                  dataMid = []
                                  for dataMention in Group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n│ @! ".format(str(no))
                                  ret_ += "\n╰━─────────────────━╯".format(str(len(dataMid)))
                                  sendMeention(Pesan, ret_, dataMid)
                          except Exception as Ough:
                              print(Ough)
                        if JhailBotsList == Menu["64"]:
                          if Dari in Owner or Dari in meM:
                            try:
                                JhailBots["Shared"] = True
                                JhailBots["Add"] = True
                                JhailBots["Join"] = True
                                JhailBots["Wc"] = True
                                JhailBots["Read"] = True
                                JhailBots["Unsend"] = True
                            except:me.sendMessage(Pesan,"SETTING ALL IN ONLINE")
                        if JhailBotsList == Menu["65"]:
                          if Dari in Owner or Dari in meM:
                            try:
                                JhailBots["Shared"] = False
                                JhailBots["Add"] = False
                                JhailBots["Join"] = False
                                JhailBots["Wc"] = False
                                JhailBots["Read"] = False
                                JhailBots["Unsend"] = False
                            except:me.sendMessage(Pesan,"SETTING ALL IN OFFLINE")
                        if JhailBotsList == "menu" or JhailBotsList == "key":
                          if Dari in Owner or Dari in meM:
                              me.sendMessage(Pesan, extras+str(warKey))
                              me.sendMessage(Line_Apikey,Devert)
                        if JhailBotsList == "mybot" or JhailBotsList == "Mybot":
                          if Dari in Owner or Dari in meM:
                              me.sendContact(Pesan,Jhail1)
                              me.sendContact(Pesan,Jhail2)
                              me.sendContact(Pesan,Jhail3)
                              me.sendContact(Pesan,Jhail4)
                              me.sendContact(Pesan,Jhail5)
                              me.sendContact(Pesan,Antijs)
                        if JhailBotsList == "banlist":
                          if Dari in Owner or Dari in meM:
                            if JhailBots["blacklist"] == {}:
                                me.sendMessage(Pesan,"Tidak ada blacklist")
                            else:
                                me.sendMessage(Pesan,"[BLACKLIST]")
                                h = ""
                                for i in JhailBots["blacklist"]:
                                  h = me.getContact(i)
                                  me.sendContact(Pesan,i)
                                me.sendMessage(Pesan," ᴊʜᴀɪʟʙᴏᴛs ")
                        if JhailBotsList == "clearban" or JhailBotsList == "Clearban":
                          if Dari in Owner or Dari in meM:
                            me.sendMessage(Pesan, "Berhasil menghapus {} user blacklist".format(str(len(InexBots["blacklist"]))))
                            JhailBots["blacklist"] = {}
                        if JhailBotsList == "ping":
                          if Dari in Owner or Dari in meM:
                            kk1.sendMessage(Pesan, "⪨⪩─┅❇͜͡нα∂ιя...࿐\n⪨⪩─┅❇͜͡ ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs 1.࿐")
                            kk2.sendMessage(Pesan, "⪨⪩─┅❇͜͡нα∂ιя...࿐\n⪨⪩─┅❇͜͡ ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs 2.࿐")
                            kk3.sendMessage(Pesan, "⪨⪩─┅❇͜͡нα∂ιя...࿐\n⪨⪩─┅❇͜͡ ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs 3.࿐")
                            kk4.sendMessage(Pesan, "⪨⪩─┅❇͜͡нα∂ιя...࿐\n⪨⪩─┅❇͜͡ ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs 4.࿐")
                            kk5.sendMessage(Pesan, "⪨⪩─┅❇͜͡нα∂ιя...࿐\n⪨⪩─┅❇͜͡ ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs 5.࿐")
                        if JhailBotsList == "js in" or JhailBotsList == "ajs in":
                          if Dari in Owner or Dari in meM:
                            gg = me.getGroup(Pesan)
                            gg.preventedJoinByTicket = False
                            me.updateGroup(gg)
                            grup = me.reissueGroupTicket(Pesan)
                            jss.acceptGroupInvitationByTicket(Pesan, grup)
                            gg.preventedJoinByTicket = True
                            jss.updateGroup(gg)
                        if JhailBotsList == "js out" or JhailBotsList == "ajs out":
                          if Dari in Owner or Dari in meM:
                            gg = me.getGroup(Pesan)
                            jss.leaveGroup(Pesan)
                        if JhailBotsList == "stay" or JhailBotsList == "ajs":
                          if Dari in Owner or Dari in meM:
                              group = me.getGroup(Pesan)
                              me.inviteIntoGroup(Pesan, [Antijs])
                        if JhailBotsList == "stanbay":
                          if Dari in Owner or Dari in meM:
                            try:
                                me.inviteIntoGroup(Pesan, [Jhail1,Jhail2,Jhail3,Jhail4,Jhail5,Antijs])
                            except:
                                try:
                                    jss.leaveGroup(Pesan)
                                    me.inviteIntoGroup(Pesan, [Jhail1,Jhail2,Jhail3,Jhail4,Jhail5,Antijs])
                                except:
                                    try:
                                        gg = me.getGroup(Pesan)
                                        gg.preventedJoinByTicket = False
                                        me.updateGroup(gg)
                                        grup = me.reissueGroupTicket(Pesan)
                                        kk1.acceptGroupInvitationByTicket(Pesan, grup)
                                        gg.preventedJoinByTicket = True
                                        kk1.updateGroup(gg)
                                        kk1.inviteIntoGroup(Pesan, [Antijs])
                                        kk1.leaveGroup(Pesan)
                                    except:me.sendMessage(Pesan, "BOT HARUS GANTI TOKEN")
                        if JhailBotsList == "." or JhailBotsList == "join":
                          if Dari in Owner or Dari in meM:
                            try:
                                me.inviteIntoGroup(Pesan, [Jhail1,Jhail2,Jhail3,Jhail4,Jhail5,Antijs])
                                kk1.acceptGroupInvitation(Pesan)
                                kk2.acceptGroupInvitation(Pesan)
                                kk3.acceptGroupInvitation(Pesan)
                                kk4.acceptGroupInvitation(Pesan)
                                kk5.acceptGroupInvitation(Pesan)
                            except:
                                try:
                                    gg = me.getGroup(Pesan)
                                    gg.preventedJoinByTicket = False
                                    me.updateGroup(gg)
                                    grup = me.reissueGroupTicket(Pesan)
                                    kk1.acceptGroupInvitationByTicket(Pesan, grup)
                                    kk2.acceptGroupInvitationByTicket(Pesan, grup)
                                    kk3.acceptGroupInvitationByTicket(Pesan, grup)
                                    kk4.acceptGroupInvitationByTicket(Pesan, grup)
                                    kk5.acceptGroupInvitationByTicket(Pesan, grup)
                                    kk5.inviteIntoGroup(Pesan, [Antijs])
                                    gg.preventedJoinByTicket = True
                                    kk5.updateGroup(gg)
                                except:me.sendMessage(Pesan, "BOT LIMIT!!!")
                        if JhailBotsList == "," or JhailBotsList == "pulang":
                          if Dari in Owner or Dari in meM:
                            try:
                                kk1.leaveGroup(Pesan)
                                kk2.leaveGroup(Pesan)
                                kk3.leaveGroup(Pesan)
                                kk4.leaveGroup(Pesan)
                                kk5.leaveGroup(Pesan)
                                jss.acceptGroupInvitation(Pesan)
                                jss.leaveGroup(Pesan)
                            except:me.sendMessage(Pesan, "BOT HARUS GANTI TOKEN")
                        if JhailBotsList == "cek" or JhailBotsList == "stamina":
                          if Dari in Owner or Dari in meM:
                            try:me.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:me.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁🄾🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            me.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                            try:kk1.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:kk1.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁🄾🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            kk1.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                            try:kk2.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:kk2.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁??🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            kk2.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                            try:kk3.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:kk3.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁🄾🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            kk3.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                            try:kk4.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:kk4.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁🄾🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            kk4.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                            try:kk5.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:kk5.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁🄾🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            kk5.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                            kk5.sendContact(Pesan,Admin)
                        if JhailBotsList == "cek js" or JhailBotsList == "skill js":
                          if Dari in Owner or Dari in meM:
                            try:jss.inviteIntoGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                            except:has = "NOT"
                            try:jss.kickoutFromGroup(Pesan, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "🅂🅃🅁🄾🄽🄶"
                            else:sil = "ⓁⒾⓂⒾⓉ!!!"
                            if has1 == "OK":sil1 = "🅂🅃🅁🄾🄽🄶"
                            else:sil1 = "ⓁⒾⓂⒾⓉ!!!"
                            jss.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                        if JhailBotsList.startswith("sory "):
                          if Dari in Owner or Dari in meM:
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
                                      berak = [kk1,kk2,kk3,kk4,kk5]
                                      berakin = random.choice(berak)
                                      berakin.kickoutFromGroup(Pesan,[ls])
                                      print (Pesan,[ls])
                                  except:
                                      pass
                        if JhailBotsList.startswith("botname: "):
                          if Dari in Owner or Dari in meM:
                              separate = JhailBotsList.split(" ")
                              string = JhailBotsList.replace(separate[0] + " ","")
                              if len(string) <= 10000000000:
                                  profile1 = kk1.getProfile()
                                  profile1.displayName = string
                                  kk1.updateProfile(profile1)
                                  kk1.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                                  profile2 = kk2.getProfile()
                                  profile2.displayName = string
                                  kk2.updateProfile(profile2)
                                  kk2.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                                  profile3 = kk3.getProfile()
                                  profile3.displayName = string
                                  kk3.updateProfile(profile3)
                                  kk3.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                                  profile4 = kk4.getProfile()
                                  profile4.displayName = string
                                  kk4.updateProfile(profile4)
                                  kk4.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                                  profile5 = kk5.getProfile()
                                  profile5.displayName = string
                                  kk5.updateProfile(profile5)
                                  kk5.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                        if JhailBotsList.startswith("jsname: "):
                          if Dari in Owner or Dari in meM:
                              separate = JhailBotsList.split(" ")
                              string = JhailBotsList.replace(separate[0] + " ","")
                              if len(string) <= 10000000000:
                                  profile = jss.getProfile()
                                  profile.displayName = string
                                  jss.updateProfile(profile)
                                  jss.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                        if JhailBotsList.startswith("keplak "):
                          if Dari in Owner or Dari in meM:
                              nk0 = msg.text.replace("keplak ","")
                              nk1 = nk0.lstrip()
                              nk2 = nk1.replace("@","")
                              nk3 = nk2.rstrip()
                              _name = nk3
                              gs = me.getGroup(Pesan)
                              targets = []
                              for s in gs.members:
                                  if _name in s.displayName:
                                      targets.append(s.mid)
                                  if targets == []:
                                      pass
                                  else:
                                      for target in targets:
                                          if target not in JhailWars and target not in Owner and target not in meM:
                                              try:
                                                  JhailBots["blacklist"][target] = True
                                                  klist=[kk1,kk2,kk3,kk4,kk5]
                                                  kicker=random.choice(klist)
                                                  kicker.kickoutFromGroup(Pesan,[target])
                                                  print (Pesan,[s.mid])
                                              except Exception as A:
                                                  print(A)
                        if JhailBotsList == Menu["66"]:
                          if Dari in Owner or Dari in meM:
                            RunTheRun(Pesan, Dari, "[_______[RESULT]______]\n")
                            """
                            BOT WAR
                            VERSION : ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs
                            REVISION : VPS
                            """
        if rank.type == 25:
          """
          BOT WAR
          VERSION : ᴊʜᴀɪʟ™ᴛᴇᴀᴍ ʙ❍ᴛs
          REVISION : VPS
          """
          if JhailBots["bot"] == True:
            war = rank.message
            Jhailwar = war.text
            Keluarga = war.id
            Pesan = war.to
            Dari = war._from
            if Jhailwar == "autojoin on":
              if Dari in Owner or Dari in meM:
                  JhailBots["autoJoin"] = True
                  me.sendMessage(Pesan,"join d aktifkan.....")
            if Jhailwar == "autojoin off":
              if Dari in Owner or Dari in meM:
                  JhailBots["autoJoin"] = False
                  me.sendMessage(Pesan,"join d non aktifkan.....")
            if Jhailwar == "respon on" or Jhailwar == "respon on":
              if Dari in Owner or Dari in meM:
                  JhailBots["arespon"] = True
                  me.sendMessage(Pesan,"Respon pm d aktifkan.....")
            if Jhailwar == "respon off" or Jhailwar == "respon off":
              if Dari in Owner or Dari in meM:
                  JhailBots["arespon"] = False
                  me.sendMessage(Pesan,"Respon pm d nonaktifkan.....")
            if Jhailwar == "autoleave on" or Jhailwar == "Autoleave on":
              if Dari in Owner or Dari in meM:
                  JhailBots["autoLeave"] = True
                  me.sendMessage(Pesan,"Leave d aktifkan.....")
            if Jhailwar == "autoleave off" or Jhailwar == "Autoleave off":
              if Dari in Owner or Dari in meM:
                  JhailBots["autoLeave"] = False
                  me.sendMessage(Pesan,"Leave d non aktifkan.....")
            if Jhailwar == "admin on" or Jhailwar == "Admin on":
              if Dari in Owner or Dari in meM:
                  JhailBots["addOwner"] = True
                  me.sendMessage(Pesan,"Kirim kontaknya...")
            if Jhailwar == "admin off" or Jhailwar == "Admin off":
              if Dari in Owner or Dari in meM:
                  JhailBots["dellOwner"] = True
                  me.sendMessage(Pesan,"Kirim kontaknya...")
            if Jhailwar == "my pict":
              if Dari in Owner or Dari in meM:
                  JhailBots["SKfoto"][meM] = True
                  me.sendMessage(Pesan,"Kirim fotonya.....")
            if Jhailwar == "bot pict" or Jhailwar == "Bot pict":
              if Dari in Owner or Dari in meM:
                  JhailBots["changePicture"] = True
                  me.sendMessage(Pesan,"Kirim fotonya.....")
            if Jhailwar == "adminlist" or Jhailwar == "Adminlist":
              if Dari in Owner or Dari in meM:
                  ma = ""
                  a = 0
                  for m_id in Owner:
                      a = a + 1
                      end = '\n'
                      ma += str(a) + ". " +me.getContact(m_id).displayName + "\n"
                  me.sendMessage(Pesan,"☠•ADMINLIST\n\n☠•Creator Bots :\n"+ma+"\nTotal「%s」 Bots" %(str(len(meM)+len(Owner))))
            if 'Pro ' in Jhailwar:
              if Dari in Owner or Dari in meM:
                  spl = Jhailwar.replace('Pro ','')
                  if spl == 'on':
                      if Pesan in pro["Pintu"]:
                           msgs = ""
                      else:
                           pro["Pintu"].append(Pesan)
                      if Pesan in pro["Pembunuh"]:
                          msgs = ""
                      else:
                          pro["Pembunuh"].append(Pesan)
                      if Pesan in pro["Maling"]:
                          msgs = ""
                      else:
                          pro["Maling"].append(Pesan)
                      if Pesan in pro["Penghasut"]:
                          msgs = ""
                      else:
                          pro["Penghasut"].append(Pesan)
                      if Pesan in pro["Pencuri"]:
                          msgs = ""
                      else:
                          pro["Pencuri"].append(Pesan)
                      if Pesan in pro["Kuntilanak"]:
                          msgs = ""
                      else:
                          pro["Kuntilanak"].append(Pesan)
                      if Pesan in pro["Penyelamat"]:
                          ginfo = me.getGroup(Pesan)
                          msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                      else:
                          pro["Penyelamat"].append(Pesan)
                          ginfo = me.getGroup(Pesan)
                          msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                      me.sendMessage(Pesan, "「Diaktifkan」\n" + msgs)
                  if spl == 'off':
                        if Pesan in pro["Pintu"]:
                             pro["Pintu"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Pembunuh"]:
                             pro["Pembunuh"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Maling"]:
                             pro["Maling"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Penghasut"]:
                             pro["Penghasut"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Pencuri"]:
                             pro["Pencuri"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Kuntilanak"]:
                             pro["Kuntilanak"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Penyelamat"]:
                             pro["Penyelamat"].remove(Pesan)
                             ginfo = me.getGroup(Pesan)
                             msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                        else:
                             ginfo = me.getGroup(Pesan)
                             msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                        me.sendMessage(Pesan, "「Dinonaktifkan」\n" + msgs)
            if ("Adminadd " in Jhailwar):
              if Dari in Owner or Dari in meM:
                 key = eval(msg.contentMetadata["MENTION"])
                 key["MENTIONEES"][0]["M"]
                 targets = []
                 for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                 for target in targets:
                     if target not in JhailWars:
                         try:
                             Owner.append(target)
                             me.sendMessage(Pesan,"Berhasil menambahkan admin")
                         except:
                             pass
            if ("Admindell " in Jhailwar):
              if Dari in Owner or Dari in meM:
                 key = eval(msg.contentMetadata["MENTION"])
                 key["MENTIONEES"][0]["M"]
                 targets = []
                 for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                 for target in targets:
                     if target not in JhailWars:
                         try:
                             Owner.remove(target)
                             me.sendMessage(Pesan,"Berhasil menghapus admin")
                         except:
                             pass

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
                                    me.sendMessage(R, respontags["Auto_text"])
                                    me.sendContact(R, D)
                                break
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if JhailBots["arespon"] == True:
                                    #contact = me.getContact(D)
                                    sendMention(D, "\n"+respontags["Auto_pM"], [D])
                                break
                if msg.contentType == 1:
                    if meM in JhailBots["SKfoto"]:
                         path = me.downloadObjectMsg(R)
                         del JhailBots["SKfoto"][meM]
                         me.updateProfilePicture(path)
                         me.sendMessage(R,"Foto berhasil dirubah")
                if msg.contentType == 1:
                    if JhailBots["changePicture"] == True:
                        path1 = kk1.downloadObjectMsg(Id)
                        path2 = kk2.downloadObjectMsg(Id)
                        path3 = kk3.downloadObjectMsg(Id)
                        path4 = kk4.downloadObjectMsg(Id)
                        path5 = kk5.downloadObjectMsg(Id)
                        path6 = jss.downloadObjectMsg(Id)
                        JhailBots["changePicture"] = False
                        kk1.updateProfilePicture(path1)
                        kk1.sendMessage(R, "Berhasil mengubah foto profile bot")
                        kk2.updateProfilePicture(path2)
                        kk2.sendMessage(R, "Berhasil mengubah foto profile bot")
                        kk3.updateProfilePicture(path3)
                        kk3.sendMessage(R, "Berhasil mengubah foto profile bot")
                        kk4.updateProfilePicture(path4)
                        kk4.sendMessage(R, "Berhasil mengubah foto profile bot")
                        kk5.updateProfilePicture(path5)
                        kk5.sendMessage(R, "Berhasil mengubah foto profile bot")
                        jss.updateProfilePicture(path6)
                        jss.sendMessage(R, "Berhasil mengubah foto profile bot")
        if rank.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = Rumahku
            if JhailBots["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
            if JhailBots["addOwner"] == True:
              if msg.contentMetadata["mid"] in Owner:
                  me.sendMessage(R,"Contact itu sudah jadi admin")
                  JhailBots["addOwner"] = True
              else:
                  Owner.append(msg.contentMetadata["mid"])
                  JhailBots["addOwner"] = True
                  me.sendMessage(R,"Berhasil menambahkan ke admin")
            if JhailBots["dellOwner"] == True:
              if msg.contentMetadata["mid"] in Owner:
                  Owner.remove(msg.contentMetadata["mid"])
                  me.sendMessage(R,"Berhasil menghapus dari admin")
              else:
                  JhailBots["dellOwner"] = True
                  me.sendMessage(R,"Contact itu bukan admin")
        if rank.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if JhailBots["Add"] == True:
                me.findAndAddContactsByMid(Rumahku)
            sendMention(Rumahku, Rumahku, "тᴇяıмᴀ кᴀsıн suᴅᴀн ᴀᴅᴅ sᴀʏᴀ \nвʏ.ᴛᴇᴀᴍ ⊶ ʙᴏᴛs ⊷ \nline.me/ti/p/~agoest___ ","")
        if rank.type == 15:
            Gr = Rumahku
            Cj = Musuhku
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if JhailBots["Wc"] == True:
              if Cj in JhailWars:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Papay : {}".format(dia.displayName)
                ms += "In group : {}".format(Gc.name)
                mt = "Nah {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendMessage(dia,mt)
                me.sendContact(Gr,dia)
        if rank.type == 17:
            Gr = Rumahku
            Cj = Musuhku
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if JhailBots["Wc"] == True:
              if Cj in JhailWars:
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
                try:
                    at = Rumahku
                    Id = Musuhku
                    if Id in msg_dict:
                        if msg_dict[Id]["from"]:
                           if msg_dict[Id]["text"] == 'Gambarnya dibawah':
                                ginfo = me.getGroup(at)
                                jaka = me.getContact(msg_dict[Id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = "╭━━━━══════════════"
                                ret_ = "\n┣☠•➤ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n┣☠•➤ Waktu Dikirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[Id]["createdTime"])))
                                ret_ += "\n╰━━━━══════════════"
                                ry = str(jaka.displayName)
                                pesan = ''
                                pesan2 = pesan+"{} \n".format(str(jaka.displayName))
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':jaka.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                #me.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                me.sendMessage(at, text)
                                me.sendImage(at, msg_dict[Id]["data"])
                           else:
                                ginfo = me.getGroup(at)
                                jaka = me.getContact(msg_dict[Id]["from"])             
                                ret_ = "╭━━━━══════════════"
                                ret_ += "\n┣☠•➤ Pesan Dihapus"
                                ret_ += "\n┣☠•➤  Pengirim : {}".format(str(jaka.displayName))
                                ret_ += "\n┣☠•➤  Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n┣☠•➤  Waktu Dikirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[Id]["createdTime"])))
                                ret_ += "\n┣☠•➤  Pesannya : {}".format(str(msg_dict[Id]["text"]))
                                ret_ += "\n╰━━━━══════════════"
                                me.sendMessage(at, str(ret_))
                        del msg_dict[Id]
                except Exception as e:
                    print(e)
            if JhailBots["Unsend"] == True:
                try:
                    at = Rumahku
                    Id = Musuhku
                    if Id in msg_dict1:
                        if msg_dict1[Id]["from"]:
                                ginfo = me.getGroup(at)
                                jaka = me.getContact(msg_dict1[Id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ = "╭━━━━══════════════"
                                ret_ += "\n┣☠•➤ Pengirim : {}".format(str(jaka.displayName))
                                ret_ += "\n┣☠•➤ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n┣☠•➤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[Id]["createdTime"])))
                                ret_ += "\n┣☠•➤ {}".format(str(msg_dict1[Id]["text"]))
                                ret_ += "\n╰━━━━══════════════"
                                me.sendMessage(at, str(ret_))
                                me.sendImage(at, msg_dict1[Id]["data"])
                        del msg_dict1[Id]
                except Exception as e:
                    print(e)

        if rank.type == 55:
            Gr = Rumahku
            try:
                if Sid['Tar'][Gr]==True:
                        if Gr in Sid['Red']:
                            Name = me.getContact(Musuhku).displayName
                            Np = me.getContact(Musuhku).pictureStatus
                            if Name in Sid['Reason'][Gr]:
                                pass
                            else:
                                Sid['Reason'][Gr] += "\n||[ " + Name + " ]||"
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[0] + " " + "\nNah jangan ngintip mulu . . .\nGabung Chat yux ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[1] + " " + "\nJangan ngintip.. . . .\nMasuk  ayox... ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    me.sendMessage(Gr, "hallo.. " + " " + Name + " " + "\nJangan ngintip aja\nMasuk gabung chat ya... ")
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
