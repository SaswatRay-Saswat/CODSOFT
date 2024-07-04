import random
import string
def main():
    print("\nWelcome to Password Generator")
    length = int(input("Enter the length of required password: "))
    digit = string.digits
    symbols = string.punctuation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    combine = lower + upper + digit + symbols
    x = random.sample(combine,length)
    password="".join(x)
    print(f"Password is {password}")
    main()
    
main()
