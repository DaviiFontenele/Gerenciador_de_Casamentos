from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from noivos.models import Convidados, Presentes, Acompanhante

# Create your views here.

def convidados (request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    if resposta not in ["C", "R"]:
        return redirect(f'/convidados/?token={token}')
    

    convidado.status = resposta
    convidado.save()

    return redirect(f'/convidados/?token={token}')

def reservar_presente(request, id):
    token = request.GET.get('token')

    convidado = Convidados.objects.get(token=token)
    presente = Presentes.objects.get(id=id)

    presente.reservado=True
    presente.reservado_por = convidado
    presente.save()
    return redirect(f'/convidados/?token={token}')

#acompanhantes


def adicionar_acompanhante(request):
    token = request.GET.get("token")
    convidado = get_object_or_404(Convidados, token=token)
    


    if request.method == "POST":
        nome_acompanhante = request.POST.get("nome")

        # Verificar se o limite de acompanhantes foi atingido
        if convidado.acompanhantes.count() < convidado.maximo_acompanhantes:
            Acompanhante.objects.create(convidado=convidado, nome=nome_acompanhante)
        else:
            # Exibir uma mensagem de erro caso o limite tenha sido atingido
            return render(request, "convidado.html", {"convidado": convidado, "error": "Limite de acompanhantes atingido."})

        return redirect(f"/convidados/?token={token}")

    return render(request, "convidado.html", {"convidado": convidado})



    

    

