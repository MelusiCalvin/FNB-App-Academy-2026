while True:
    input = input("Please enter a game score (Next to the flashing cursor): ")
    if input.lower().strip() == "stop":
        break
    elif int(input) > 100:
        print("Good try! Keep playing!")