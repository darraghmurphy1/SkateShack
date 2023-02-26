from django import forms
from .models import Review

RATINGS = [(1, 'Unsatisfactory'),
           (2, 'Poor'),
           (3, 'Ok'),
           (4, 'Good'),
           (5, 'Top Class')]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(label='How will you rate this product?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)