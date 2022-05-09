from well_selector import WellSelector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ctypes import windll
from tkinter.tix import *
import os
import argparse

#Testing how to import WellSelector
#This fixes grainy widgets
windll.shcore.SetProcessDpiAwareness(1)

root = Tk()



app = WellSelector(root,"8x12","Hej","Du der")


