# Define a dictionary of patterns
patterns = {}
import re
keywords={'goodbye': ['bye', 'farewell'], 
'greet': ['hello', 'hi', 'hey'], 'thankyou': ['thank', 'thx']}
 
responses= {'default': 'default message',
 'goodbye': 'goodbye for now',
 'greet': 'Hello you! :)',
 'thankyou': 'you are very welcome'}
# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

# Print the patterns
print(patterns)

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")