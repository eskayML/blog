from django.db import models

class Blog(models.Model):
    
    blog_content = models.TextField()
    authors_name = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.blog_content[:15]