from django import forms
from .models import Pessoa
from .models import Professor
from .models import Escola
from .models import Universidade
from .models import Curso
from .models import Cadeira
from .models import Projeto
from .models import Linguagem
from .models import ExperienciaProfissional
from .models import Aptidao
from .models import Tecnologia
from .models import TipoTecnologia
from .models import TipoAptidao
from .models import TipoProjeto

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields ='__all__'
    

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields ='__all__'

    # Select field tem de ser Escolhe a Universidade
    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)
        self.fields['universidade'].empty_label = "Escolhe a Universidade"

class EscolaForm(forms.ModelForm):

    class Meta:
        model = Escola
        fields ='__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(EscolaForm, self).__init__(*args, **kwargs)
        self.fields['pessoa'].empty_label = "Escolhe a Pessoa"

class UniversidadeForm(forms.ModelForm):
    
    class Meta:
        model = Universidade
        fields ='__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(UniversidadeForm, self).__init__(*args, **kwargs)
        self.fields['pessoa'].empty_label = "Escolhe a Pessoa"

class CursoForm(forms.ModelForm):
        
    class Meta:
        model = Curso
        fields ='__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['professor'].empty_label = "Escolhe o Professor"
        self.fields['universidade'].empty_label = "Escolhe a Universidade"

class CadeiraForm(forms.ModelForm):
            
    class Meta:
        model = Cadeira
        fields ='__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(CadeiraForm, self).__init__(*args, **kwargs)
        self.fields['curso'].empty_label = "Escolhe o Curso"
        self.fields['professor'].empty_label = "Escolhe o Professor"

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields ='__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(ProjetoForm, self).__init__(*args, **kwargs)
        self.fields['pessoa'].empty_label = "Escolhe a Pessoa"
        self.fields['tipo_projeto'].empty_label = "Escolhe o Tipo de Projeto"

class LinguagemForm(forms.ModelForm):
                    
    class Meta:
        model = Linguagem
        fields ='__all__'

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(LinguagemForm, self).__init__(*args, **kwargs)
        self.fields['projeto'].empty_label = "Escolhe o Projeto"
        
class ExperienciaProfissionalForm(forms.ModelForm):

    class Meta:
        model = ExperienciaProfissional
        fields ='__all__'
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(ExperienciaProfissionalForm, self).__init__(*args, **kwargs)
        self.fields['pessoa'].empty_label = "Escolhe a Pessoa"
        self.fields['tipo_projeto'].empty_label = "Escolhe o Tipo de Projeto"   
                            
class AptidaoForm(forms.ModelForm):
                            
    class Meta:
        model = Aptidao
        fields ='__all__'

    # Select field tem de ser Escolhe a Pessoa
    def __init__(self, *args, **kwargs):
        super(AptidaoForm, self).__init__(*args, **kwargs)
        self.fields['pessoa'].empty_label = "Escolhe a Pessoa"
        self.fields['tipo_aptidao'].empty_label = "Escolhe o Tipo de Aptidão"

class TecnologiaForm(forms.ModelForm):
        
        class Meta:
            model = Tecnologia
            fields ='__all__'
    
        # Select field tem de ser Escolhe a Pessoa
        def __init__(self, *args, **kwargs):
            super(TecnologiaForm, self).__init__(*args, **kwargs)
            self.fields['pessoa'].empty_label = "Escolhe a Pessoa"
            self.fields['tipo_tecnologia'].empty_label = "Escolhe o Tipo de Tecnologia"

class TipoTecnologiaForm(forms.ModelForm):
        
        class Meta:
            model = TipoTecnologia
            fields ='__all__'

class TipoAptidaoForm(forms.ModelForm):
            
            class Meta:
                model = TipoAptidao
                fields ='__all__'

class TipoProjetoForm(forms.ModelForm):
                
                class Meta:
                    model = TipoProjeto
                    fields ='__all__'