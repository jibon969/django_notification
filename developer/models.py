from django.db import models
from django.contrib.auth.models import User

FILE_TYPE = [
    ('Csv', 'Csv'),
    ('PDF', 'PDF'),
    ('Image', 'Image'),
    ('Excel', 'Excel'),
    ('Word', 'Word'),
    ('Zip', 'Zip'),
]

APPROVED = [
    ('Yes', 'Yes'),
    ('Rejection', 'Rejection'),
    ('Under_considerations', 'Under_Considerations'),
]


class DeveloperDocument(models.Model):
    title = models.CharField(max_length=120)
    file_type = models.CharField(max_length=20, choices=FILE_TYPE, blank=True, null=True)
    details = models.TextField()
    file = models.FileField(upload_to='developerDocument/')
    date = models.DateField()
    approved = models.CharField(max_length=50, choices=APPROVED, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name="developer_document_user", 
                                   null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']