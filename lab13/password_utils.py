"""
Password utilities module for security applications.
This module contains functions for password validation and hashing.
"""
import hashlib
import re


def check_password_strength(password: str) -> str:
    """
    Check password strength and return category.
    
    Args:
        password: The password to check
        
    Returns:
        'Weak', 'Medium', or 'Strong'
        
    Raises:
        ValueError: If password is empty or None
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def hash_password(password: str, algorithm: str = "sha256") -> str:
    """
    Hash a password using specified algorithm.
    
    Args:
        password: The password to hash
        algorithm: Hash algorithm ('sha256', 'sha512', 'md5')
        
    Returns:
        Hexadecimal hash string
        
    Raises:
        ValueError: If password is empty or algorithm unsupported
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    supported = ['sha256', 'sha512', 'md5']
    if algorithm not in supported:
        raise ValueError(f"Unsupported algorithm. Use: {supported}")
    
    if algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        return hashlib.md5(password.encode()).hexdigest()


def is_common_password(password: str) -> bool:
    """
    Check if password is in the list of common passwords.
    
    Args:
        password: The password to check
        
    Returns:
        True if password is common, False otherwise
    """
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "qwerty", "abc123", "111111",
        "password1", "admin", "letmein", "welcome", "monkey",
        "dragon", "master", "login", "princess", "qwerty123"
    ]
    return password.lower() in common_passwords


def validate_password(password: str) -> dict:
    """
    Comprehensive password validation.
    
    Args:
        password: The password to validate
        
    Returns:
        Dictionary with validation results:
        {
            'valid': bool,
            'strength': str,
            'is_common': bool,
            'errors': list[str]
        }
    """
    result = {
        'valid': True,
        'strength': 'Unknown',
        'is_common': False,
        'errors': []
    }
    
    if not password:
        result['valid'] = False
        result['errors'].append("Password cannot be empty")
        return result
    
    if len(password) < 8:
        result['valid'] = False
        result['errors'].append("Password must be at least 8 characters")
    
    if is_common_password(password):
        result['valid'] = False
        result['is_common'] = True
        result['errors'].append("Password is too common")
    
    try:
        result['strength'] = check_password_strength(password)
    except ValueError as e:
        result['errors'].append(str(e))
    
    return result


def generate_password_hash(password: str, salt: str = "") -> str:
    """
    Generate a salted password hash.
    
    Args:
        password: The password to hash
        salt: Optional salt value
        
    Returns:
        Salted SHA-256 hash
    """
    salted = salt + password + salt
    return hashlib.sha256(salted.encode()).hexdigest()
