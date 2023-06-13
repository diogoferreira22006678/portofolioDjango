from django.contrib import admin

# Register your models here.
from .models import Pessoa, Universidade, Curso, Professor, Cadeira, Projeto, Linguagem, Tecnologia, Aptidao, ExperienciaProfissional, TipoProjeto, TipoAptidao, TipoTecnologia, Escola

admin.site.register(Pessoa)
admin.site.register(Universidade)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(Linguagem)
admin.site.register(Tecnologia)
admin.site.register(Aptidao)
admin.site.register(ExperienciaProfissional)
admin.site.register(TipoProjeto)
admin.site.register(TipoAptidao)
admin.site.register(TipoTecnologia)
admin.site.register(Escola)