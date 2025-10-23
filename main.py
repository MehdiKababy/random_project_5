# Run = True


# def check_Len_Character(password):
#     if len(password) > 8 and len(password) < 64:
#         check_Use_Number(password)
#     else:
#         print("Your password must be between 8 and 64 characters")


# def check_Use_Number(password):
#     check_All_Character = []
#     for i in password:
#         if i.isnumeric():
#             check_All_Character.append(True)
#         else:
#             check_All_Character.append(False)
#     if False not in check_All_Character:
#         print("The password must contain letters")
#     elif True in check_All_Character:
#         check_Use_Upper_Lower_Character(password)
#     else:
#         print("The password must also contain numbers")


# def check_Use_Upper_Lower_Character(password):
#     global Run  # بره function گلوبال میشه تا با تغییرات اعمال شده به خارج Run اینجا
#     check_Use_Upper_Lower = []
#     for i in password:
#         if i.isupper():
#             check_Use_Upper_Lower.append(True)
#         elif i.isnumeric():
#             continue
#         else:
#             check_Use_Upper_Lower.append(False)
#     if False not in check_Use_Upper_Lower:
#         print("The password must contain lowercase letters")
#     elif True in check_Use_Upper_Lower:
#         print("Password confirmed")
#         Run = False
#     else:
#         print("Password must contain uppercase letters")


# print("Welcome to password checker")
# while Run:
#     check_Len_Character(input("Enter password : "))


# Run = True
def password_Checker(password):
    all_Characters = []
    for i in password:
        if i.isnumeric():
            all_Characters.append("int")
        elif i.isalpha():
            if i.isupper():
                all_Characters.append("Ustr")
            elif i.islower():
                all_Characters.append("Lstr")
        else:
            all_Characters.append("else")
    if len(password) > 8 and len(password) < 64:
        if "Ustr" not in all_Characters:
            print("You should also use capital letters")
        elif "Lstr" not in all_Characters:
            print("You should also use lowercase letters")
        elif "int" not in all_Characters:
            print("You should also use numbers")
        elif (
            "Ustr" in all_Characters
            and "Lstr" in all_Characters
            and "int" in all_Characters
        ):
            print("Your password confirmed")
            Upper_Lower_Case(String=password)
            # return False
            # global Run
            # Run = False
    else:
        print("The password must be between 8 and 64 characters")


def Upper_Lower_Case(String):
    upper_Case = lower_Casre = spaces = numbers = other = 0
    for i in String:
        if i.isupper():
            upper_Case += 1
        elif i.islower():
            lower_Casre += 1
        elif i == " ":
            spaces += 1
        elif i.isnumeric():
            numbers += 1
        else:
            other += 1
    return print(
        f"upper case : {upper_Case}\nlower case : {lower_Casre}\nspaces : {spaces}\nnumbers : {numbers}\nother : {other}"
    )


print("Welcome to password checker")
exit = ["exit", "Exit", "exit()", "Exit()", "leave", "Leave"]
while True:
    input_Password = input("Enter password (Type (exit, leave, exit) for log out) : ")
    if input_Password in exit:
        break
    password_Checker(password=input_Password)
