import random

def handle_response(message) -> str:
    p_message = message.upper()

    if p_message == 'HELLO':
        return 'Hey there!'
    
    if p_message == 'ROLL':
        return str(random.randint(1,6))
    
    if p_message == '!HELP':
        return "`This is a help message that you can modify.`"
    
    return p_message