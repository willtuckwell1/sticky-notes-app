"""Forms used for creating and updating notes."""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and editing a sticky note."""

    class Meta:
        model = Note
        fields = ["title", "content"]  # Only the fields users need to enter
