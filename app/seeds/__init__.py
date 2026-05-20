from flask.cli import AppGroup
from .users import seed_users, undo_users
from .services import seed_services, undo_services
from .bookings import seed_bookings, undo_bookings
from .pets import seed_pets, undo_pets
from .reviews import seed_reviews, undo_reviews
from .pet_images import seed_pet_images, undo_pet_images

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    seed_users()
    seed_services()
    seed_reviews()
    seed_pets()
    seed_pet_images()
    seed_bookings()

@seed_commands.command('undo')
def undo():
    undo_bookings()
    undo_pet_images()
    undo_pets()
    undo_reviews()
    undo_services()
    undo_users()
