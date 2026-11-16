# Practical 17: Hospital Enquiry Chatbot

print("Hospital Enquiry Chatbot")

while True:
    q = input("You: ").lower()

    if "name" in q:
        print("Bot: City Care Hospital")
    elif "doctor" in q:
        print("Bot: Doctors are available in different departments.")
    elif "timing" in q:
        print("Bot: Hospital is open 24 hours.")
    elif "emergency" in q:
        print("Bot: Contact emergency department.")
    elif "exit" in q:
        print("Bot: Thank you!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
