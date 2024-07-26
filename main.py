import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bank Management System")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.label = customtkinter.CTkLabel(self, text="Bank Management System", font=("Arial", 20))
        self.label.pack(pady=20)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Name", "Balance", "Account Type"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Balance", text="Balance")
        self.tree.heading("Account Type", text="Account Type")
        self.tree.pack(pady=20, padx=20, fill="both", expand=True)

        self.load_data()

        self.add_button = customtkinter.CTkButton(self, text="Add Account", command=self.add_account)
        self.add_button.pack(side=LEFT, padx=20, pady=10)

        self.update_button = customtkinter.CTkButton(self, text="Update Account", command=self.update_account)
        self.update_button.pack(side=LEFT, padx=20, pady=10)

        self.delete_button = customtkinter.CTkButton(self, text="Delete Account", command=self.delete_account)
        self.delete_button.pack(side=LEFT, padx=20, pady=10)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for row in database.get_accounts():
            self.tree.insert("", "end", values=row)

    def add_account(self):
        self.popup = customtkinter.CTkToplevel(self)
        self.popup.title("Add Account")

        self.name_label = customtkinter.CTkLabel(self.popup, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = customtkinter.CTkEntry(self.popup)
        self.name_entry.pack(pady=5)

        self.balance_label = customtkinter.CTkLabel(self.popup, text="Balance:")
        self.balance_label.pack(pady=5)
        self.balance_entry = customtkinter.CTkEntry(self.popup)
        self.balance_entry.pack(pady=5)

        self.account_type_label = customtkinter.CTkLabel(self.popup, text="Account Type:")
        self.account_type_label.pack(pady=5)
        self.account_type_entry = customtkinter.CTkEntry(self.popup)
        self.account_type_entry.pack(pady=5)

        self.submit_button = customtkinter.CTkButton(self.popup, text="Add", command=self.submit_add)
        self.submit_button.pack(pady=20)

    def submit_add(self):
        name = self.name_entry.get()
        balance = self.balance_entry.get()
        account_type = self.account_type_entry.get()
        if name and balance and account_type:
            database.add_account(name, float(balance), account_type)
            self.load_data()
            self.popup.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def update_account(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item, "values")
            self.popup = customtkinter.CTkToplevel(self)
            self.popup.title("Update Account")

            self.name_label = customtkinter.CTkLabel(self.popup, text="Name:")
            self.name_label.pack(pady=5)
            self.name_entry = customtkinter.CTkEntry(self.popup)
            self.name_entry.insert(0, item[1])
            self.name_entry.pack(pady=5)

            self.balance_label = customtkinter.CTkLabel(self.popup, text="Balance:")
            self.balance_label.pack(pady=5)
            self.balance_entry = customtkinter.CTkEntry(self.popup)
            self.balance_entry.insert(0, item[2])
            self.balance_entry.pack(pady=5)

            self.account_type_label = customtkinter.CTkLabel(self.popup, text="Account Type:")
            self.account_type_label.pack(pady=5)
            self.account_type_entry = customtkinter.CTkEntry(self.popup)
            self.account_type_entry.insert(0, item[3])
            self.account_type_entry.pack(pady=5)

            self.submit_button = customtkinter.CTkButton(self.popup, text="Update", command=lambda: self.submit_update(item[0]))
            self.submit_button.pack(pady=20)
        else:
            messagebox.showwarning("Selection Error", "Please select an account to update")

    def submit_update(self, id):
        name = self.name_entry.get()
        balance = self.balance_entry.get()
        account_type = self.account_type_entry.get()
        if name and balance and account_type:
            database.update_account(id, name, float(balance), account_type)
            self.load_data()
            self.popup.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def delete_account(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item, "values")
            database.delete_account(item[0])
            self.load_data()
        else:
            messagebox.showwarning("Selection Error", "Please select an account to delete")

if __name__ == "__main__":
    app = App()
    app.mainloop()
