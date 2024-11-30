from django.contrib import admin
from .models import Presentes, Convidados, Acompanhante

# Register your models here.

#chatgpt
# Inline para exibir acompanhantes dentro do Convidado
class AcompanhanteInline(admin.TabularInline):
    model = Acompanhante
    extra = 0  # Evita exibir linhas extras para adicionar acompanhantes

# Configuração do modelo Convidados no admin
class ConvidadosAdmin(admin.ModelAdmin):
    list_display = ('nome_convidado', 'status', 'maximo_acompanhantes', 'mostrar_acompanhantes')
    inlines = [AcompanhanteInline]  # Adiciona o inline para mostrar acompanhantes na página de detalhes

    # Função para exibir acompanhantes na lista de convidados
    def mostrar_acompanhantes(self, obj):
        return ", ".join([acompanhante.nome for acompanhante in obj.acompanhantes.all()])
    mostrar_acompanhantes.short_description = 'Acompanhantes'


admin.site.register(Presentes)
admin.site.register(Convidados)
admin.site.register(Acompanhante) #chat