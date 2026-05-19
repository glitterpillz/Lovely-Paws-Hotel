from datetime import datetime, timedelta
from app.models import Booking, db, environment, SCHEMA
from sqlalchemy import text
from .services import Service

def seed_bookings():
    hair_cut = Service.query.get(1)
    nail_trim = Service.query.get(2)
    simple_bath = Service.query.get(3)
    luxury_bath = Service.query.get(4)

    bookings = [
        Booking(
            client_id=5,
            pet_id=1,
            booking_type='day_care',
            drop_off_date=datetime.now() - timedelta(days=5),
            pick_up_date=datetime.now() - timedelta(days=5),
            services=[hair_cut, luxury_bath]
        ),
        Booking(
            client_id=6,
            pet_id=2,
            booking_type='boarding_care',
            drop_off_date=datetime.now() - timedelta(days=10),
            pick_up_date=datetime.now() + timedelta(days=2),
            services=[hair_cut, nail_trim, simple_bath]
        ),
        Booking(
            client_id=7,
            pet_id=3,
            booking_type='day_care',
            drop_off_date=datetime.now() - timedelta(days=8),
            pick_up_date=datetime.now() - timedelta(days=8),
            services=[hair_cut, nail_trim, luxury_bath]
        ),
        Booking(
            client_id=8,
            pet_id=4,
            booking_type='boarding_care',
            drop_off_date=datetime.now() - timedelta(days=3),
            pick_up_date=datetime.now() + timedelta(days=4),
            services=[hair_cut, nail_trim, luxury_bath]
        ),
        Booking(
            client_id=5,
            pet_id=5,
            booking_type='boarding_care',
            drop_off_date=datetime.now() + timedelta(days=10),
            pick_up_date=datetime.now() + timedelta(days=15),
            services=[hair_cut, nail_trim, simple_bath]
        ),
    ]

    db.session.add_all(bookings)
    db.session.commit()

def undo_bookings():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM bookings"))

    db.session.commit()
