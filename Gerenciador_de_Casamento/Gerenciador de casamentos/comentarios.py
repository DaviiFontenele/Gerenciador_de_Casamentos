#django-admin startproject core .

#django-admin -> criar um arquivo
#startproject -> inicia os arquivos do projeto
#"core" -> nome que foi dado
# . -> espaço + ponto -> deixo o arquivo na pasta que ja estou

# ------------------------------------------------------------

#o arquivo "manage.py" e aonde iremos configurar todos os nossos app

#criar um app
# selecionar a pasta, digitar o codigo "startapp" e depois o nome da pasta
#python manage.py startapp noivos   

#criar o servidor para evitar erros -> python manage.py runserver

#----------------------------------------------------------

#devo adicionar meu novo app, na pagina settings.py da pasta "mae" para ativar meu app
#na seção "installe_apps"

#2) criar uma url - na pasta "mae" deve-se criar a url

# para acesar o painel do adm
# no terminal: python manage.py createsuperuser
# no servidor /admin

# organizar o front o notion

#iniciar o servidor: python manage.py runserver

'''
{% extends "base.html" %}

{% block 'body' %}
    <div class="max-w-7xl mx-auto mt-12">
        <div class="mx-auto max-w-2xl text-center">
            <h2 class="text-balance text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">Olá, {{convidado.nome_convidado}}</h2>

            {% if error %}
                <p class="text-red-500">{{ error }}</p>
            {% endif %}

            <div class="bg-slate-200/20 p-6 rounded-md mt-4 drop-shadow-lg ring-1 ring-gray-600/20">
                <h2 class="text-balance text-xl font-semibold tracking-tight text-gray-900 text-center">Adicione seus acompanhantes</h2>
                {% if convidado.acompanhantes.count < convidado.maximo_acompanhantes %}
                    <form action="{% url 'adicionar_acompanhante' %}?token={{ convidado.token }}" method="POST">
                        {% csrf_token %}
                        <label class="mt-4 block text-sm leading-6 text-gray-900">Nome</label>
                        <input type="text" name="nome" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300">
                        <input type="submit" class="rounded-md mt-4 bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 cursor-pointer" value="Adicionar">
                    </form>
                {% else %}
                    <p class="text-sm text-gray-600">Você já atingiu o limite de acompanhantes.</p>
                {% endif %}

                <br><hr><br>

                <ul>
                    {% for acompanhante in convidado.acompanhantes.all %}
                        <li class="bg-slate-100 p-4">{{ acompanhante.nome }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
{% endblock %}


'''