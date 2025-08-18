users_info = [["Bob", 79],
              ["Tom", 59],
              ["Ken", 61]]

for i in range(len(users_info)):
    user = users_info[i]
    profile = "Name: {}, Age: {}".format(*user)
    print(profile)
