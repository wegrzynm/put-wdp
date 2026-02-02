# vulnerable_app.py - KOD DO ANALIZY (NIE URUCHAMIAJ!)

import sqlite3
import hashlib

def login(username, password):
    """Authenticate user and return True if valid."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Check credentials
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    return result is not None


def register(username, password):
    """Register a new user."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Store user
    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{hashed}')")
    conn.commit()
    
    print(f"User {username} registered with password hash: {hashed}")
    return True


def change_password(username, old_password, new_password):
    """Change user password."""
    if login(username, old_password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        hashed = hashlib.md5(new_password.encode()).hexdigest()
        cursor.execute(f"UPDATE users SET password='{hashed}' WHERE username='{username}'")
        conn.commit()
        return True
    return False


def get_user_data(user_id):
    """Get user data by ID."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchone()


PASSWORD_REQUIREMENTS = {
    'min_length': 4,
    'require_special': False,
    'require_uppercase': False
}


def validate_new_password(password):
    """Validate password meets requirements."""
    if len(password) >= PASSWORD_REQUIREMENTS['min_length']:
        return True
    return False