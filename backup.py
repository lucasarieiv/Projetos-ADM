import os, shutil, datetime
from tkinter import *

def backup():
    user = os.getlogin()
    shutil.copy('produtos.txt', 'C:\\Users\\' + user + '\\OneDrive')
