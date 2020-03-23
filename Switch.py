def Switch(low, high, choice):
    if (choice >= low) & (choice <= high):
        return False
    else:
        low = str(low)
        high = str(high)
        print("Please enter a value between " + low + " and " + high)
        return True