from django import forms
from .models import Pessoa
from .models import Professor
from .models import Escola
from .models import Universidade
from .models import Curso
from .models import Cadeira

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
