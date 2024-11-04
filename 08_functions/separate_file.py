msgs = ['lol', 'lmao', 'rofl', 'jjjj']
sent_msgs = []

def send_messages():
    '''Print messages from list and moves them to a new list'''
    while msgs:
        current_msg = msgs.pop()
        print(current_msg)
        sent_msgs.append(current_msg)

send_messages()

print(msgs)
print(sent_msgs)
