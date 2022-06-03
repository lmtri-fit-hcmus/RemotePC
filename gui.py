from ast import arg
from base64 import encode
from http import client
from lib2to3.pgen2 import driver
from operator import index
from pdb import Restart
import socket
from sqlite3 import Cursor
import string
import threading
from typing import ItemsView
import pyodbc
from http import server
import tkinter as tk
from tkinter import ttk 
from tkinter.ttk import *
import socket
from tkinter.ttk import Label
from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import Tk, Button, Canvas
from PIL import Image, ImageFont
from matplotlib import image
from time import time, sleep

import Main
import ReceiveEmail

client_address = "client1.computernetwork@gmail.com"


client_pass="computernetwork" #unsecure

    #    Hàm hiển thị danh sách các máy client
class HomePage(tk.Frame):
    def __init__(self,parent, appController):
        tk.Frame.__init__(self, parent)

    #self.pack(side=tk.LEFT, padx=20)
        self.tv=ttk.Treeview(self)

        # Define our columns
        self.tv['column']=("Message Number","From","To","Subject","Date", "State")
        
        # Formate our columns
        self.tv.column("#0",width=0,stretch=NO)
        self.tv.column("Message Number",anchor=W,width=150)
        self.tv.column("From",anchor=W,width=200)
        self.tv.column("To",anchor=W,width=200)
        self.tv.column("Subject",anchor=W,width=200)
        self.tv.column("Date",anchor=W,width=150)
        self.tv.column("State",anchor=W,width=75)
        
        # Create heading
       # tv.heading("#0",text="ID",anchor=CENTER)
        self.tv.heading("Message Number",text="Message Number",anchor=CENTER)
        self.tv.heading("From",text="From",anchor=CENTER)
        self.tv.heading("To",text="To",anchor=CENTER)
        self.tv.heading("Subject",text="Subject",anchor=CENTER)
        self.tv.heading("Date",text="Date",anchor=CENTER)
        self.tv.heading("State",text="State",anchor=CENTER)
        
       
        label_title=tk.Label(self, text="UNREAD MAIL",font="Arial,45")
        label_title.pack()

        self.appController = appController
        self.parent = parent

        button_refresh=tk.Button(self,text="Run",command=lambda: self.Run(list_sub = appController.sub_list, detail_list = appController.detail_list))
        button_refresh.pack()

       

        s=ttk.Style()
        s.theme_use('clam')

        # Add the rowheight
        s.configure('Treeview', rowheight=80)

   
    def Run( self,list_sub, detail_list):
        c = 0
        d = 0
        for i in list_sub:
        #Xử lý các title tương ứng
            Main.Handling(i)
            l = len(detail_list)
            detail = detail_list[d]
            selected_item = self.tv.get_children()[l-1-c]
            self.tv.item(selected_item,values=(detail[0],detail[1],detail[2],detail[3],detail[4], "Done"))
            
            items = []
            lists = []
            for child in self.tv.get_children():
                items.append(self.tv.item(child)["values"])
                lists.append(child)
            self.tv.delete(*self.tv.get_children())
            temp = 0
            for item in items:
                self.tv.insert(parent = '',index= 'end', text="",values=(item[0],item[1],item[2],item[3],item[4],item[5]))
                temp+=1
            self.update()
            c+=1
            d+=1
        print("Read")
        list_sub, detail_list =ReceiveEmail.ReceiveEmail(client_address,client_pass)
        for detail in detail_list:
            self.tv.insert(parent = '',index= 0,text="",values=(detail[0],detail[1],detail[2],detail[3],detail[4], "Unread"))
        self.after(1000, self.Run(list_sub, detail_list))
        
        

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Remote Control")
        self.geometry("1000x600")
        self.resizable(width=True, height=True)

        container=tk.Frame()
        container.configure(bg="red")
       
        container.pack()

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        frame=HomePage(container, self)
        frame.grid(row=0,column=0,sticky="nsew")
        self.frame=frame


      

        self.sub_list, self.detail_list = ReceiveEmail.ReceiveEmail(client_address,client_pass)

        for detail in self.detail_list:
            self.frame.tv.insert(parent = '',index=0,text="",values=(detail[0],detail[1],detail[2],detail[3],detail[4], "Unread"))
    
        # self.run = Main.run()
        # Pack to the screen
        self.frame.tv.pack(pady=20)
        self.frame.tkraise()

 

    def resize(self,curFrame,w,h):
        self.geometry(f"{w}x{h}")
 

def main():
    app=App()
    #app.showPage(HomePage)
    app.mainloop()

if __name__ == "__main__":
    main()
