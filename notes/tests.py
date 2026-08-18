"""Tests covering the sticky notes application model and views."""

from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    """Test cases for the Note model behaviour."""

    def setUp(self):
        """Create a sample note for the model tests."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
        )

    def test_note_has_title(self):
        """Check that the note title is stored correctly."""
        self.assertEqual(self.note.title, "Test Note")

    def test_note_has_content(self):
        """Check that the note content is stored correctly."""
        self.assertEqual(self.note.content, "This is a test note.")


class NoteViewTest(TestCase):
    """Test the note list and detail views in the app."""

    def setUp(self):
        """Create a note for testing page responses."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
        )

    def test_note_list_view(self):
        """The list page should load and show the note title."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """The detail page should load and show the stored note content."""
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")
