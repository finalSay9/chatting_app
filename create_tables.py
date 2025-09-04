from database import engine, Base
from models import User  # import all your models

# This will create all tables defined in Base.metadata
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
