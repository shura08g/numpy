request = {'form': {'username': 'Alex', 'password': 'qwerty'}}
request2 = {'form': {'username': 'Tom', 'password': 'qwerty2'}}
request3 = {'form': {'username': 'Sam', 'password': 'qwer'}}
request4 = {'form': {'username': 'Tom', 'password': 'qwerty'}}
db = {}


def process_form(request):
    password = request.get('form').get('password')
    username = request['form'].get('username')

    if len(password) > 5:
        if username not in db:
            db[username] = password
            return 'Added user!'
        else:
            return f'User with name {username} already exist!'
    else:
        return 'Password is too short!'

print(process_form(request))
print(process_form(request2))
print(process_form(request3))
print(process_form(request4))
print(db)
