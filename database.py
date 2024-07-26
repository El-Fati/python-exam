import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database 
import sqlite3

def connect_db():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                 (id INTEGER PRIMARY KEY, name TEXT, balance REAL, account_type TEXT)''')
    conn.commit()
    return conn

def add_account(name, balance, account_type):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO accounts (name, balance, account_type) VALUES (?, ?, ?)", 
              (name, balance, account_type))
    conn.commit()
    conn.close()

def get_accounts():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    accounts = c.fetchall()
    conn.close()
    return accounts

def update_account(id, name, balance, account_type):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE accounts SET name = ?, balance = ?, account_type = ? WHERE id = ?", 
              (name, balance, account_type, id))
    conn.commit()
    conn.close()

def delete_account(id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM accounts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
