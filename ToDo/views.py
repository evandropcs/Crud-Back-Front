from django.http import JsonResponse
from ToDo.models import FormsTarefa



def home(request):
    tarefas = [t.resposta_json() for t in FormsTarefa.objects.all()]

    return JsonResponse(
        {
            'tarefas': tarefas
        }
    )


# from django.shortcuts import render
#
#
# def teste(request):
#     return render(request, 'teste.html')
