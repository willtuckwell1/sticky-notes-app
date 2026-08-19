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
    """Test the note list, detail, create, update, and delete views."""

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

    def test_note_create_view(self):
        """A user can create a new note from the form."""
        response = self.client.post(
            reverse("note_create"),
            {"title": "New Note", "content": "Fresh content"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Note")
        self.assertTrue(Note.objects.filter(title="New Note", content="Fresh content").exists())

    def test_note_update_view(self):
        """A user can edit an existing note."""
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            {"title": "Updated Note", "content": "Updated content"},
            follow=True,
        )
        self.note.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.note.title, "Updated Note")
        self.assertEqual(self.note.content, "Updated content")

    def test_note_delete_view(self):
        """A user can delete a note and be redirected back to the list."""
        response = self.client.post(
            reverse("note_delete", args=[self.note.pk]),
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
        self.assertContains(response, "All Notes")

    def test_note_create_use_case(self):
        """Creating a note covers the create use case."""
        self.client.post(
            reverse("note_create"),
            {"title": "Create Use Case", "content": "Created via test"},
            follow=True,
        )
        self.assertTrue(
            Note.objects.filter(title="Create Use Case", content="Created via test").exists()
        )

    def test_note_update_use_case(self):
        """Updating a note covers the update use case."""
        self.client.post(
            reverse("note_update", args=[self.note.pk]),
            {"title": "Updated Use Case", "content": "Updated via test"},
            follow=True,
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Use Case")
        self.assertEqual(self.note.content, "Updated via test")

    def test_note_delete_use_case(self):
        """Deleting a note covers the delete use case."""
        self.client.post(reverse("note_delete", args=[self.note.pk]), follow=True)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
