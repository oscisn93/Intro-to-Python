messages = [
    "Hi",
    "Hello",
    "wyd?",
    "not much,hby?",
    "just chillen"
]
sent_messages = []
def send_messages(msgs):
    for msg in msgs:
        sent_messages.append(msg)
        print("Message:",msg)
        
send_messages(messages)
print("Original:\t",messages)
print("Copy:\t\t",sent_messages)
