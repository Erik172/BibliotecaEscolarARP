from django.shortcuts import render
from books import services

# Create your views here.
def viewBooks(request):
    context = {
        'mostViews': services.getMostViewBooks(num_items=6, lang='spanish'),
        'allCategoriesBooks': services.getCategoriesBook(),
    }
    return render(request, 'books/index.html', context)

def viewBooksCategory(request, category: str):
    context = {
        'books': services.searchBookCategory(category, lang='spanish')
    }

    return render(request, 'books/search.html', context)

def searchBook(request):
    try:
        typeSearch = request.POST['type']
        lang = request.POST['lang']
    except:
        typeSearch = 'keyword'
        lang = 'all'

    search = request.POST['search']

    if typeSearch == 'title':
        books = services.searchBookTitle(search, lang=lang)
        return render(request, 'books/search.html', {'books': books})
    
    elif typeSearch == 'author':
        books = services.searchBookAuthor(search, lang=lang)
        return render(request, 'books/search.html', {'books': books})

    elif typeSearch == 'keyword':
        books = services.searchBookKeyword(search, lang=lang)
        return render(request, 'books/search.html', {'books': books})

    elif typeSearch == 'category':
        books = services.searchBookCategory(search, lang=lang)
        return render(request, 'books/search.html', {'books': books})