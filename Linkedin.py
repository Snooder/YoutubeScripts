import pyautogui
import sys
import requests
#import urllib.requests
import time
from bs4 import BeautifulSoup
import random


def readconnectionfile():
    connfile = open("linkedinaccounts.txt",'r')
    connections = []
    accounts = connfile.read().split("\n")
    for x in range(0,len(accounts)-1):
        username = accounts[x].split(" ")
        connections.append((username[0], username[1]))

    return connections

#Leftover code from Instagram project
#The 0 and 1 are used to identify if I had already messaged.
#Sometimes the bot will lag behind and need to restart
def writeconnectionfile(connections):
    connfile = open("linkedinaccounts.txt",'w')
    for i in connections:
        connfile.write(i + " 0\n")

#This is to keep a record of who you talked to already
def writeaccountsfile(account):
    connfile = open("linkedinaccountsmessaged.txt",'w')
    connfile.write(account + " 1\n")


def sendsolicitation(connections):
    for x in range(0, len(connections)-1):
        #print(connections[x])
        print(connections[x][0])
        print(connections[x][1])

        #This check to see if I messaged them already
        if(connections[x][1] == '0'):
            pyautogui.moveTo(265, 220)
            pyautogui.click()
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(300, 225)
            pyautogui.click()
            pyautogui.write(connections[x][0], interval=0.05)
            pyautogui.moveTo(430,425)
            time.sleep(5)
            pyautogui.moveTo(430, 175)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(440,820)
            pyautogui.click()
            pitch = solicitationtext()
            pyautogui.write(pitch)
            pyautogui.press("enter")
            writeaccountsfile(connections[x][0])
            time.sleep(5)
        elif(connections[x][1] == 'jerseypickz1' or connections[x][1] == 'nypickz'):
            continue;
        else:
            continue;

def solicitationtext():
    openings = ["Hey boss ", "Good afternoon ", "Hi ", "Hope you are doing well, "]
    pitches = [
    "are you interested in developing a website for your sports picks business? I can make a really nice looking subscription based platform to handle daily, weekly, monthly and so on customers. ",
    "would you be interested in hiring someone to make you a subscription website for your business. My strengths are in the ability to make a subscription based website that only allows users that purchased a timed-package to view your content. ",
    "have you considered the possibility that having your own website for your business would gain you more traffic for your sports picks business? I am a very experienced website developer and can make you a great looking website for your company. "
    ]
    pitches2 = [
    "The website management for you is incredibly simple, a simple log in to the webhosting platform, all you need to do is drag and drop your picks for the day and you're done. "
    "I have had 4 previous clients that were thrilled with my service and their websites have been growing ever since. ",
    ]
    pricing = ["My rates are fairly priced in regards to how much money will be automated to your bank account and the technology that I am offering. My going rate is 150$ to set up the website start to finish, half is due before I start working and the other half is due once the designing is finished. "]
    references = ["If you'd like to see some of my work, just ask ",
    "If you are interested in seeing my portfolio, just ask "]

    openingpick = random.randrange(0,3)
    pitchespick = random.randrange(0,2)
    pitches2pick = random.randrange(0,1)
    referencespick = random.randrange(0,1)
    fullpitch = str(openings[openingpick]) + str(pitches[pitchespick]) + str(pricing[0]) + str(references[referencespick])
    print(fullpitch)
    return fullpitch

#response = requests.get(url)

#soup = BeautifulSoup(response.text, 'html.parser')

#soup.findAll('<li>')
#print(soup)

#homiecircle = ['Deiv Shanmugasundaram','Warren Choi', 'Daniel Fraley']
#first = 0


connections = readconnectionfile()
print(connections)
sendsolicitation(connections)
