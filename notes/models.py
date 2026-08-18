"""Models for the sticky notes application."""

from django.db import models


class Note(models.Model):
    """Represents a single sticky note stored in the database."""

    # Basic note information
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """Return the note title for display in the admin and templates."""
        return self.title
