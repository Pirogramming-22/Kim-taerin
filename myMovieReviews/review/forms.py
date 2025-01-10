from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'director', 'genre', 'release_year', 'rating', 'runtime', 'content','cast']