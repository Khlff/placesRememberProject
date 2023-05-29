from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Класс формы фидбэка.
    """
    class Meta:
        model = Feedback
        fields = ['title', 'comment', 'latitude', 'longitude']
