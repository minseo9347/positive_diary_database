# diary/forms.py

from django import forms
from .models import Affirmation

class AffirmationForm(forms.ModelForm):
    class Meta:
        model = Affirmation
        fields = ['nickname', 'date', 'emotion', 'content']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'emotion': forms.Select(choices=[
                ('❤️', '❤️'), ('🔥', '🔥'), ('🌈', '🌈'), ('😊', '😊')
            ]),
            'content': forms.Textarea(attrs={'placeholder': '오늘의 긍정확언을 입력해주세요.'}),
        }
