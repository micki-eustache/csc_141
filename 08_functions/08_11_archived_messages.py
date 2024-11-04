msgs = ['lol', 'lmao', 'rofl', 'jjjj']
sent_msgs = []

def send_messages(msgs, sent_msgs):
    '''Print messages from list and moves them to a new list'''
    while msgs:
        current_msg = msgs.pop()
        print(current_msg)
        sent_msgs.append(current_msg)

send_messages(msgs[:], sent_msgs)

print(msgs)
print(sent_msgs)
