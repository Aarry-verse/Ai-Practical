# Practical 19: Online Shopping Assistant Chatbot

print("Shopping Assistant Chatbot")

while True:
    q = input("You: ").lower()

    if "product" in q:
        print("Bot: We have mobiles, laptops and clothes.")
    elif "price" in q:
        print("Bot: Check product price on our website.")
    elif "delivery" in q:
        print("Bot: Delivery takes 3-5 days.")
    elif "payment" in q:
        print("Bot: We accept online payments.")
    elif "exit" in q:
        print("Bot: Thank you for shopping!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
