contacts = {
    "Melusi": "0821112222",
    "Njabulo": "0821113333",
    "Sihle": "0821114444",
}
input = input("Please enter a name to search for (Next to the flashing cursor): ").capitalize()
if input in contacts.keys():
    print(f"{input}'s phone number is {contacts[input]}")
else:
    print("Contact not found")