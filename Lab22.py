def accepts(string):
    state = "q0"

    for symbol in string:

        if state == "q0" and symbol == "a":
            state = "q1"

        elif state == "q1" and symbol == "b":
            state = "q2"

        elif state == "q2" and symbol == "b":
            state = "q3"

        else:
            return False

    return state in ["q2", "q3"]


string = input("Enter a string: ")

if accepts(string):
    print("String Accepted")
else:
    print("String Rejected")