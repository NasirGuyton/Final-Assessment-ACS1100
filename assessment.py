
def load_data(txt):
    users = []
    with open(txt) as file:
        for line in file:
             
            user_data = line.strip().split(',')
            user = {
                'name': user_data[0],
                'password': user_data[1],
                'full_name': user_data[2],
                'Current Balance': float(user_data[3])
            }
            users.append(user)
    return users

def user_information(user):
    return f"Name: {user['full_name']} Balance: {user['balance']}"

def login(users, username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

def Run():
    users = load_data('data.txt')
    username = input("Name: ")
    password = input("password: ")
    
    user = login(users, username, password)
    
    if user:
        print(user_information(user))
    else:
        print("Username and password are incorrect")

Run()

