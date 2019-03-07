#!/usr/bin/env python2.7

import sys
import socket
import string
import re
from time import sleep

host = "irc.devel.redhat.com"
port = 6667
nick = "cnvrobot"
ident = "cnvrobot"
realname = "cnvrobot"
channel = "#cnv-qe"

s = socket.socket()
s.connect((host, port))
s.send("NICK %s\r\n" % nick)
s.send("USER %s %s bla :%s\r\n" % (ident, host, realname))
s.send("JOIN :%s\r\n" % channel)
s.send("PRIVMSG %s :%s\r\n" % (channel, "Hey!I'm cnvrobot:P"))

while True:
    # Keep receive data
    data = s.recv(4096)

    # Keep response to irc server
    matchObj = re.search(r"PING", data)
    if matchObj:
        s.send('PONG ' + data.split()[1] + '\r\n')
        s.send("JOIN :%s\r\n" % channel)

    # Response hi from anyone
    matchObj = re.search(r"cnvrobot[,:]? hi", data, re.I)
    if matchObj:
        s.send("PRIVMSG %s :%s %s\r\n" %
               (channel, "Hi~", re.search(r"[a-z]+", data).group()))

    matchObj = re.search(r"hi[,:]? cnvrobot[,:]?", data, re.I)
    if matchObj:
        s.send("PRIVMSG %s :%s %s\r\n" %
               (channel, "Hi~", re.search(r"[a-z]+", data).group()))
    
    # Response hello from anyone
    matchObj = re.search(r"cnvrobot[,:]? hello", data, re.I)
    if matchObj:
        s.send("PRIVMSG %s :%s %s\r\n" %
               (channel, "I already said Hi~", re.search(r"[a-z]+", data).group()))

    # Response hello from anyone
    matchObj = re.search(r"hello[,:]? cnvrobot[,:]?", data, re.I)
    if matchObj:
        s.send("PRIVMSG %s :%s %s\r\n" %
               (channel, "I already said Hi~", re.search(r"[a-z]+", data).group()))

    # broadcast message to team
    matchObj = re.search(r"\.team(.*)", data)
    if matchObj:
        team = "aramteke ashoshan dollierp dshchedr duyan gouyang guchen gszasz igulina ipinto jparrill kbidarka kgoldbla lbednar myakove nelly ngavrilo pbrilla pharvey qwang rhrazdil shiywang sradco talayan vatsal xlisovsk ysegev zpeng nkononov"
        message = matchObj.group().replace(".team", team)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to beijing members
    matchObj = re.search(r"\.cnvbeijing(.*)", data)
    if matchObj:
        cnvbeijing = "duyan gouyang qwang shiyang zpeng"
        message = matchObj.group().replace(".cnvbeijing", cnvbeijing)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to cnvraanana members
    matchObj = re.search(r"\.cnvraanana(.*)", data)
    if matchObj:
        cnvraanana = "ashoshan guchen kgoldbla myakove nelly ngavrilo ysegev nkononov"
        message = matchObj.group().replace(".cnvraanana", cnvraanana)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to cnvbrno members
    matchObj = re.search(r"\.cnvbrno(.*)", data)
    if matchObj:
        cnvbrno = "igulina gszasz lbednar pbrilla rhrazdil"
        message = matchObj.group().replace(".cnvbrno", cnvbrno)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))
    
    # broadcast message to cnvindia members
    matchObj = re.search(r"\.cnvindia(.*)", data)
    if matchObj:
        cnvindia = "aramteke kbidarka vatsal"
        message = matchObj.group().replace(".cnvindia", cnvindia)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))    
    
    # broadcast message to cnvcanada members
    matchObj = re.search(r"\.cnvcanada(.*)", data)
    if matchObj:
        cnvcanada = "dshchedr xlisovsk"
        message = matchObj.group().replace(".cnvcanada", cnvcanada)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to cnvfrance members
    matchObj = re.search(r"\.cnvfrance(.*)", data)
    if matchObj:
        cnvfrance = "dollierp "
        message = matchObj.group().replace(".cnvfrance", cnvfrance)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to virt members
    matchObj = re.search(r"\.virt(.*)", data)
    if matchObj:
        virt = "dshchedr kbidarka ipinto zpeng "
        message = matchObj.group().replace(".virt", virt)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to network members
    matchObj = re.search(r"\.network(.*)", data)
    if matchObj:
        network = "duyan myakove ysegev nkononov"
        message = matchObj.group().replace(".network", network)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to storage members
    matchObj = re.search(r"\.storage(.*)", data)
    if matchObj:
        storage = "kgoldbla ngavrilo qwang shiywang"
        message = matchObj.group().replace(".storage", storage)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to manage members
    matchObj = re.search(r"\.manage(.*)", data)
    if matchObj:
        manage = "gouyang rhrazdil igulina pbrilla"
        message = matchObj.group().replace(".manage", manage)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to ecosystem members
    matchObj = re.search(r"\.ecosystem(.*)", data)
    if matchObj:
        ecosystem = "ashoshan lbednar dollierp vparekh talayan"
        message = matchObj.group().replace(".ecosystem", ecosystem)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))

    # broadcast message to community members
    matchObj = re.search(r"\.community(.*)", data)
    if matchObj:
        community = "scolier karim jparrill rwsu ari fabiand jgriffith markllama"
        message = matchObj.group().replace(".community", community)
        s.send("PRIVMSG %s :%s\r\n" % (channel, message))
    # Debug
    # print(data)
