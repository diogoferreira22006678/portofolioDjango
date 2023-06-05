from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

class Universidade (models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.nome

class Curso (models.Model):
    nome = models.CharField(max_length=255)
    ectsTotal = models.IntegerField()
    ProfessorResponsavel = models.ForeignKey('Professor', on_delete=models.CASCADE)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Professor (models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
    
class Cadeira (models.Model):
    nome = models.CharField(max_length=255)
    ects = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    github = models.URLField(max_length=200, null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    linguagem = models.ForeignKey('Linguagem', on_delete=models.CASCADE)
    pessoal = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Linguagem (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome

class Aptidao (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=255)
    ano_criacao = models.IntegerField()
    criador = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='logos/')
    link_oficial = models.URLField()
    descricao = models.TextField()

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
    data_inicio = models.DateField()
    data_fim = models.DateField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

    