import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Schedule(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'schedules'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    class_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("classes.id"))
    my_class = orm.relationship('Class', back_populates='schedules')

    day_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("week_days.id"))
    day = orm.relationship('WeekDay')

    slot_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("time_tables.id"))
    slot = orm.relationship('TimeTable')

    lesson_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lessons.id"))
    lesson = orm.relationship('Lesson')

    def __repr__(self):
        return f'<Student> {self.id} {self.name} {self.my_class} {self.is_admin}'