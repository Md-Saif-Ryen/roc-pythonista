#-------------CHapter1---WARM Up----------
#Q-NO.3----------------------------------------------
# Online Registration Form_________
# print("Welcome to ABC Uni!")
# print("Please enter the required information to begin.")
# s_f_n = input("Enter your name: ")
# phone = int(input("Enter your phone number: "))
# em = input("Enter Email address: ")
# crs = input("Choose your coarse: ")

#Q-NO.4----------------------------------------------
# Library Login page_________
# username = input("Username: ")
# password = input("Password: ")
# print(f"Your Username is {username}.")
# print(f"Your password is {password}")
#
# while True:
#     user_id = input("Please enter your username: ")
#     passw = input("Please enter your password: ")
#     if user_id==username and passw==password:
#         print("You have successfully logged in.!")
#         break
#     elif user_id==username and passw!=password:
#         print("Invalid Password.!\nPlease try again.")
#         continue
#     elif user_id!=username and passw==password:
#         print("invalid Username.!\nPlease try again.")
#         continue
#     else:
#         print("Invalid Username/Password.!\nPlease try again.")
#         continue


#Q-5----------------------

# grades = ["A", "A", "B","U", "F", "E", "D"]
# for grade in grades:
#     if grade == "A" or grade == "B":
#         print("True")
#
#     else:
#         print("False")
#



#--------------------------------Ch-2 Recording Information------------------

#task 1:::::::::::::::

# print("Please complete this survey for our next video.!!")
# print("What shall I stream next?")
# print("a) Days Gone\nb) Resident Evil 2\nc) Fortnite\nd) Apex Legends\ne) Death Stranding\nf) Surprise Us!")
# print("Please enter 'a', 'b', 'c', 'd', 'e', 'f' for the corresponding.")
# a = "Days Gone"
# b = "Resident Evil 2"
# c = "Fortnite"
# d = "Apex Legends"
# e = "Death Stranding"
# f = "Surprise Us!"
# grtd = "I really appreciate your time and hope to see you in the next one!"
# while True:
#     wish = input("Enter here :")
#     if wish == "a":
#         print(f"You have chosen {a}.{grtd}")
#         break
#     elif wish == "b":
#         print(f"You have chosen {b}.{grtd}")
#         break
#     elif wish == "c":
#         print(f"You have chosen {c}.{grtd}")
#         break
#     elif wish == "d":
#         print(f"You have chosen {d}.{grtd}")
#         break
#     elif wish == "e":
#         print(f"You have chosen {e}.{grtd}")
#         break
#     elif wish == "f":
#         print(f"You have chosen {f}.{grtd}")
#         break
#     else:
#         print("Please choose among the given options.")
#         continue

#Task 2:::::::::::::::::::::::::::::::
# print("Welcome to our services.!\nThe same are as follows :")
# print("a) Root Canal Therapy - $250\nb) Oral Hygiene Check - $50\nc) Emergency Injury Treatment - $100\n"
#       "d) post-Procedure-Check-up - $150\ne) Routine Check-ups and Consultation - $75")
# print("Please choose the name of the service(s) by entering 'a', 'b', 'c', 'd', 'e' for the corresponding option.")
# print("NOTE ::: Make Sure to put spaces between service options")
# service = input()
# print("We are giving a discount of 50% for every advance payment.\nEnter 'a' to pay in Advance or 'b' to pay after the service.")
# met_svc = input()
# a = 250
# b = 50
# c = 100
# d = 150
# e = 75
# total = 0
# lst_svc = service.split()
# for i in lst_svc:
#     if i == "a":
#         total += a
#     elif i == "b":
#         total += b
#     elif i == "c":
#         total += c
#     elif i == "d":
#         total += d
#     elif i == "e":
#         total += e
# if met_svc == "a":
#     total -= 0.5*total
# elif met_svc == "b":
#     total = total
# print(f"Your total amount payable is {total}\nThank You for choosing our services.! Hope to see you next time.")



#Is it correct part 2-----------

#Q-2---

# print("Your door-way to autoload eligibility checker.\nPlease provide full information for the best result.")
# name = input("Enter your full name :")
# age = int(input("Enter your age :"))
# income = int(input("Enter your income per month :"))
# nature_of_job = input("Do you work Part-time/Full-time/Freelancing? : ")
# criminal_rec = input("Any criminal record in the last 5 years[y/n] :")
# has_licence = input("Do you have a licence[y/n] :")
# if age < 45 and income > 8000 and nature_of_job == "Full-time" and criminal_rec.lower() == "n" and has_licence.lower() == "y":
#     print("Congrats, You are eligible for the auto-loan.!")
# elif age < 45 and income >= 5000 and nature_of_job == "Part-time" and criminal_rec.lower() == "n" and has_licence.lower() == "y":
#     print("You are eligible to apply for a loan.")
# elif criminal_rec.lower() == "y":
#     print("You are not eligible for a loan.")
# elif has_licence.lower() == "n":
#     print("You are not eligible for a loan at the moment.")
# else:
#     print("Please have patience,We will contact you soon.")


#--------------------------RUNNING INTO CIRCLES
#--Task 1

# dict_num = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}
# while True:
#     try:
#         inp_num = int(input("Enter your number :"))
#         break
#     except Exception as e:
#         print("Please enter a number")
#         continue

# str_inp = str(inp_num)
# num_list = []
# for num in str_inp:
#     num_list.append(dict_num[int(num)])
# ur_num = " ".join(num_list)
# print(ur_num)



