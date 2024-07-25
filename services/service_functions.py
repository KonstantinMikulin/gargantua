from datetime import datetime


# function to convert dict with date of birth to str
def convert_dob(date: dict) -> str:
    date_obj = datetime(date['year'], date['month'], date['day'])
    date_str = date_obj.strftime('%d-%m-%Y')
    
    return date_str

data = {'day': 1, 'month': 1, 'year': 1984}

print(convert_dob(data))
