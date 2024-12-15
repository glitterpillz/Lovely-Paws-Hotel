from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo_client = User(
        username="demo-client", email="demo-client@example.com", password="password",
        fname="Demo", lname="Client", address="200 Demo Lane", city="Demo City",
        state="DC", zip=12345, staff=False, position=None
    )
    demo_employee = User(
        username="demo-employee", email="demo-employee@example.com", password="password",
        fname="Demo", lname="Employee", address="100 Demo Lane", city="Demo City",
        state="DC", zip=12345, staff=True, position="Employee"
    )
    demo_manager = User(
        username="demo-manager", email="demo-manager@example.com", password="password",
        fname="Demo", lname="Manager", address="300 Demo Lane", city="Demo City",
        state="DC", zip=12345, staff=True, position="Manager"
    )
    demo_owner = User(
        username="demo-owner", email="demo-owner@example.com", password="password",
        fname="Demo", lname="Owner", address="400 Demo Lane", city="Demo City",
        state="DC", zip=12345, staff=True, position="Owner"
    )
    john = User(
        username="johnsmith", email="johnsmith@example.com", password="password1",
        fname="John", lname="Smith", address="123 Main St", city="Redlands",
        state="CA", zip=92323, staff=False, position=None
    )
    jane = User(
        username="janedoe", email="janedoe@example.com", password="password2",
        fname="Jane", lname="Doe", address="456 Elm St", city="Springfield",
        state="IL", zip=62704, staff=False, position=None
    )
    micheal = User(
        username="michaelbrown", email="michaelbrown@example.com", password="password3",
        fname="Michael", lname="Brown", address="789 Oak St", city="Austin",
        state="TX", zip=73301, staff=False, position=None
    )
    sara = User(
        username="sarawilson", email="sarawilson@example.com", password="password4",
        fname="Sara", lname="Wilson", address="321 Pine St", city="Denver",
        state="CO", zip=80203, staff=False, position=None
    )
    david = User(
        username="davidlee", email="davidlee@example.com", password="password5",
        fname="David", lname="Lee", address="654 Cedar St", city="Seattle",
        state="WA", zip=98101, staff=True, position="Employee"
    )
    emily = User(
        username="emilydavis", email="emilydavis@example.com", password="password6",
        fname="Emily", lname="Davis", address="987 Maple St", city="Miami",
        state="FL", zip=33101, staff=True, position="Employee"
    )
    james = User(
        username="jameswhite", email="jameswhite@example.com", password="password7",
        fname="James", lname="White", address="159 Birch St", city="Chicago",
        state="IL", zip=60601, staff=True, position="Employee"
    )
    linda = User(
        username="lindagreen", email="lindagreen@example.com", password="password8",
        fname="Linda", lname="Green", address="753 Willow St", city="Phoenix",
        state="AZ", zip=85001, staff=True, position="Employee"
    )
    robert = User(
        username="roberthall", email="roberthall@example.com", password="password9",
        fname="Robert", lname="Hall", address="951 Spruce St", city="Atlanta",
        state="GA", zip=30301, staff=True, position="Employee"
    )
    elizabeth = User(
        username="elizabethmartin", email="elizabethmartin@example.com", password="password10",
        fname="Elizabeth", lname="Martin", address="147 Cherry St", city="Boston",
        state="MA", zip=20108, staff=True, position="Employee"
    )
    charles = User(
        username="charlesking", email="charlesking@example.com", password="password11",
        fname="Charles", lname="King", address="369 Poplar St", city="Nashville",
        state="TN", zip=37201, staff=True, position="Employee"
    )
    patricia = User(
        username="patriciajohnson", email="patriciajohnson@example.com", password="password12",
        fname="Patricia", lname="Johnson", address="258 Palm St", city="Orlando",
        state="FL", zip=32801, staff=True, position="Employee"
    )
    stephen = User(
        username="stephenmoore", email="stephenmoore@example.com", password="password13",
        fname="Stephen", lname="Moore", address="654 Cypress St", city="Dallas",
        state="TX", zip=75201, staff=True, position="Employee"
    )
    barbara = User(
        username="barbarathomas", email="barbarathomas@example.com", password="password14",
        fname="Barbara", lname="Thomas", address="846 Aspen St", city="San Diego",
        state="CA", zip=92101, staff=True, position="Employee"
    )
    daniel = User(
        username="danielhernandez", email="danielhernandez@example.com", password="password15",
        fname="Daniel", lname="Hernandez", address="927 Fir St", city="San Jose",
        state="CA", zip=95101, staff=True, position="Manager"
    )
    nancy = User(
        username="nancyadams", email="nancyadams@example.com", password="password16",
        fname="Nancy", lname="Adams", address="163 Pine St", city="Portland",
        state="OR", zip=97201, staff=True, position="Owner"
    )

    db.session.add(demo_client)
    db.session.add(demo_employee)
    db.session.add(demo_manager)
    db.session.add(demo_owner)
    db.session.add(john)
    db.session.add(jane)
    db.session.add(micheal)
    db.session.add(sara)
    db.session.add(david)
    db.session.add(emily)
    db.session.add(james)
    db.session.add(linda)
    db.session.add(robert)
    db.session.add(elizabeth)
    db.session.add(charles)
    db.session.add(patricia)
    db.session.add(stephen)
    db.session.add(barbara)
    db.session.add(daniel)
    db.session.add(nancy)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
