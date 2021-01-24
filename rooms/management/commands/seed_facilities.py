from django.core.management.base import BaseCommand
from rooms import models as room_models

class Command(BaseCommand):
    help = "This commands create facilities"


    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} faclities created!"))


        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.WARNING("i luv u"))


"""
    def add_arguments(self,parser):
        
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that i love you"
            )
"""