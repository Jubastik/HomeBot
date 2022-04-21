import datetime

import flask
import sqlalchemy
from flask import request, jsonify, make_response

from API.api_modules.core import id_processing, IDError
from API.data import db_session
from API.data.classes import Class
from API.data.schedules import Schedule
from API.data.students import Student
from API.data.time_tables import TimeTable
from API.data.week_days import WeekDay

blueprint = flask.Blueprint(
    'additional',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/current_lessons/<platform>/<int:user_id>', methods=['GET'])
def current_lessons(platform, user_id):
    try:
        id = id_processing(platform, user_id)
    except IDError as e:
        return make_response(jsonify({'error': str(e)}), 404)
    db_sess = db_session.create_session()

    now_time = datetime.time(13, 30)  # После отладки надо сделать нормально!!!!
    past_time = datetime.time(10, 30)
    day = "понедельник"

    print(datetime.datetime.today().weekday())
    now_lesson = db_sess.query(Schedule).join(WeekDay).join(TimeTable).join(Class).join(Student) \
        .filter(Student.id == id, WeekDay.name == day,
                TimeTable.begin_time >= past_time,
                TimeTable.end_time < now_time).all()

    return jsonify({'lessons': [_.to_dict(only=('lesson.name',)) for _ in now_lesson]})
    if user_schedules is None:
        return make_response(jsonify({'error': 'Расписание на этот день не существует'}), 404)
    print(user_schedules)
    return jsonify({'data': [schedule.to_dict(only=('day.name', 'lesson.name', 'slot.number_of_lesson')) for
                             schedule in user_schedules]})