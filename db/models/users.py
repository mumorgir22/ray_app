from sqlalchemy import VARCHAR, Column, Integer, String

from core.connection.db_connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    phone = Column(VARCHAR(20), nullable=True)
    city = Column(String, nullable=True)
