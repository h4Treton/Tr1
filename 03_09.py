users = {1: {'name': 'name1', 'surname': 'surname1', 'phone': 375291111111, 'email': ''},
         2: {'name': 'name2', 'surname': 'surname2', 'phone': 375292222222, 'email': 'mail2@mail.by'},
         3: {'name': 'name3', 'surname': 'surname3', 'phone': 375293333333},
         4: {'name': 'name4', 'surname': 'surname4', 'phone': 375294444444, 'email': 'mail4@mail.by'}}


def filter_users():
    users_keys = list(users.keys())
    for i in range(len(users_keys)):
        if ((users.get(users_keys[i])).get('email') is None) or ((users.get(users_keys[i])).get('email') == ''):
            print(users.get(users_keys[i]).get('name'))
    return None


filter_users()
