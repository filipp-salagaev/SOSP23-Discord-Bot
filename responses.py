import random
import math

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hey there!"
    
    if p_message == "roll dice":
        return str(random.randint(1, 6))
    
    if "multiply" in p_message:
        return int(p_message.split(' ')[0]) * int(p_message.split(' ')[2])
    
    if "natlog" in p_message:
        return math.log(int(p_message.split(' ')[1]))
    
