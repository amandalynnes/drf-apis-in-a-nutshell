from django.core.management.base import BaseCommand
from nutshell.api.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = '''Populates the ShoeType table with the following entries:
            sneaker
            boot
            sandal
            dress
            other

            Populates the ShoeColor table with the following entries:
            Red
            Orange
            Yellow
            Green
            Blue
            Indigo
            Violet
            White
            Black'''

    def add_shoe_types(self):
        ShoeType.objects.bulk_create([
            ShoeType(style='sneaker'),
            ShoeType(style='boot'),
            ShoeType(style='sandal'),
            ShoeType(style='dress'),
            ShoeType(style='other'),
        ])

    def add_shoe_colors(self):
        ShoeColor.objects.bulk_create([
            ShoeColor(color_name='RE'),
            ShoeColor(color_name='OR'),
            ShoeColor(color_name='YE'),
            ShoeColor(color_name='OR'),
            ShoeColor(color_name='GR'),
            ShoeColor(color_name='BE'),
            ShoeColor(color_name='IN'),
            ShoeColor(color_name='VI'),
            ShoeColor(color_name='WH'),
            ShoeColor(color_name='BL'),
        ])

    def handle(self, *args, **options):
        self.add_shoe_types()
        self.add_shoe_colors()


