import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pyrebase
from PIL import Image

try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate('library-automation-c121b-firebase-adminsdk-4933x-8b068eb369.json')
    firebase_admin.initialize_app(cred , {
        'databaseURL' : 'https://library-automation-c121b-default-rtdb.asia-southeast1.firebasedatabase.app/', 
    '   storageBucket': 'library-automation-c121b.appspot.com'
    })

ref = db.reference("/Book List/")

firebaseConfig = {"apiKey": "AIzaSyBMryd1nTKNDtVFNTVOMzYr8qkmQBncihA",
  "authDomain": "library-automation-c121b.firebaseapp.com",
  "databaseURL": "https://library-automation-c121b-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "library-automation-c121b",
  "storageBucket": "library-automation-c121b.appspot.com",
  "messagingSenderId": "947173452722",
  "appId": "1:947173452722:web:a75dee1de0479ff12a52ab",
  "measurementId": "G-6SNQV9KJND"}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def add_book():

    try:
        # f_types = [('Jpg Files', '*.jpg')]
        # basewidth = 100
        # filename = filedialog.askopenfilename(filetypes=f_types, title = "Select Book Image")
        # image = Image.open(filename)
        # wpercent = (basewidth/float(image.size[0]))
        # hsize = int((float(image.size[1]) * float(wpercent)))
        # image = image.resize((basewidth,hsize), Image.ANTIALIAS)
        # image.save(fp = filename)

        name = name1.get()
        author = author1.get()
        quantity = quantity1.get()
        description = description1.get()
        availability = availability1.get()

        if name != "" and author != "" and quantity != "" and description != "" and availability != "":
            # storage.child("Book Image/"+name).put(filename)
            # photo_link = storage.child("book image/"+name).get_url(None)

            data = {'name':name,'author':author,'quantity':quantity, 'description':description, 'availability':availability}
            ref.child(name).set(data)
            messagebox.showinfo("Information", "Book Added")
        else:
            messagebox.showerror("Error", "Please Fill in All Details")    
    except:
        messagebox.showerror("Error", "Please Try Again Later")


root = Tk()
root.title("Library")
root.geometry("900x450")

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


menubar = Menu(root)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label = 'Main Page', command = mainPage)
file.add_command(label ='Help', command = lambda:messagebox.showinfo("Information", "For help contact following email:\nraghav.7920@stmarysdelhi.org"))
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
  
add_book_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Add Book', menu = add_book_menu)
add_book_menu.add_command(label ='Add Book', command = add_bookPage)

issue_book_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Issue Book', menu = issue_book_menu)
issue_book_menu.add_command(label ='Issue by Name', command = issue_namePage)
issue_book_menu.add_command(label = 'Issue by Author', command = issue_authorPage)
issue_book_menu.add_command(label = 'Issue Available Books', command = issue_availPage)

return_book_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Return Book', menu = return_book_menu)
return_book_menu.add_command(label ='Return Book', command = returnPage)
root.config(menu = menubar)


Label(root, text = "Add Book", font = ("Helvetica 20 bold underline"), fg = "black").pack(pady=20, side = TOP, anchor = "n")

name1 = Entry(root, width = 40)
name1.insert(0, "Enter Book Name")
name1.pack(pady = 10, side=TOP, anchor = "n")

author1 = Entry(root, width = 40)
author1.insert(0, "Enter Book Author")
author1.pack(pady = 10, side=TOP, anchor = "n")

quantity1 = Entry(root, width = 40)
quantity1.insert(0, "Enter Book Quantity")
quantity1.pack(pady=10, side=TOP, anchor = "n")

description1 = Entry(root, width = 40)
description1.insert(0, "Book Description")
description1.pack(ipady = 40, pady = 10, side=TOP, anchor = "n")

availability1 = StringVar(value = "1")
Label(root, text = "Book Availability:", font = ("Helvetica 10"), fg = "black").pack(side = TOP, anchor = "n")
r = Radiobutton(root, text = "Yes", value = "Yes", variable = availability1)
r.select()
r.pack(side = TOP, anchor = "n")
r = Radiobutton(root, text = "No", value = "No", variable = availability1)
r.pack(side = TOP, anchor = "n")

Button(root, text = "Add Book to Database", width = 30, command = lambda:add_book()).pack(pady = 10, side = TOP, anchor = "n")

root.mainloop()