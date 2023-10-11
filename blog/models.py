from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True, max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at', )