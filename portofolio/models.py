from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

class Universidade (models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Escola (models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()

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
    email = models.EmailField(max_length=255)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
    
class Cadeira (models.Model):
    nome = models.CharField(max_length=255)
    ects = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    semestre = models.IntegerField()
    anoEscolar = models.IntegerField()

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
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    linguagens = models.ManyToManyField('Linguagem')
    tipo = models.ForeignKey('TipoProjeto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length=255)
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
    ano_criacao = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    link_oficial = models.URLField()
    descricao = models.TextField()
    tipo = models.ForeignKey('TipoTecnologia', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Interesses (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

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
    

    
