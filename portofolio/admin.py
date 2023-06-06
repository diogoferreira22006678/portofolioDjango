from django.contrib import admin

# Register your models here.
from .models import Pessoa, Universidade, Curso, Professor, Cadeira, Projeto, Linguagem, Tecnologia, Aptidao, Interesses, ExperienciaProfissional

admin.site.register(Pessoa)
admin.site.register(Universidade)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(Linguagem)
admin.site.register(Tecnologia)
admin.site.register(Aptidao)
admin.site.register(Interesses)
admin.site.register(ExperienciaProfissional)

