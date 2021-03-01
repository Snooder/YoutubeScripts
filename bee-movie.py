# -*- coding: utf-8 -*-
import pyautogui
import sys

path = "bee-movie.txt"
script = open(path, 'r')
words = script.read().split('.')
coor = (530,445) #imessage top right corner of screen
ninja = "THE FUCK YOU SAY TO ME YOU LITTLE SHIT? AHAHAHAHAHAHA! How are you- how are you not in fucking school? You kiss your mother with that mouth? It’s called you- it’s called you kiss your mother with that fucking mouth? Huh? Huh? AHAHAH he so AHAH AH AHAHAHAHA- because the fucking youth of society- AYAHAHAHAHA AHAYAYO- YOU SHUT UP WHEN I’M TALKING TO YOU- YOU SHUT YOUR MOUTH!"
ninja = ninja.split('?')
guerilla = "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
guerilla = guerilla.split(' ')

for word in words:
    pyautogui.moveTo(coor)
    pyautogui.click()
    pyautogui.write(word, interval=0.00005)
    pyautogui.press('enter');
    print(word)
