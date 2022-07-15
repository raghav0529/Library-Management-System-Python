from tkinter import *
from PIL import Image
from PIL import ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import filedialog
from tkinter import messagebox
from tkinter.simpledialog import askstring
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

def issue_book():
    book_name = askstring('Issue Book', 'Reconfirm Book Name:', parent = root)
    issue_input = book_name
    book = ref.get()
    quantity = book[book_name]['quantity']
    if int(quantity) <= 0:
        messagebox.showerror("Error", "Book Not Available")
    else:
        try:
            student_admno = askstring('Issue Book', 'Enter Student Admission Number:', parent = root)
            data = {'book':issue_input, 'admission no':student_admno}
            issue_ref.push(data)
            ref.child(issue_input).update({'quantity':str(int(book[issue_input]['quantity']) - 1)})
            if int(ref.get()[issue_input]['quantity']) == 0:
                ref.child(issue_input).update({'availability':"No"})
            messagebox.showinfo("Information", "Book Issued")

        except:
            messagebox.showerror("Error", "Please Try Again Later")

def book_name_search():
    for widgets in frameMain.winfo_children():
        widgets.destroy()

    book_name_input = entry1.get()
    book = ref.get()
    sorted_dict = {}
    for i in list(book.keys()):
        string_count = len(book_name_input)
        if str(book[i]['name'])[:string_count].lower() == book_name_input.lower():
            sorted_dict[i]=book[i]
    coulumn_num = 1
    row_num = 1
    for i in list(sorted_dict.keys()):
        name = book[i]['name']
        author = book[i]['author']
        quantity = book[i]['quantity']
        availability = book[i]['availability']
        description = book[i]['description']
        if len(description) > 30:
            small_length = int(len(description)/2)
            description = description[:small_length] + "\n" + description[small_length:int(len(description))]
        
        frame = Frame(frameMain, highlightbackground= "black", highlightthickness= 2)
        frame.grid(column = coulumn_num, row = row_num, padx = 5, pady = 5)
        Label(frame, text = "Name").grid(row = 2, column = 1)
        Label(frame, text= name).grid(row = 2, column = 2)
        Label(frame, text = "Author").grid(row = 3, column = 1)
        Label(frame, text= author).grid(row = 3, column = 2)
        Label(frame, text = "Current Quantity").grid(row = 4, column = 1)
        Label(frame, text= quantity).grid(row = 4, column = 2)
        Label(frame, text = "Availability").grid(row = 5, column = 1)
        Label(frame, text= availability).grid(row = 5, column = 2)
        Label(frame, text = "Description").grid(row = 6, column = 1)
        Label(frame, text= description).grid(row = 6, column = 2)
        Button(frame, text = "Issue Book", width = 20, command = lambda:issue_book()).grid(column=1, row = 7, columnspan= 2, rowspan= 1, pady = 4)

        coulumn_num += 1
        if coulumn_num == 3:
            coulumn_num = 1
            row_num += 1

root = Tk()
root.title("Library")

path2 = path.abspath(path.join(path.dirname(__file__), 'library.png'))
p1 = PhotoImage(file=path2)
root.iconphoto(False, p1)

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


Label(root, text = "Issue Book", font = ("Helvetica 20 bold underline"), fg = "black").pack(pady=5, side = TOP, anchor = "n")
Label(root, text = "Search By Name", font = ("Helvetica 10 underline"), fg = "black").pack(side = TOP, anchor = "n")

entry1 = Entry(root, width = 40)
entry1.insert(0, "Enter Book Name")
entry1.pack(pady = 25, side=TOP, anchor = "n")
button1 = Button(text = "Find Book", command = book_name_search).pack(side = TOP, anchor = "n")

frameMain = Frame(root)
frameMain.pack(side = TOP, anchor = N, padx = 10)

root.mainloop()