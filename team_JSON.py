#!/usr/bin/python3
"""Illustrate related data models using JSON Data-Type"""
from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
from uuid import uuid4

# Create engine and metadata object
# This is just for illustration, don't hard code sensitive data like password.
# Consider storing them as environmental variables
engine = create_engine("postgresql://many_user:many_pwd@localhost/many_db")
Base = declarative_base()


class Team(Base):
    """Class definition of teams models."""
    __tablename__ = "teams"
    id = Column(String(50), primary_key=True, nullable=False, default=uuid4())
    name = Column(String(50), nullable=False, unique=True)
    members = Column(JSON, nullable=False)


# Create the table in the database
Base.metadata.create_all(engine)

# Create a sessin engine to interact with database.
session = sessionmaker(bind=engine)
session = session()

# Add new team to developer team
members = {
    "Alice": {"role": "Developer", "email": "alice@example.com"},
    "Bob": {"role": "Tester", "email": "bob@example.com"},
    "Charlie": {"role": "Manager", "email": "charlie@example.com"}
}
new_team = Team(name="Developers", members=members)
session.add(new_team)
session.commit()

# Query the team
team = session.query(Team).filter_by(name="Developers").first()
print(team.name)       # Outputs: Developers
print(team.members)    # Outputs: The dictionary of members
print(team.members['Alice']['email']) # Outputs: alice@example.com

# Close the session
session.close()
