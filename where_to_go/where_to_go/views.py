from django.http import HttpResponse

def render_main_page(request):
    return HttpResponse('Здесь будет карта!')