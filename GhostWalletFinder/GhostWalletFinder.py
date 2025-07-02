#!/usr/bin/python
# -*- coding: utf-8 -*-

#BittWalletFinder an open source Bitcoin Seed Finder, if you are wondering why sometimes GhostWalletFinder is mentioned its because i changed the corny ass name...
#Developed by Deccatron and DigitalSamurai

from customtkinter import *
from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
import uuid
import sys
import os

def SeedFinder():
    print("Checking Seeds for Used Wallets")
    while True:
        id = uuid.uuid4()
        passphrase = Mnemonic().generate()
        w = Wallet.create(str(id), keys=passphrase, network='bitcoin')
        w.get_key()
        balance = w.balance()

        try:
            with open("live.txt", 'a', encoding="utf8") as f:
                print("SEED: " + str(passphrase) + " BALANCE: " + str(balance))
                if balance != 0.0:
                    print("SEED: " + str(passphrase) + " BALANCE: " + str(balance) + " Live")
                    try:
                        f.write("SEED: " + str(passphrase) + " BALANCE: " + str(balance) + "\n")
                    except:
                        print("Error writing to file")
                else:
                    print("DEAD: " + str(passphrase))
        except Exception as e:
            print("Error:", e)

def credits():
    app2 = CTk()
    app2.geometry('300x150')
    label2 = CTkLabel(app2, text='Developed by Deccatron and DigitalSamurai')
    label2.place(relx=0.5, rely=0.5, anchor='center')
    app2.mainloop()

def UI():
    app = CTk()
    app.geometry('300x300')
    app.title('GhostWalletFinder')
    label = CTkLabel(app, text='GhostWalletFinder GUI', font=("Helvetica", 20))
    label.place(relx=0.5, rely=0.275, anchor='center')
    button = CTkButton(app, text='Launch',
                       command=SeedFinder)
    button.place(relx=0.5, rely=0.5, anchor='center')
    button2 = CTkButton(app, text='Credits',
                        command=credits)
    button2.place(relx=0.5, rely=0.65, anchor='center')
    set_appearance_mode("dark")
    app.mainloop()

UI()
