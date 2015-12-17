from django.shortcuts import render

def index(request):
    """
    Returns the main page.

    Note as of now, all other "pages" are partially loaded. That is, this
    is the only full HTML file (including DOCTYPE, head, body, etc.). Through
    AngularJS, all other content is pulled in later.
    """
    return render(request, 'home/index.html')
