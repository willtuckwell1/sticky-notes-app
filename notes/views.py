"""Views for handling note listing, detail, creation, update, and deletion."""

from django.shortcuts import get_object_or_404, redirect, render
from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display all notes ordered by newest first."""
    notes = Note.objects.all().order_by(
        "-created_at"
    )
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """Display the details for a single note."""
    note = get_object_or_404(Note, pk=pk)  # Get the note or return 404
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Create a new note from a submitted form."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new note to the database
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """Update an existing note using the form data submitted by the user."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()  # Save the updated note
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """Delete a note after confirmation from the user."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()  # Remove the note from the database
        return redirect("note_list")

    return render(request, "notes/note_delete.html", {"note": note})
