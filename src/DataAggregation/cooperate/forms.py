from models import MessageBoard
from django.forms.models import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = MessageBoard  
        fields = ['name' ,'email' , 'phone' , 'messagecontent']
