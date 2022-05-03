import streamlit as st
import tkinter
import tkinter as ttk
from tkinter import *

TUTORIAL_URL = "https://docs.streamlit.io/en/latest/tutorial/databases.html"

INTRO_IDENTIFIER = "—"

HOME_PAGE_TEXT = f""" ## Welcome to Capital Commission App!


 
 
root = tkinter.Tk()
root.title("Tk dropdown example")
 
# Add a grid
mainframe = tkinter.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable
tkvar = tkinter.StringVar(root)
 
# Dictionary with options
choices = { 'PYTHON','C','C++','PHP','JAVA'}
tkvar.set('PYTHON') # set the default option
 
popupMenu = tkinter.OptionMenu(mainframe, tkvar, *choices)
tkinter.Label(mainframe, text="Choose Programming Language").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
root.mainloop()
**Ready?**

👈 Choose the data source you want to access!
"""


def load_keyboard_class():
    st.write(
        """<style>
    .kbdx {
    background-color: #eee;
    border-radius: 3px;
    border: 1px solid #b4b4b4;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .2), 0 2px 0 0 rgba(255, 255, 255, .7) inset;
    color: #333;
    display: inline-block;
    font-size: .85em;
    font-weight: 700;
    line-height: 1;
    padding: 2px 4px;
    white-space: nowrap;
   }
   </style>""",
        unsafe_allow_html=True,
    )


def app():

    load_keyboard_class()

    st.write(HOME_PAGE_TEXT, unsafe_allow_html=True)
