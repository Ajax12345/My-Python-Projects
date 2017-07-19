import requests
import sys

EMAIL = 'jpetullo14@gmail.com'
PASSWORD = 'secretpassword'

URL = 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f'

def main():
    # Start a session so we can have persistant cookies
    session = requests.session() #config={'verbose': sys.stderr}

    # This is the form data that the page sends when logging in
    login_data = {
        'loginemail': EMAIL,
        'loginpswd': PASSWORD,
        'submit': 'login',
    }

    # Authenticate
    r = session.post(URL, data=login_data)

    # Try accessing a page that requires you to be logged in
    r = session.get('https://stackoverflow.com/users/7326738/ajax1234')
    print re.findall("<p>(.*?)</p>", r.text)
    if str(r) == "<Response [200]>":
        print "Yes"


if __name__ == '__main__':
    main()
