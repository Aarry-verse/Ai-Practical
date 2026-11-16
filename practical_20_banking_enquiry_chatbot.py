# Practical 20: Banking Enquiry Chatbot

print("Banking Enquiry Chatbot")

while True:
    q = input("You: ").lower()

    if "balance" in q:
        print("Bot: Check your balance using mobile banking.")
    elif "loan" in q:
        print("Bot: Contact the bank for loan details.")
    elif "account" in q:
        print("Bot: Visit the bank to open an account.")
    elif "timing" in q:
        print("Bot: Bank working hours are 10 AM to 4 PM.")
    elif "exit" in q:
        print("Bot: Thank you!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
