
from django.db import models
from accounts.models import User

class Assessment(models.Model):

    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('javascript', 'JavaScript'),
    ]

    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    batch = models.CharField(max_length=100)

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES
    )

    exam_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assessments"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )

    def __str__(self):
        return self.title