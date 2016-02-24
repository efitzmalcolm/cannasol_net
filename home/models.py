from django.utils.safestring import mark_safe
from django.db import models
from django.core.validators import RegexValidator


class CarouselImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    header = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Carousel Image'
        verbose_name_plural = 'Carousel Images'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" src="%s" />' % self.image.url)


class BrandSection(models.Model):
    title = models.CharField(max_length=30)
    intro = models.TextField()

    class Meta:
        verbose_name = 'Brand Section'
        verbose_name_plural = 'Brand Section'

    def __str__(self):
        return self.title


class BrandItem(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField()
    section = models.ForeignKey('BrandSection')
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Brand Item'
        verbose_name_plural = 'Brand Items'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" src="%s" />' % self.image.url)


class InfoSection(models.Model):
    image = models.ImageField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Info Section'
        verbose_name_plural = 'Info Section'

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    email = models.EmailField()
    image = models.ImageField()
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class AboutUsPage(models.Model):
    header_image = models.ImageField()
    title = 'About Us Section'

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title

    def preview_image(self):
        if self.header_image and hasattr(self.header_image, 'url'):
            return mark_safe('<img height="263px" src="%s" />' % self.header_image.url)


class AboutUsSection(models.Model):
    header = models.CharField(max_length=35)
    text = models.TextField()
    order = models.PositiveSmallIntegerField()
    page = models.ForeignKey('AboutUsPage')

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Sections'

    def __str__(self):
        return self.header


class Retailer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    homepage = models.URLField()

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'

    def __str__(self):
        return self.name

    # Generates HTML Image preview for use at thumbnail on admin, etc...
    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)


class NewsletterContact(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Newsletter Contact'
        verbose_name_plural = 'Newsletter Contacts'

    def __str__(self):
        return self.email


class RetailerContact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    title = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )
    phone = models.CharField(validators=[phone_regex], max_length=16)
    storename = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    license = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Retailer Contact'
        verbose_name_plural = 'Retailer Contacts'

    def __str__(self):
        return "%s: %s %s" % (self.storename, self.firstname, self.lastname)
