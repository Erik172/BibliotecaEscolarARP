import requests
import json

URL = 'https://www.etnassoft.com/api/v1/get/?'


def searchBookTitle(title: str, num_items=10000, lang='all', verify=False):
    response = requests.get(f'{URL}book_title="{title}"&decode=true&num_items={num_items}&lang={lang}')
    if response.status_code == 200:
        responseJson = response.json()
        books = []
        for bookJson in responseJson:
            books.append(bookJson)

        return books

    elif response.status_code == 500:
        return '500'

def searchBookId(id: int):
    response = requests.get(f'{URL}id={id}&decode=true')
    if response.status_code == 200:
        return response.json()[0]

    elif response.status_code == 500:
        return  '500'

def searchBookAuthor(autor: str, num_items=10000, lang='all'):
    response = requests.get(f'{URL}book_author="{autor}"&decode=true&num_items={num_items}&lang={lang}')
    if response.status_code == 200:
        responseJson = response.json()
        books = []
        for bookJson in responseJson:
            books.append(bookJson)

        return books

    elif response.status_code == 500:
        return '500'

def searchBookKeyword(keyword: str, num_items=10000, lang='all'):
    response = requests.get(f'{URL}keyword={keyword}&decode=true&num_items={num_items}&lang={lang}')
    if response.status_code == 200:
        responseJson = response.json()
        books = []
        for bookJson in responseJson:
            books.append(bookJson)

        return books

    elif response.status_code == 500:
        return '500'

def searchBookCategory(category: str, num_items=10000, lang='all'):
    response = requests.get(f'{URL}category={category}&decode=true&num_items={num_items}&lang={lang}')
    if response.status_code == 200:
        responseJson = response.json()
        books = []
        for bookJson in responseJson:
            books.append(bookJson)

        return books

    elif response.status_code == 500:
        return '500'

def getCategoriesBook():
    response = requests.get(f'{URL}get_categories=all&decode=true')
    if response.status_code == 200:
        responseJson = response.json()
        books = []
        for bookJson in responseJson:
            books.append(bookJson)

        return books

    elif response.status_code == 500:
        return '500'

def getMostViewBooks(num_items=100000, lang='all'):
    response = requests.get(f'{URL}most_viewed&lang={lang}&decode=true&num_items={num_items}')
    if response.status_code == 200:
        responseJson = response.json()
        books = []
        for bookJson in responseJson:
            books.append(bookJson)

        return books
    
    elif response.status_code == 500:
        return '500'
