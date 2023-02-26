import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'department '

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User')
