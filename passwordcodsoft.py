#python program to generate random password based on length entered by user
import random
import string
def gen_password(length):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_"
    password = ''.join(random.choice(letters) for i in range(length))
    return password
n=int(input("Enter the length of the password: ")) #to input the length of the password
password = gen_password(n)  
print(password)
