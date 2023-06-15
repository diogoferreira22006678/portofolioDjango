from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    resumo_sobre = models.TextField()
    resumo_estudos = models.TextField()
    resumo_competencias = models.TextField()

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

class Universidade (models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/universidade/', null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateField(default='2020-01-01')
    fim = models.DateField(default='2020-01-01')

    def __str__(self):
        return self.nome
    
class Escola (models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()
    logo = models.ImageField(upload_to='logos/escola/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Curso (models.Model):
    nome = models.CharField(max_length=255)
    ectsTotal = models.IntegerField()
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return self.nome

class Professor (models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    link_lusofona = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
    
class Interesse (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='interesses/', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Cadeira (models.Model):
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    ects = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professores = models.ManyToManyField('Professor')
    semestre = models.IntegerField()
    anoEscolar = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    
class TipoProjeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    github = models.URLField(max_length=200, null=True, blank=True)
    pessoas = models.ManyToManyField(Pessoa)
    orientadores = models.ManyToManyField('Professor', null=True, blank=True)
    tipo = models.ForeignKey('TipoProjeto', on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField('Tecnologia')
    cadeira = models.ForeignKey('Cadeira', on_delete=models.CASCADE, null=True, blank=True)
    pokemon = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    ano = models.IntegerField()
    link_relatorio = models.URLField(max_length=200, null=True, blank=True)
    link_video = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length=255)
    acronimo = models.CharField(max_length=255)
    ano_criacao = models.IntegerField()
    criador = models.CharField(max_length=255, null=True, blank=True)
    logotipo = models.ImageField(upload_to='logos/linguagens/', null=True, blank=True)
    imagem_exemplo = models.ImageField(upload_to='snippets/', null=True, blank=True)
    link_oficial = models.URLField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class TipoAptidao (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Aptidao (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    cadeiras = models.ManyToManyField('Cadeira', null=True, blank=True)
    projetos = models.ManyToManyField('Projeto', null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tipo = models.ForeignKey('TipoAptidao', on_delete=models.CASCADE)


    def __str__(self):
        return self.nome



class TipoTecnologia(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=255)
    acronimo = models.CharField(max_length=255, null=True, blank=True)
    ano_criacao = models.IntegerField()
    criador = models.CharField(max_length=255, null=True, blank=True)
    resumo = models.TextField()
    link_oficial = models.URLField()
    descricao = models.TextField()
    tipo = models.ForeignKey('TipoTecnologia', on_delete=models.CASCADE)
    linguagens = models.ManyToManyField('Linguagem', null=True, blank=True)
    logotipo = models.ImageField(upload_to='logos/tecnologias/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
class ExperienciaProfissional (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    inicio = models.DateField()
    fim = models.DateField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class FormResponses (models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome + ' ' + self.email


class DadoColetado(models.Model):
    valor = models.FloatField()
    data_coleta = models.DateTimeField(auto_now_add=True)

    
