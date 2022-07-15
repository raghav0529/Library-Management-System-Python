import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import *
from os import path

path1 = path.abspath(path.join(path.dirname(__file__), 'library-automation-c121b-firebase-adminsdk-4933x-8b068eb369.json'))

try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate(path1)
    firebase_admin.initialize_app(cred , {
        'databaseURL' : 'https://library-automation-c121b-default-rtdb.asia-southeast1.firebasedatabase.app/', 
        'storageBucket': 'library-automation-c121b.appspot.com'
    })

def add_bookPage():
    root.destroy()
    import add_book
def mainPage():
    root.destroy()
    import main
def issue_authorPage():
    root.destroy()
    import issue_by_author
def issue_namePage():
    root.destroy()
    import issue_by_name
def issue_availPage():
    root.destroy()
    import issue_by_available     
def returnPage():
    root.destroy()
    import return_book

root = Tk()
root.title("Library")

path2 = path.abspath(path.join(path.dirname(__file__), 'library.png'))
p1 = PhotoImage(file=path2)
root.iconphoto(False, p1)

root.geometry("900x450")

Label(root, text = "St. Mary's Library", font = ("Helvetica 20 bold underline"), fg = "black").pack(pady=20, side = TOP, anchor = "n")

Button(root, text = "Add Book", width = 30, command = lambda:add_bookPage()).pack(pady = 10, side = TOP, anchor = "n")
Button(root, text = "Issue Book by Name", width = 30, command = lambda:issue_namePage()).pack(pady = 10, side = TOP, anchor = "n")
Button(root, text = "Issue Book by Author", width = 30, command = lambda:issue_authorPage()).pack(pady = 10, side = TOP, anchor = "n")
Button(root, text = "Issue Available Books", width = 30, command = lambda:issue_availPage()).pack(pady = 10, side = TOP, anchor = "n")
Button(root, text = "Return Book", width = 30, command = lambda:returnPage()).pack(pady = 10, side = TOP, anchor = "n")

root.mainloop()