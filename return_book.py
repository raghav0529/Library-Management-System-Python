import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import *
from tkinter import messagebox
from os import path

path1 = path.abspath(path.join(path.dirname(__file__), 'library-automation-c121b-firebase-adminsdk-4933x-8b068eb369.json'))

try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate(path1)
    firebase_admin.initialize_app(cred , {
        'databaseURL' : 'https://library-automation-c121b-default-rtdb.asia-southeast1.firebasedatabase.app/', 
    '   storageBucket': 'library-automation-c121b.appspot.com'
    })

ref = db.reference("/Book List/")
issue_ref = db.reference("/Issued Books/")

def return_book():
    try:
        return_input = entry1.get()
        book = issue_ref.order_by_child('book').equal_to(return_input).get()
        i = list(book.keys())[0]
        book_name = issue_ref.get()[i]['book']
        ref.child(book_name).update({'quantity':str(int(ref.get()[book_name]['quantity']) + 1)})
        issue_ref.child(i).delete()
        if int(ref.get()[book_name]['quantity']) > 0:
            ref.child(book_name).update({'availability':"Yes"})
        messagebox.showinfo("Information", "Book Successfully Returned")    
    except:
        messagebox.showerror("Error", "Please Try Again Later")


root = Tk()
root.geometry("900x450")

path2 = path.abspath(path.join(path.dirname(__file__), 'library.png'))
p1 = PhotoImage(file=path2)
root.iconphoto(False, p1)

root.title("Library")

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


Label(root, text = "Return Book", font = ("Helvetica 20 bold underline"), fg = "black").pack(pady=20, side = TOP, anchor = "n")
entry1 = Entry(root)
entry1.pack(side = TOP, anchor = "n")
button1 = Button(text = "Return Book", command = return_book).pack(pady = 10, side = TOP, anchor = "n")

root.mainloop()