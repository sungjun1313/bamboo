from django import forms
from package.models import Custom, Pack1, Pack2

class CustomForm(forms.ModelForm):
    name = forms.CharField(required=True,max_length=100,widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
        }
    ))

    phone = forms.CharField(required=False,max_length=100,widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
        }
    ))

    address = forms.CharField(required=False,max_length=100,widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Custom
        fields = ("name", "phone", "address",)
        labels = {
            "name" : "이름*",
            "phone" : "전화번호",
            "address" : "주소",
        }


class Pack1Form(forms.ModelForm):
    title = forms.CharField(required=True,max_length=100, widget= forms.TextInput(attrs={'type':'hidden', 'value': 'package1'}))
    p1 = forms.CharField(required=False,max_length=100, widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    p2 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p3 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p4 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p5 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p6 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p7 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p8 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p9 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p10 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p11 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p12 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p13 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p14 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p15 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p16 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p17 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p18 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p19 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p20 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p21 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p22 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Pack1
        fields = {"custom", "title" ,"p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16", "p17", "p18", "p19", "p20", "p21", "p22",}

class Pack2Form(forms.ModelForm):
    title = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'type': 'hidden', 'value': 'package2'}))
    p23 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r23 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p24 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r24 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p25 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r25 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p26 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r26 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p27 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r27 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p28 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r28 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p29 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r29 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p30 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r30 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p31 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r31 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p32 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r32 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p33 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r33 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p34 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r34 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p35 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r35 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    p36 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    r36 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Pack2
        fields = {"custom", "title", "p23", "r23", "p24", "r24", "p25", "r25", "p26", "r26", "p27", "r27", "p28", "r28", "p29", "r29", "p30", "r30", "p31", "r31", "p32", "r32", "p33", "r33", "p34", "r34", "p35", "r35", "p36", "r36",}