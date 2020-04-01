
while 1 == 1:
    number_emails = {
        'manha@gmail.com': '12345',
        'jack@gmail.com': '124567'
    }
    login_or_sign_in = input('login or sign in: ')
    if login_or_sign_in.upper() == 'LOGIN':
        email = input('what is your email: ')
        if email in number_emails:
            password = input('password: ')
            if password == number_emails.get(email):
                print("welcome")
                break
            else:
                print('wrong password')
        else:
            print('wrong email')
    elif login_or_sign_in.upper() == 'SIGN IN':
        new_account = input('name of account: ')
        if new_account in number_emails:
            print('Sorry this title has already been  taken')
        if len(new_account) <= 9:
            print('Sorry the account name must contain a minimum of 10 characters')
        if new_account.count('@gmail.com') == 0:
            print("The account name must contain '@gmail.com'")
        new_password = input('password: ')
        if len(new_password) <= 5:
            print('Sorry the password must have a minimum of 5 characters')
        confirmation = input('please confirm the password')
        if new_password == confirmation:
            number_emails[new_account] = new_password
            print("you have successfully created a new account")
            break
        else:
            print("you have not confirmed your password please try again later")
    else:
        print('can you please repeat')
