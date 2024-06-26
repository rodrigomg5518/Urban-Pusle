import sqlite3
from bs4 import BeautifulSoup  # type: ignore
import tkinter as tk
from tkinter import messagebox

# Define the paths to the HTML files
html_files = {
    'index': '/mnt/data/UrbanPulse_extracted/UrbanPulse/index.html',
    'reportesref': '/mnt/data/UrbanPulse_extracted/UrbanPulse/Erick/reportesref.html',
    'register': '/mnt/data/UrbanPulse_extracted/UrbanPulse/Samantha/Register.html',
    'denuncias': '/mnt/data/UrbanPulse_extracted/UrbanPulse/Eduardo/denuncias/denuncias.html'
}

db_name = 'urban_pulse.db'

def create_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Index (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ReportesRef (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Register (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Denuncias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    );
    ''')
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Database and tables created successfully.")

def extract_data_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
            # Example extraction logic (modify according to your HTML structure)
            title = soup.title.string if soup.title else 'No Title'
            content = soup.body.get_text(separator='\n') if soup.body else 'No Content'
            
            return title, content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return "No Title", "No Content"

def insert_data():
    for name, path in html_files.items():
        title, content = extract_data_from_html(path)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute(f'''
            INSERT INTO {name.capitalize()} (title, content)
            VALUES (?, ?)
        ''', (title, content))
        
        conn.commit()
        conn.close()
    messagebox.showinfo("Success", "Data inserted successfully.")

def fetch_data():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    tables = ['Index', 'ReportesRef', 'Register', 'Denuncias']
    all_data = ""
    
    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        all_data += f"Data from {table}:\n"
        for row in rows:
            all_data += f"{row}\n"
        all_data += "\n"
    
    conn.close()
    messagebox.showinfo("Data", all_data)

# Creating the GUI
root = tk.Tk()
root.title("Urban Pulse Database")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

create_db_button = tk.Button(frame, text="Create Database", command=create_database)
create_db_button.grid(row=0, column=0, padx=10, pady=10)

insert_data_button = tk.Button(frame, text="Insert Data", command=insert_data)
insert_data_button.grid(row=0, column=1, padx=10, pady=10)

fetch_data_button = tk.Button(frame, text="Fetch Data", command=fetch_data)
fetch_data_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
