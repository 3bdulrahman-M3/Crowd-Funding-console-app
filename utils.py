import re
from datetime import datetime

def validate_phone_number(phone):
    return bool(re.fullmatch(r"01[0-9]{9}", phone))

def validate_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email))

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None 