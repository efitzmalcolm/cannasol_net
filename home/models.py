from django.utils.safestring import mark_safe
from django.db import models


class CarouselImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Carousel Image'
        verbose_name_plural = 'Carousel Images'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class BrandSection(models.Model):
    title = models.CharField(max_length=30)
    intro = models.TextField()

    def __str__(self):
        return self.title


class BrandItem(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField()
    section = models.ForeignKey('BrandSection')

    class Meta:
        verbose_name = 'Brand Item'
        verbose_name_plural = 'Brand Items'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class InfoSection(models.Model):
    image = models.ImageField()

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    email = models.EmailField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class Retailer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)
