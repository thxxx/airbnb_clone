from django_seed import Seed
from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from reservations import models as reservation_models
from django.contrib.admin.utils import flatten
import random
from datetime import datetime, timedelta

NAME = "reservations"


class Command(BaseCommand):

    help = f"This commands create {NAME}"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number", default=2, type=int, help=f"How many {NAME} do you create",
        )

    def handle(self, *args, **options):
        number = options.get("number")  # 입력안하면 1
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        # [4:10] 이런식으로 하면 array를 제한한다. 모든 방을 주되 4에서 10사이의 방만.
        rooms = room_models.Room.objects.all()

        seeder.add_entity(reservation_models.Reservation, number, {
            "status": lambda x: random.choice(["pending", "confirmed", "canceled", ]),
            "guest": lambda x: random.choice(users),
            "check_in": lambda x: datetime.now(),
            "check_out": lambda x: datetime.now() + timedelta(days=random.randint(2, 5)),
            "room": lambda x: random.choice(rooms),
        },)  # 필드를 만든다. # Host가 존재하야한다. 포린키를 돕는데 시더를 사용해야한다.
        seeder.execute()
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))

        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.WARNING("i luv u"))
