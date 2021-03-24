from django.core.management.base import BaseCommand, CommandError
# from api.models import ShoeType, ShoeColor

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


# def new_ticket(request, ticket_id):
#     ticket = TicketItem.objects.filter(id=ticket_id).first()
#     ticket.ticket_status = 'NW'
#     ticket.assigned_to = None
#     ticket.completed_by = None
#     ticket.filed_by = request.user
#     ticket.save()

    # def add_shoe_types(self, ):
    #     ShoeType.objects.create(
    #         style='sneaker'
    #     )


    # def add_shoe_colors(self, ):
    #     ShoeColor.objects.create(

    #     )

    # def handle(self, *args, **kwargs):
    #     self.add_shoe_types()
    #     self.add_shoe_colors()

    def handle(self, *args, **options):
        print('Command: bootstrap_data')