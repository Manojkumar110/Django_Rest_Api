from django .http import HttpResponse

def home_page(request):
    print('home page')
    return HttpResponse('Home Page')
