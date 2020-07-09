from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-Vindo! Você está na página de votações.")

