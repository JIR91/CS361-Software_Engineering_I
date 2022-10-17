#!/usr/bin/env python3
# coding=utf-8

from tkinter import *


class WINDOW_FRAME():
    def __init__(self, control, win):
        self.win = win
        self.control =control
        win.title("Item Finder")
        win.geometry("600x600")
        win.resizable(False, False)

        self.user_input = StringVar()

        self.first_frame = Frame(win)
        self.first_frame.pack()
        self.intruction_frame = Frame(self.first_frame).pack()

        
        self.result_frame = Frame(self.win)
        self.link_frame = Frame(self.win)

        Label(self.first_frame, text='Welcome!', font=("Freestyle Script", 60), pady=100).pack()
        Label(self.first_frame, text='Search Web for The Cheapest Price.', font=("Freestyle Script", 30)).pack()
        Label(self.first_frame, text='\nYour Search Ends Here', font=('Arial', 12), pady=25).pack()
        
        self.search_box = Entry(self.first_frame, width=70, textvariable=self.user_input, borderwidth=10)
        self.search_box.bind('<Return>',control.user_input)
        self.search_box.pack()

    def display_search_results(self):
        self.first_frame.pack_forget()
        self.search_box = Entry(self.result_frame, width=70, textvariable=self.user_input, borderwidth=10)
        self.search_box.pack(side=TOP,pady=15)
        
        Label(self.result_frame, text="Links below\t\t\tCost", font=('Arial', 18)).pack(pady=10)
        self.links = Label(self.link_frame, font=('Arial', 15))

        self.result_frame.pack()
        self.links.pack()
        self.link_frame.pack()

    def display_links(self, user_input): 
        display_text =''
        for i in user_input:
            display_text += i + '\t\t\t\t\t $0.00\n'
        
        self.links.config(text=display_text)
