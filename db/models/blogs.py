from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from core.connection.db_connection import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_deleted = Column(Boolean, server_default="false")
