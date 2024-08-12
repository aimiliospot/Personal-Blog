from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from unidecode import unidecode


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    subtitle = models.CharField(max_length=200, null=False, default='')
    image = models.ImageField(upload_to='uploads/', null=False)
    date = models.DateTimeField()
    slug = models.SlugField(unique=True, editable=False)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='author')
    caption = models.ManyToManyField(Tag, null=False, related_name='tag')

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)


class Comment(models.Model):
    username = models.CharField(max_length=100, null=False)
    comment = models.TextField(null=False, max_length=500)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name='comments')

    def __str__(self):
        return f'{self.username} on {self.date}'
