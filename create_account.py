import json
import time
import requests
import random
import names
import os
import secrets
import string


script_version = "1.0"
script_title = "Spotify Account Creator and Streamer By Frogleim"
script_info = f'''
	 ..: {script_title} :..

 [!] ABOUT SCRIPT:
 [-] With this script, you can register on Spotify.com
 [-] Version: {script_version}
 --------
 [!] ABOUT CODER:
 [-] ALIILAPRO, Programmer and developer from Armenia.
 [-] Github   : https://github.com/Frogleim
 --------
'''


class Main:

    def clear(self, text):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text)

    def settitle(self, title_name: str):
        os.system("title {0}".format(title_name))

    def __init__(self):

        self.alphabet = string.ascii_letters + string.digits
        self.settitle(script_title)
        self.clear(script_info)
        self.password = '077108803GBH'
        self.birth_year = random.randint(1990, 2002)
        self.birth_month = random.randint(1, 12)
        self.birth_day = random.randint(1, 28)
        self.gender = random.choice(['male', 'female'])

    def gen_credentails_method(self):

        self.credentails_data = []
        credentails = {}
        credentails['gender'] = self.gender
        credentails['birth_year'] = self.birth_year
        credentails['birth_month'] = self.birth_month
        credentails['birth_day'] = self.birth_day
        credentails['password'] = self.password
        username = string.ascii_letters + string.digits
        username = ''.join(random.choice(username) for i in range(random.randint(7, 11)))
        credentails['username'] = username
        credentails['email'] = names.get_full_name().replace(' ', '').lower() + f'{random.randint(100, 200)}@gmail.com'
        print(f'Email: {credentails["email"]}')
        print(f'Password: {credentails["password"]}')

        return credentails

    def creator(self):

        try:
            session = requests.Session()
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/86.0.4280.141 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": "https://www.spotify.com/",
                "Accept-Encoding": "gzip, deflate, br",
                "accept-language": "en",
                "Host": "spclient.wg.spotify.com"
            }
            credentails = self.gen_credentails_method()
            data = 'birth_day={0}&birth_month={1}&birth_year={2}&collect_personal_info' \
                   '=undefined&creation_flow=&creation_point=https:' \
                   '//www.spotify.com/uk/&displayname={3}&email={4}&gender={5}&iagree=1' \
                   '&key=a1e486e2729f46d6bb368d6b2bcda326&password={6}&password_repeat={7}&' \
                   'platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0'.format(
                credentails['birth_day'], credentails['birth_month'], credentails['birth_year'],
                credentails['username'], credentails['email'], credentails['gender'], credentails['password'],
                credentails['password'])
            proxies = {
                'http://':
                    'uncutgems : dasherZ1',
                'https://':
                    'uncutgems: dasherZ1'
            }
            req = session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers=headers, data=data,
                               proxies=proxies)
            print(req.status_code)
            print(
                '[>] ACCOUNT CREATED SUCCESSFULLY\n[-] Email:{0}\n[-] Password:{1}\n[-] Username:{2}\n[-] '
                'Gender:{3}\n[-] Birth year:{4}\n[-] Birth month:{5}\n[-] Birth day:{6}\n'.format(
                    credentails['email'], credentails['password'], credentails['username'], credentails['gender'],
                    credentails['birth_year'], credentails['birth_month'], credentails['birth_day']))
            return credentails
        except Exception as e:
            print(e)

    def run(self):

        while True:
            count = 0
            for i in range(50):
                credentails = self.creator()
                time.sleep(2)
                count += 1
                with open(f'users/data_1.json', 'r+') as savefile:
                    file_data = json.load(savefile)
                    file_data['users'].append(credentails)
                    savefile.seek(0)
                    json.dump(file_data, savefile, indent=7)
                print(f'{count} account')
            print(f'___Accounts created successfully___')
            time.sleep(3600)


if __name__ == "__main__":
    main = Main()
    main.run()