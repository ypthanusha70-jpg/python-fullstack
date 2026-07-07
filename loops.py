for i in range(5):
    print("siri")

###################################

users=["siri","thanu","sak","hima"]
for users in users:
    print("message sent to",users)


###############################################

for i in range(2,6):
    print(i)



#########################################


count = 1
while count <=5:
    print(count)
    count +=1

##############################3

for i in range(10):
    if i == 5:
        break
    print(i)

#######################################

for i in range(10):
    if i == 5:
        continue
    print(i)

###################################

# password = ""
# while password != "1234":
    passowrd = input("enter password")
#     print("login success")



#########################################

student = [
    "ram",
    "sam",
    "rana"
]
student.remove("sam")
student.append("Thanu")
print(student)