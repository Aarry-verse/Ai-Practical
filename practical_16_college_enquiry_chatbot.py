# Practical 16: College Enquiry Chatbot

print("College Enquiry Chatbot")
print("Ask about college")

while True:
    q = input("You: ").lower()

    if "name" in q:
        print("Bot: PDEA College of Engineering, Manjari")
    elif "courses" in q:
        print("Bot: Computer, Mechanical, Civil and other courses")
    elif "fees" in q:
        print("Bot: Contact college office for fee details")
    elif "admission" in q:
        print("Bot: Admission is through CAP process")
    elif "exit" in q:
        print("Bot: Thank you!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
