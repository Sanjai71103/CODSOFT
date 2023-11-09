import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_-+=<>?"

    # Combine character sets based on complexity
    if length < 4:
        print("Password length is too short. Please choose a longer length.")
        return

    if length <= 8:
        password_set = lower_letters
    elif length <= 12:
        password_set = lower_letters + digits
    elif length <= 16:
        password_set = lower_letters + digits + upper_letters
    else:
        password_set = lower_letters + digits + upper_letters + special_chars

    # Generate the password
    password = ''.join(random.choice(password_set) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid password length.")

if __name__ == "__main__":
    main()
