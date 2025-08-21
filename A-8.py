users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

for user in users_info:
    profile = "Name: {}, Age: {}".format(*user)
    print(profile)
