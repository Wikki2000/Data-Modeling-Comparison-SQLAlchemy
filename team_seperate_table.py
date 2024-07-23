#!/usr/bin/python3
"""Illustrate related data models using seperate table"""
from sqlalchemy import create_engine, Column, String, ForeignKey, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, Relationship
from uuid import uuid4


# Create engine and metadata object
# This is just for illustration, don't hard code sensitive data like password.
# Consider storing them as environmental variables
engine = create_engine("postgresql://many_user:many_pwd@localhost/many_db")
Base = declarative_base()


class Team(Base):
    """Models for team."""
    __tablename__ = "teams"
    id = Column(String(50), primary_key=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(50), nullable=False)

    members = Relationship("Member", backref="teams")

class Member(Base):
    """Models for team members."""
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(String(50), ForeignKey("teams.id"), nullable=False)
    name = Column(String(50), nullable=False)

# Create map table in database
Base.metadata.create_all(engine)

# Create a session engine to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create new team
team = Team(name="Developer")
session.add(team)
session.commit()

# Adding two members to the Developer team
member1 = Member(team_id=team.id, name="John Bush")
member2 = Member(team_id=team.id, name="Moses Tom")
members = [member1, member2]
session.add_all(members)
session.commit()

"""
Alternatively: You can query each class
# Query all members
members = session.query(Member).all()
for member in members:
    print(member.id, member.name)

# Query Team
team = session.query(Team).first()
print(team.id, team.name)
"""
# Query the database
for team in session.query(Team).all():
    print(f"Team: {team.name}, Members: {[member.name for member in team.members]}")

# Close database session
session.close()
