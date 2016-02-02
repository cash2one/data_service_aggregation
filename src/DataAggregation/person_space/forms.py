from django.forms.models import ModelForm
from django import forms
from models import User_Info, User_Personal_Certi, User_Org_Certi


class UserInfoForm(ModelForm):
    class Meta:
        model = User_Info  
        fields = ['mobile_no', 'nickname', 'user_type',]


class EditPasswordForm(forms.Form):
    username = forms.CharField(max_length=100)
    oldPassword = forms.CharField(max_length=100)
    newPassword = forms.CharField(max_length=100)
    newPassword2 = forms.CharField(max_length=100)


class PersonalCertiFrom(ModelForm):
    class Meta:
        model = User_Personal_Certi 
        fields = ['realname', 'id_card_no', 'forward_side_photo', 'back_side_photo',]


class OrgCertiFrom(ModelForm):
    class Meta:
        model = User_Org_Certi  
        fields = ['company_name', 'province', 'city', 'district', 'address',
                  'busi_lisence_no', 'busi_lisence_photo', 'tax_reg_no', 'tax_reg_photo', 'org_no', 'org_photo',
                  'contact_name', 'contact_phone', ]
        

