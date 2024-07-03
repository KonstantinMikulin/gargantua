from datetime import datetime

text = '40.01.1984'

print(f'text: {text}')

try:
    datetime.strptime(text, "%d.%m.%Y")
    
except ValueError:
    print(f'except: False')
else:
    dob = list(map(int, text.split('.')))
    if all([1 <= dob[0] <= 31, 1 <= dob[1] <= 12, 1924 <= dob[2] <= 2006]):
        print('True')
    else:
        print(f'else: False')
        

