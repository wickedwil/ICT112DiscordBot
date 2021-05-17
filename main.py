import random

class DiscordUser:
    """A class for each individual discord user."""


    def __init__(self, str_user_name, int_user_id):
        self.str_user_name = str_user_name
        self.int_user_id = int_user_id


    def get_user_name(self):
        return self.str_user_name


    def get_user_id(self):
        return self.int_user_id


list_server_members = []
int_server_members = 10
for member in range(int_server_members):
    list_server_members.append(member)
    list_server_members[member] = DiscordUser("Bob", random.randint(1000, 10000))
    print(list_server_members[member].get_user_name(), list_server_members[member].get_user_id())

print("LUCY FRICKIN SMELLS ALL THE DOO DA DAY")