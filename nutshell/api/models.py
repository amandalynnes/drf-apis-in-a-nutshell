from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=20)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=20)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'RE'
    ORANGE = 'OR'
    YELLOW = 'YE'
    GREEN = 'GR'
    BLUE = 'BE'
    INDIGO = 'IN'
    VIOLET = 'VI'
    WHITE = 'WH'
    BLACK = 'BL'
    SHOE_COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]
    color_name = models.CharField(
        max_length=2,
        choices=SHOE_COLOR_CHOICES,
        default=WHITE
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, null=True, blank=True)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, null=True, blank=True)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return self.size
