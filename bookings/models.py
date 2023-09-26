from django.db import models
from django.contrib.auth.models import User

TIME_CHOICES = (
    ("4:00 pm - 6:00 pm", "4:00 pm - 6:00 pm"),
    ("4:15 pm - 6:15 pm", "4:15 pm - 6:15 pm"),
    ("4:30 pm - 6:30 pm", "4:30 pm - 6:30 pm"),
    ("4:45 pm - 6:45 pm", "4:45 pm - 6:45 pm"),
    ("5:00 pm - 7:00 pm", "5:00 pm - 7:00 pm"),
    ("5:15 pm - 7:15 pm", "5:15 pm - 7:15 pm"),
    ("5:30 pm - 7:30 pm", "5:30 pm - 7:30 pm"),
    ("5:45 pm - 7:45 pm", "5:45 pm - 7:45 pm"),
    ("6:00 pm - 8:00 pm", "6:00 pm - 8:00 pm"),
    ("6:15 pm - 8:15 pm", "6:15 pm - 8:15 pm"),
    ("6:30 pm - 8:30 pm", "6:30 pm - 8:30 pm"),
    ("6:45 pm - 8:45 pm", "6:45 pm - 8:45 pm"),
    ("7:00 pm - 9:00 pm", "7:00 pm - 9:00 pm"),
    ("7:15 pm - 9:15 pm", "7:15 pm - 9:15 pm"),
    ("7:30 pm - 9:30 pm", "7:30 pm - 9:30 pm"),
    ("7:45 pm - 9:45 pm", "7:45 pm - 9:45 pm"),
    ("8:00 pm - 10:00 pm", "8:00 pm - 10:00 pm"),
)


class Booking(models.Model):
    """create booking model"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservation")
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(
        max_length=20, choices=TIME_CHOICES, default="4:00 pm - 6:00 pm")
    number_of_guests = models.PositiveIntegerField(default=2)
    message = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"Name: {self.name} Date: {self.date} Time: {self.time}"
