from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.name

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    description =models.TextField(max_length=500)
    image = models.ImageField(upload_to='image')

    top1_text = models.CharField(max_length=150)
    top1_image = models.ImageField(upload_to='image')
    top1_description = models.TextField(max_length=500)

    top2_text = models.CharField(max_length=150)
    top2_image = models.ImageField(upload_to='image')
    top2_description = models.TextField(max_length=500)

    category = models.ForeignKey(category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class PostFilter(models.TextChoices):
        FEATURE = 'F', 'Feature'
        TRENDING = 'T', 'Trending'
        PROMOTION = 'PR', 'Promotion'
    post_filter = models.CharField(
        choices=PostFilter.choices,
        max_length=20,
        default=PostFilter.FEATURE,  # You can set a default value if needed
    )

