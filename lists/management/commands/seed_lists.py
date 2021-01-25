from django_seed import Seed
from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from lists import models as list_models
from django.contrib.admin.utils import flatten
import random

NAME = "lists"

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
        rooms = room_models.Room.objects.all() # [4:10] 이런식으로 하면 array를 제한한다. 모든 방을 주되 4에서 10사이의 방만.

        seeder.add_entity(list_models.List, number, {
            "user": lambda x: random.choice(users),
        },)  # 필드를 만든다. # Host가 존재하야한다. 포린키를 돕는데 시더를 사용해야한다.
        seeder.execute()
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0,5): random.randint(6, 30)]
            list_model.rooms.add(*to_add) # *을 붙이는 이유는 to_add는 query set. array가 될건데 나는 array안의 요소를 원해
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))

        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.WARNING("i luv u"))


