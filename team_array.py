#!/usr/bin/python3
"""Illustrate related data models using ARRAY Data-Type"""
from sqlalchemy import create_engine, Column, String, ARRAY
from sqlalchemy.orm import sessionmaker, declarative_base
from uuid import uuid4


# Create engine and metadata object
# This is just for illustration, don't hard code sensitive data like password.
# Consider storing them as environmental variables
engine = create_engine("postgresql://many_user:many_pwd@localhost/many_db")
Base = declarative_base()


# Define the team model
class Team(Base):
    """Class definition of teams models."""
    __tablename__ = "teams"
    id = Column(String(50), primary_key=True, nullable=False, default=uuid4())
    name = Column(String(50), nullable=False)
    members = Column(ARRAY(String), nullable=False) # You can have ARRAY(Integer) as well

# Create the table in the database
Base.metadata.create_all(engine)

# Create a sessin engine to interact with database.
session = sessionmaker(bind=engine)
session = session()

# Add new team
new_team = Team(name="Developers", members=["Wisdom", "John", "Bush"])
session.add(new_team)
session.commit()

# Query the team
team = session.query(Team).filter_by(name="Developers").first()
print(team.id)
print(team.name)       # Outputs: Developers
print(team.members)    # Outputs: ['Alice', 'Bob', 'Charlie']
print(team.members[0]) # Outputs: Alice

"""
To update team
if team:
    # Example: Replace the entire list
    team.members = ["Alice", "Bob", "Charlie", "David"]

    # Example: Add a new member
    team.members.append("Eve")

    # Example: Remove a member
    team.members.remove("Bob")
"""

# Close the session
session.close()
