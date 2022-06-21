'''Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы
он сохранял базу ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться
с модулем shelve (https://docs.python.org/3/library/shelve.html), который в данном случае будет весьма
удобен и упростит выполнение задания.'''
import shelve


def add_url(**kwargs):
    for k, v in kwargs.items():
        with shelve.open('LinksDb') as db:
            if not k in db:
                db[k] = v
                print(f'{db[k]} successfully added')
            else:
                print('Url already exists')


def get_urls():
    with shelve.open('LinksDb') as file:
        for k, v in file.items():
            print(f'{k} is the Full name for {v} url')


def app_run():
    while True:
        try:
            choice = int(input('''
Press <1> to add a link
Press <2> to view all links
Press <0> to exit
'''))
        except ValueError:
            print("Wrong number")
        else:
            if choice == 1:
                url_full = input('Enter URL: ')
                url_short = input('Enter short name: ')
                mydict = {url_full: url_short}
                add_url(**mydict)
            elif choice == 2:
                get_urls()
            elif choice == 0:
                exit()
            else:
                continue



def array_diff(a, b):
    newlist = []
    if len(b) == 0:
        return a
    for elem in a:
        if not elem in b:
            newlist.append(elem)
    return newlist
if __name__ == '__main__':
    print(array_diff([1, 2, 3], [1, 2]))
