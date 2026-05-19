conversation_history=[]
def add_message(role,content):
    message={
        "role":role,
        "content":content
    }
    conversation_history.append(message)

def get_history():
    return conversation_history