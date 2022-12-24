from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", max_length=100, help_text="100 caracteres maximo")
    url = forms.URLField(label="Tu sitio web", required=False,initial="http://")
    comment = forms.CharField(label="Escribe tu comentario")
    
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=50,widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.EmailField(label="Email", max_length=50,widget=forms.EmailInput(attrs={'class':'email'}))
    message = forms.CharField(label="message", widget=forms.TextInput(attrs={'class':'message'}))
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != "open":
            raise forms.ValidationError("SOLO OPEN VALIDO")
        else:
            return name