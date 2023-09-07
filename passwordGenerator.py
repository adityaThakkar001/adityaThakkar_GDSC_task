import random

def passwordGenerator(length):
    passchar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    passuchar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    passn = ['0','1','2','3','4','5','6','7','8','9']
    passpchar = ['!','@','#','$','%','&','*','<','>','.',',','?','/',':',';','|','+','-']
    print("Choose Password complexity:")
    choice = int(input("1. No Complexity\n2. For password with lowercase and uppercase characters\n3. For password with lowercase, uppercase, and numerical characters\n4. For characters with lowercase, uppercase, numerical, and special characters\n"))
    match choice:
        case 1:
            passchar
        case 2:
            passchar.extend(passuchar)
        case 3:
            passchar.extend(passuchar + passn)
        case 4:
            passchar.extend(passuchar + passn + passpchar)
    password = ''.join(random.choice(passchar) for _ in range(length))
    print("Generated Password:", password)

length = int(input("Enter the length of the password: "))
passwordGenerator(length)

