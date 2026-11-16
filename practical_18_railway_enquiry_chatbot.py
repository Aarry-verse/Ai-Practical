# Practical 18: Railway Enquiry Chatbot

print("Railway Enquiry Chatbot")

while True:
    q = input("You: ").lower()

    if "train" in q:
        print("Bot: Trains are available on different routes.")
    elif "time" in q:
        print("Bot: Check the railway schedule for timings.")
    elif "ticket" in q:
        print("Bot: Book tickets through IRCTC.")
    elif "platform" in q:
        print("Bot: Check the station display for platform details.")
    elif "exit" in q:
        print("Bot: Thank you!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
