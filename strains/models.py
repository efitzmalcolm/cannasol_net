from django.utils.safestring import mark_safe
from django.db import models


class Strain(models.Model):

    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    brand = models.ForeignKey('Brand')
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Strain"
        verbose_name_plural = "Strains"

    def __str__(self):
        return self.name

    def preview_image(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img height="263px" width="263px" src="%s" />' % self.image.url)
        else:
            return mark_safe('<img height="263px" width="263px" src= "/static/strains/img/placeholder.png" />')


class Brand(models.Model):

    name = models.CharField(max_length=30)
    desc = models.TextField(blank=True, unique=True)
    logo = models.ImageField()

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name

    def preview_image(self):
        return mark_safe('<img src="%s" />' % self.logo.url)


class qaSample(models.Model):

    lab_name = models.CharField(max_length=50)

    date_received = models.DateField()
    date_reported = models.DateField()

    sample_type = models.CharField(max_length=25)
    strain = models.ForeignKey('Strain')

    lab_id = models.CharField(max_length=16)
    sample_id = models.CharField(max_length=16, unique=True)
    lot_id = models.CharField(max_length=16)

    class Meta:
        verbose_name = "QA Sample"
        verbose_name_plural = "QA Samples"

    def __str__(self):
        return self.sample_id + " - " + self.strain.name


class PotencyResult(models.Model):

    qa_sample = models.ForeignKey('qaSample', unique=True)

    delta9_thc = models.DecimalField(max_digits=4, decimal_places=2)
    cbd = models.DecimalField(max_digits=4, decimal_places=2)
    cbn = models.DecimalField(max_digits=4, decimal_places=2)
    cbg = models.DecimalField(max_digits=4, decimal_places=2)
    cbc = models.DecimalField(max_digits=4, decimal_places=2)
    delta8_thc = models.DecimalField(max_digits=4, decimal_places=2)
    total_cannabinoids = models.DecimalField(max_digits=4, decimal_places=2)
    total_thc = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "Potency Result"
        verbose_name_plural = "Potency Results"

    def __str__(self):
        return self.name + ": " + self.result


class TerpeneResult(models.Model):

    terpene = models.ForeignKey('Terpene')
    result = models.DecimalField(max_digits=4, decimal_places=2)
    qa_sample = models.ForeignKey('qaSample')

    class Meta:
        verbose_name = "Terpene Result"
        verbose_name_plural = "Terpene Results"
        unique_together = ('qa_sample', 'terpene')

    def __str__(self):
        return self.terpene.name + ": " + str(self.result) + '%'


class Terpene(models.Model):

    name = models.CharField(max_length=50, unique=True)
    short_desc = models.CharField(max_length=250, blank=True, null=True)
    long_desc = models.TextField(blank=True, null=True)
    aroma = models.CharField(max_length=250, blank=True, null=True)
    flavor = models.CharField(max_length=250, blank=True, null=True)
    effects = models.CharField(max_length=250, blank=True, null=True)

    row_map = {
        'α-Pinene': 7,
        'β-Pinene': 8,
        'Terpinolene': 9,
        'Geraniol': 10,
        'α-Terpinene': 11,
        'γ-Terpinene': 12,
        'Camphene': 13,
        'Linalool': 14,
        'd-Limonene': 15,
        'Citral': 16,
        'Myrcene': 17,
        'α-Terpineol': 18,
        'Citronellol': 19,
        'dl-Menthol': 20,
        '1-Borneol': 21,
        '2-Piperidone': 22,
        'β-Caryophyllene': 23,
        'α-Humulene': 24,
        'Caryophyllene Oxide': 25,
    }

    class Meta:
        verbose_name = "Terpene"
        verbose_name_plural = "Terpenes"

    def __str__(self):
        return self.name
