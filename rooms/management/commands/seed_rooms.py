from django_seed import Seed
from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from django.contrib.admin.utils import flatten
import random


class Command(BaseCommand):

    help = "This commands create rooms"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms do you create",
        )

    def handle(self, *args, **options):
        number = options.get("number")  # 입력안하면 1
        seeder = Seed.seeder()

        # objects.all은 데이터가 클때는 절대로 하면 안되다!!!
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        facilities = room_models.Facility.objects.all()
        amenities = room_models.Amenity.objects.all()
        rules = room_models.HouseRule.objects.all()

        seeder.add_entity(room_models.Room, number, {
            'name': lambda x: seeder.faker.address(),  # faker라는 라이브러리를 사용.
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_types),
            'price': lambda x: random.randint(1, 300),  # 숫자의 범위를 지정한다.
            'beds': lambda x: random.randint(1, 5),
            'baths': lambda x: random.randint(1, 5),
            'bedrooms': lambda x: random.randint(1, 5),
            'guests': lambda x: random.randint(1, 5),
        },)  # 필드를 만든다. # Host가 존재하야한다. 포린키를 돕는데 시더를 사용해야한다.
        created_photos = seeder.execute()  # 장고시드는 원래 primary key를 리턴한다
        # 장고에서 제공하는 flatten이라는 걸로도 2차원 리스트 값 뽑아내기 가능.
        created_clean = flatten(list(created_photos.values()))

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room, # 포린키랑 포린키 인스턴스
                    ifile=f"room_photos/{random.randint(1, 6)}.jpg",
                )
            
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a), # 매니 투 매니 field에서 무언가를 추가하는 방법
                else :
                    pass

            for f in facilities:
                magic_number = random.randint(0, 7)
                if magic_number % 2 == 0:
                    room.facilities.add(f), # 매니 투 매니 field에서 무언가를 추가하는 방법
                else :
                    pass

            for r in rules:
                magic_number = random.randint(0, 4)
                if magic_number % 2 == 0:
                    room.house_rules.add(r), # 매니 투 매니 field에서 무언가를 추가하는 방법
                else :
                    pass


        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))

        # times = options.get("times")
        # for t in range(0, int(times)):
        #     self.stdout.write(self.style.WARNING("i luv u"))


"""

"""
