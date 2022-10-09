import tkinter
import Repository

# -------------------------------------------------------------------#
def get_selected_row(event):
    global selected_book

    if len(list.curselection()) > 0:
        index = list.curselection()[0]
        selected_book = list.get(index)
        # title
        buchnameentry.delete(0, tkinter.END)
        buchnameentry.insert(tkinter.END, selected_book[1])
        # author
        authorentry.delete(0, tkinter.END)
        authorentry.insert(tkinter.END, selected_book[2])
        # year
        jahreentry.delete(0, tkinter.END)
        jahreentry.insert(tkinter.END, selected_book[3])
        # isbn
        ISBNentry.delete(0, tkinter.END)
        ISBNentry.insert(tkinter.END, selected_book[4])



def clear_list():
    list.delete(0, tkinter.END)


def fill_list(books):
    for book in books:
        list.insert(tkinter.END, book)


def view_command():
    clear_list()
    books = Repository.viewAll()
    fill_list(books)

def search_command():
    clear_list()
    books = Repository.search(txtBuchName.get(), txtAuthor.get(), txtJahre.get(), txtISBN.get())
    fill_list(books)

def insert_command():
    Repository.insert(txtBuchName.get(), txtAuthor.get(), txtJahre.get(), txtISBN.get())
    view_command()

def update_command():
    Repository.update(selected_book[0], txtBuchName.get(), txtAuthor.get(), txtJahre.get(), txtISBN.get())
    view_command()

def delete_command():
    Repository.delete(selected_book[0])
    view_command()

#--------------------MainFrame-----------------------------#
window = tkinter.Tk()
window.title('Bibliotek')
window.config(background= "lightgray")
window.geometry("400x350")
window.resizable(width=False, height=False)
#--------------------FrameEntry----------------------------------#

buchnamelbl = tkinter.Label(text="BuchName")
buchnamelbl.grid(row=0,column=0,padx=0)
jahrelbl = tkinter.Label(text="Jahre")
jahrelbl.grid(row=1,column=0,padx=0)
ISBNlbl = tkinter.Label(text="ISBN")
ISBNlbl.grid(row=0,column=3)
authorlbl = tkinter.Label(text="Author")
authorlbl.grid(row=1,column=3)
#------------------------ENTRY-----------------------------------#
txtBuchName = tkinter.StringVar()
buchnameentry = tkinter.Entry(textvariable=txtBuchName)
buchnameentry.grid(row=0,column=1)
txtJahre = tkinter.StringVar()
jahreentry = tkinter.Entry(textvariable=txtJahre)
jahreentry.grid(row=1,column=1)
txtISBN = tkinter.StringVar()
ISBNentry = tkinter.Entry(textvariable=txtISBN)
ISBNentry.grid(row=0,column=4)
txtAuthor = tkinter.StringVar()
authorentry = tkinter.Entry(textvariable=txtAuthor)
authorentry.grid(row=1,column=4)
#-----------------------LISTBox-----------------------------------#
list = tkinter.Listbox(window,width=40, height=20)
list.grid(row=2, column=0, rowspan=6, columnspan=2)
scrl1 = tkinter.Scrollbar(window)
scrl1.grid(row=2, column=2, rowspan=6,padx=10,pady=20)
list.configure(yscrollcommand=scrl1.set)
scrl1.configure(command=list.yview)
#----------------------BUTTON---------------------------------------#
viewbtn = tkinter.Button(window, text="ViewAll", command=view_command)
viewbtn.grid(row=2, column=3)
insertbtn = tkinter.Button(window, text="INSERT", command=insert_command)
insertbtn.grid(row=3, column=3)
deletebtn = tkinter.Button(window, text="DELETE", command=delete_command)
deletebtn.grid(row=4, column=3)
updatebtn = tkinter.Button(window, text="UPDATE", command=update_command)
updatebtn.grid(row=5, column=3)
searchbtn = tkinter.Button(window, text="SEARCH", command=search_command)
searchbtn.grid(row=6, column=3)

list.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()
