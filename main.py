import requests


def task1():
    with open("task1/url.txt") as file:
        array = [row.strip() for row in file]
    print(len(array))
    index = open('task1/index.txt', 'w')
    for idx, el in enumerate(array):
        print(el)
        url = 'https://' + el
        send = requests.post(url)
        filename = 'task1/urls/' + str(idx) + '.txt'
        file = open(filename, 'w')
        file.write(send.text.encode('utf-8'))
        index.write(str(idx) + ' ' + el + '\n')
        file.close()

    index.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   task1()

