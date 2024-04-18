import random

def random_event(probability):
    return random.random() < probability

def event_handler():
    if random_event(0.1):  # 1/10 chance
        print("Event 1 occurred!")
    elif random_event(0.05):  # 1/20 chance
        print("Event 2 occurred!")
    else:
        print("No event occurred.")

# Test the event handler
for _ in range(10):
    event_handler()
