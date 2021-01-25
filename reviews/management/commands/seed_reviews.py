from django_seed import Seed
from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from reviews import models as review_models
import random


class Command(BaseCommand):

    help = "This commands create reviews"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews do you create",
        )

    def handle(self, *args, **options):
        number = options.get("number")  # 입력안하면 1
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(review_models.Review, number, {
            "accuracy" : lambda x: random.randint(1, 5),
            "communication" : lambda x: random.randint(1, 5),
            "cleanliness" : lambda x: random.randint(1, 5),
            "location" : lambda x: random.randint(1, 5),
            "check_in" : lambda x: random.randint(1, 5),
            "value" : lambda x: random.randint(1, 5),
            "room": lambda x: random.choice(rooms),
            "user": lambda x: random.choice(users),
        },)  # 필드를 만든다. # Host가 존재하야한다. 포린키를 돕는데 시더를 사용해야한다.
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))

        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.WARNING("i luv u"))


"""

"""
