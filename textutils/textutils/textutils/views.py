# I Have Created this file.
from django.http import HttpResponse
from django.shortcuts import render


# code to Display Text and Links and files to Website.

# def index(request):
#     return HttpResponse('''<h1>Hello my Name is Amit Kumar<h1/> <a
#     href="https://www.codewithharry.com/blogpost/java-cheatsheet"> Link <a/>''')
#
#
# def about(request):
#     return HttpResponse("Hello my Name is Amit Kumar, I am form Delhi")

# Passing params in function
# def index(request):
#     params = {'Name': 'Amit Kumar', 'City': 'New Delhi'}
#     return render(request, 'index.html', params)
#     # return HttpResponse("Home")


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the Text
    djtext = (request.GET.get('text', 'default'))
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("Capitalize_first")
#
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
#
# def spaceremove(request):
#     return HttpResponse("spaceremove")
#
#
# def charcount(request):
#     return HttpResponse("Charcount")
