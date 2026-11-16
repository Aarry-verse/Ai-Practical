# Practical 1: Simple Reflex Agent – Vacuum Cleaner

def vacuum(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"

print(vacuum("A", "Dirty"))
print(vacuum("B", "Clean"))
