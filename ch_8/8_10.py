messages = [
    "Hi",
    "Hello",
    "wyd?",
    "not much,hby?",
    "just chillen"
]
sent_messages = []
def send_messages(msgs):
    for i in range(0, len(msgs)):
        sent_messages.append(msgs[0])
        print("Message:",msgs[0])
        msgs.remove(msgs[0])

send_messages(messages)

print("Original:\t",messages)
print("Copy:\t\t",sent_messages)
