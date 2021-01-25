from django_seed import Seed
from django.core.management.base import BaseCommand
from users import models as user_models

class Command(BaseCommand):
    help = "This commands create users"

    def add_arguments(self,parser):
        
        parser.add_argument(
            "--number", default=2, type=int, help="How many users do you create",
            )

    def handle(self, *args, **options):
        number = options.get("number") # 입력안하면 1
        seeder = Seed.seeder()
        seeder.add_entity(user_models.User, number, {
            'is_staff':False,
            'is_superuser':False  #어드민이 아닌 유저 생성
        }) # 필드를 만든다.
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))


        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.WARNING("i luv u"))


"""

"""