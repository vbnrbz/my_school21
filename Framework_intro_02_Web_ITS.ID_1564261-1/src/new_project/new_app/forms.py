from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ваше имя',
        }),
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ваше email',
        }),
    )

    message = forms.CharField(
        label='Сообщение',
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Ваше сообщение',
            'rows': 3,
        }),
    )
    # name = forms.CharField(label='Имя', max_length=100, required=True)
    # email = forms.EmailField(label='Email', required=True)
    # message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)