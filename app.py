import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    while True:
        length = input("Enter password length: ")
        if length.isdigit():
            length = int(length)
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
            cont = input("Generate another password? (yes/no): ")
            if cont.lower() != "yes":
                break
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()