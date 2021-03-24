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
        new_style = ShoeType.objects.create(
            style='sneaker'
        )
        new_style.save()

        new_style = ShoeType.objects.create(
            style='boot'
        )
        new_style.save()

        new_style = ShoeType.objects.create(
            style='sandal'
        )
        new_style.save()

        new_style = ShoeType.objects.create(
            style='dress'
        )
        new_style.save()

        new_style = ShoeType.objects.create(
            style='other'
        )
        new_style.save()

    def add_shoe_colors(self):
        add_color = ShoeColor.objects.create(
            color_name='RE'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='OR'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='YE'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='OR'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='GR'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='BE'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='IN'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='VI'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='WH'
        )
        add_color.save()

        add_color = ShoeColor.objects.create(
            color_name='BL'
        )
        add_color.save()

    def handle(self, *args, **options):
        self.add_shoe_types()
        self.add_shoe_colors()


