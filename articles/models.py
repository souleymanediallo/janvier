from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings

import uuid


# https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield
# Create your models here.
class Condition(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Condition, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MainCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MainCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.main_category.name} -> {self.name}"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.main_category.name} -> {self.category.name} -> {self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ImageArticle(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.id


class Article(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name="articles",
                                    on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.PositiveIntegerField()
    condition = models.ForeignKey(Condition, on_delete=models.DO_NOTHING, related_name="article_condition")
    tag = models.ManyToManyField(Tag, related_name="articles", blank=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, related_name="article_color", blank=True)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, related_name="article_size", blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/')
    image_article = models.ManyToManyField(ImageArticle, related_name="article_image", blank=True)
    change = models.BooleanField(default=False)
    give = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.author}"