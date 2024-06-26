import sqlite3

# Function to create a database and tables
def create_database(db_name):
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

# Main logic
db_name = 'urban_pulse.db'
create_database(db_name)
print("Database and tables created successfully.")