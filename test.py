from time import sleep

start_text = {
    'step_1': 'Hello {username}',
    'step_2': 'This bot can save your weight and body measurments',
    'step_3': '''You can send /help for command`s list
    You can send /instruction for how to use bot
    '''
}

def start_text_printer(text: dict):
    for chunk in text:
        sleep(2)
        yield str(chunk)
    
    
print(start_text_printer(start_text))
