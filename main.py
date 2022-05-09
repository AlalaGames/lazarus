import requests, ctypes
from bs4 import BeautifulSoup

ctypes.windll.kernel32.SetConsoleTitleW("Lazerus by Boolty")
#################################################
# Change name_set and country for any country   #
# us | ar | au | br | ch | gr | dk | it         #
#################################################

name_set = 'gr'
country = 'gr'
url = f'https://www.fakenamegenerator.com/gen-random-{name_set}-{country}.php'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.find(class_='address')
table = soup.find(class_='content')
f_name = name.find_all('h3')
rows = table.find_all('dl')


def main():
    global url, headers, rows, f_name
    print('Lazerus By Boolty...')
    print('Select language...')
    print('Generate personal information...')

    print(name.text)
    with open(f_name[0].text + '.txt', 'a') as file:
        file.write(name.text)
        file.close()

    i = 0
    for row in range(26):
        user_date = rows[i].text
        print(user_date)
        i += 1
        with open(f_name[0].text + '.txt', 'a') as file:
            file.write(user_date)
            file.close()
    email()
    print('File', f_name[0].text, 'has saved as .txt...')
    print('#############')
    print('# By Boolty #')
    print('#############')
    print('Press Enter to close...')
    input()


def email():
    global f_name
    rs = f_name[0].text
    en = rs.replace(' ','')
    mail = f'http://www.fakemailgenerator.com/#/rhyta.com/{en}/'
    print('Email= ' + mail)
    with open(f_name[0].text + '.txt', 'a') as file:
        file.write(mail)
        file.close()


if __name__ == '__main__':
    main()