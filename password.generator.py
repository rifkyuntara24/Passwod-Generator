import random
import string

def buat_password(min_length, has_number, has_special):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characther = letters

    if has_number:
        characther += digits
    if has_special:
        characther += special
    if (min_length < 8):
        return "Password minimal harus 8 karakter."
    
    if (has_number != "y"):
        return "setidaknya password harus memiliki number"
    
    password = ''.join(random.sample(characther, min_length))


    return password

min_length = int(input("Masukkan panjang minimal karater yang anda inginkan ? "))
has_number = input(f"Apakah anda mau menambahkan angka y/n ? ").lower() == "y"
has_special = input(f"Apakah anda mau menambahkan karakter special y/n ? ").lower() == "y"

password = buat_password(min_length, has_number, has_special)

print(f"Your password is : {password}")
