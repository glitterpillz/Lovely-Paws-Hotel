from app.models import db, Service, environment, SCHEMA
from sqlalchemy import text
from .users import User

def seed_services():
    staff_9 = User.query.get(9)
    staff_10 = User.query.get(10)
    staff_11 = User.query.get(11)
    staff_12 = User.query.get(12)
    staff_13 = User.query.get(13)
    staff_14 = User.query.get(14)
    staff_15 = User.query.get(15)
    staff_16 = User.query.get(16)
    staff_17 = User.query.get(17)
    staff_18 = User.query.get(18)

    hair_cut = Service(
        service="Hair Cut", price=57.99, staff=[staff_18, staff_17, staff_16]
    )
    nail_trim = Service(
        service="Nail Trim", price=24.99, staff=[staff_15, staff_9, staff_10]
    )
    simple_bath = Service(
        service="Simple Bath", price=39.99, staff=[staff_15, staff_14, staff_10]
    )
    luxury_bath = Service(
        service="Luxury Bath", price=59.99, staff=[staff_11, staff_12, staff_13]
    )
    all_inclusive = Service(
        service="All Inclusive", price=109.99, staff=[staff_9, staff_11, staff_12, staff_15, staff_18]
    )

    db.session.add(hair_cut)
    db.session.add(nail_trim)
    db.session.add(simple_bath)
    db.session.add(luxury_bath)
    db.session.add(all_inclusive)
    db.session.commit()

def undo_services():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.services RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM services"))
        
    db.session.commit()