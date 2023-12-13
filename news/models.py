from django.db import models
from typing import List
from django.contrib.auth.models import AbstractUser

class Taxonomy(models.Model):
    CATEGORY = 'category'
    TAG = 'tag'
    TAXONOMY_CHOICES = [
        (CATEGORY, 'Category'),
        (TAG, 'Tag'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    href = models.URLField()
    count = models.IntegerField(default=0,null=True)
    thumbnail = models.URLField(null=True, blank=True)
    desc = models.CharField(max_length=2000, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    taxonomy = models.CharField(max_length=50, choices=TAXONOMY_CHOICES, default=CATEGORY)
    def __str__(self):
        return self.name    

class PostAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
    avatar = models.URLField()
    bgImage = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    count = models.IntegerField(default=0)
    desc = models.TextField(default="")
    jobName = models.CharField(max_length=255, default="")
    href = models.URLField(default="")
    def __str__(self):
        return self.displayName    

# class Like(models.Model):
#     count = models.IntegerField()
#     isLiked = models.BooleanField()

# class Bookmark(models.Model):
#     count = models.IntegerField()
#     isBookmarked = models.BooleanField()    

class Bookmark(models.Model):
        count = models.IntegerField()
        isBookmarked = models.BooleanField()
class Like(models.Model):
        count = models.IntegerField()
        isLiked = models.BooleanField()    
class PostData(models.Model):
    STANDARD = 'standard'
    VIDEO = 'video'
    GALLERY = 'gallery'
    AUDIO = 'audio'

    POST_TYPE_CHOICES = [
        (STANDARD, 'Standard'),
        (VIDEO, 'Video'),
        (GALLERY, 'Gallery'),
        (AUDIO, 'Audio'),
    ]    
    index = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255)
    authorId = models.ForeignKey(PostAuthor, on_delete=models.CASCADE)
    date = models.DateField()
    href = models.URLField()
    categoriesId = models.ManyToManyField(Taxonomy)
    title = models.CharField(max_length=255)
    featuredImage = models.URLField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    like = models.OneToOneField(Like, on_delete=models.CASCADE) 
    bookmark = models.OneToOneField(Bookmark, on_delete=models.CASCADE)
    commentCount = models.IntegerField()
    viewdCount = models.IntegerField()
    readingTime = models.IntegerField()
    postType = models.CharField(max_length=50, choices=POST_TYPE_CHOICES)
    videoUrl = models.URLField(null=True, blank=True)
    audioUrl = models.URLField(null=True, blank=True)
    galleryImgs = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title
    
    
    
    




# user authentication custom model 



class CustomUser(AbstractUser):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username