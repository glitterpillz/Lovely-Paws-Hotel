from app.models import db, PetImage, environment, SCHEMA
from sqlalchemy import text

def seed_pet_images():
    pet_images = [
        PetImage(pet_id=1, url='https://i.ibb.co/6t9vMfT/king-6.webp'),
        PetImage(pet_id=1, url='https://i.ibb.co/QmfNhHJ/king-1.jpg'),
        PetImage(pet_id=1, url='https://i.ibb.co/KL7GStk/king-2.jpg'),
        PetImage(pet_id=1, url='https://i.ibb.co/Db3HzsT/king-3.jpg'),
        
        PetImage(pet_id=2, url='https://i.ibb.co/60JFM5b/Kilo-2.png'),
        PetImage(pet_id=2, url='https://i.ibb.co/kSMJ9rw/Kilo-3.png'),
        PetImage(pet_id=2, url='https://i.ibb.co/Lxtwjgh/Kilo-4.png'),
        PetImage(pet_id=2, url='https://i.ibb.co/gw0mZnZ/Kilo-5.jpg'),
        
        PetImage(pet_id=3, url='https://i.ibb.co/nsbqBk0/Zeus-4.png'),
        PetImage(pet_id=3, url='https://i.ibb.co/4KssNzG/Zeus-3.png'),
        PetImage(pet_id=3, url='https://i.ibb.co/cQG55dB/Zeus-2.png'),
        PetImage(pet_id=3, url='https://i.ibb.co/p4h44Cb/Zeus-1.png'),
        
        PetImage(pet_id=4, url='https://i.ibb.co/FhVrF1W/Alex-dog-5.jpg'),
        PetImage(pet_id=4, url='https://i.ibb.co/yp3LktJ/Alex-dog-3.jpg'),
        PetImage(pet_id=4, url='https://i.ibb.co/rs7n2Ys/Alex-dog-2.jpg'),
        PetImage(pet_id=4, url='https://i.ibb.co/6RTXZQN/Alex-dog-1.jpg'),
        
        PetImage(pet_id=5, url='https://i.ibb.co/4tWrTwH/bella-4.jpg'),
        PetImage(pet_id=5, url='https://i.ibb.co/1dBJ6pQ/bella-3.jpg'),
        PetImage(pet_id=5, url='https://i.ibb.co/wSZRbKk/bella-1.png'),
        PetImage(pet_id=5, url='https://i.ibb.co/KrZh4ks/bella-5.png'),
        
        PetImage(pet_id=6, url='https://i.ibb.co/JpjF8DV/cosmo-2.jpg'),
        PetImage(pet_id=6, url='https://i.ibb.co/xCWP2kb/cosmo-3.jpg'),
        PetImage(pet_id=6, url='https://i.ibb.co/vPgtmBN/cosmo-4.jpg'),
        PetImage(pet_id=6, url='https://i.ibb.co/tZST4C5/cosmo-5.jpg'),
        
        PetImage(pet_id=7, url='https://i.ibb.co/WsH02wS/Wilson-5.jpg'),
        PetImage(pet_id=7, url='https://i.ibb.co/nL5YZp7/Wilson-4.jpg'),
        PetImage(pet_id=7, url='https://i.ibb.co/71f6F6V/Wilson-2.jpg'),
        PetImage(pet_id=7, url='https://i.ibb.co/frw3XsH/Wilson-1.jpg'),
        
        PetImage(pet_id=8, url='https://i.ibb.co/LzxYL3B/Kira-5.jpg'),
        PetImage(pet_id=8, url='https://i.ibb.co/R4w2ryb/Kira-3.jpg'),
        PetImage(pet_id=8, url='https://i.ibb.co/JFKPdPm/Kira-2.jpg'),
        PetImage(pet_id=8, url='https://i.ibb.co/T1k6SMt/Kira-1.jpg'),
        
        PetImage(pet_id=9, url='https://i.ibb.co/F3JFBgh/Roxy-4.jpg'),
        PetImage(pet_id=9, url='https://i.ibb.co/Q8Rcbky/Roxy-3.jpg'),
        PetImage(pet_id=9, url='https://i.ibb.co/18876T6/Roxy-2.jpg'),
        PetImage(pet_id=9, url='https://i.ibb.co/5G19NhD/Roxy-1.jpg'),
    
        PetImage(pet_id=10, url='https://i.ibb.co/82tRbQM/harris2.jpg'),
        PetImage(pet_id=10, url='https://i.ibb.co/cvPf7j3/harris3.jpg'),
        PetImage(pet_id=10, url='https://i.ibb.co/b6rr1bW/harris4.jpg'),
        PetImage(pet_id=10, url='https://i.ibb.co/4TRbB82/harris5.jpg'),
    ]

    for pet_image in pet_images:
        db.session.add(pet_image)

    db.session.commit()

def undo_pet_images():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.pet_images RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM pet_images"))

    db.session.commit()