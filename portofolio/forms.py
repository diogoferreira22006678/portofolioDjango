from django import forms
from .models import Pessoa
from .models import Professor
from .models import Escola

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
