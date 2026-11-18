import sqlite3
import tkinter as tk
from tkinter import ttk
import database as db



root = tk.Tk()
root.title("SQLite Database Viewer")

tree = ttk.Treeview(root, columns=("ID", "username", "Password"))
tree.pack()

tree.column("ID", width=100, anchor="center")
tree.column("username", width=200, anchor="center")
tree.column("Password", width=100, anchor="center")


tree.heading("ID", text="ID")
tree.heading("username", text="username")
tree.heading("Password", text="Password")


for row in db.view_all():
    tree.insert("", "end", values=row)

root.mainloop()

