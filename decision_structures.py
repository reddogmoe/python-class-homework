correct_password = "password"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_password = input("Enter password: ")

    if entered_password == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")

if attempts == max_attempts:
    print("Account locked.")
