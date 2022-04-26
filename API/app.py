import sqlalchemy
from flask import Flask, make_response

from data import db_session
from data.CONSTANTS import day_id_to_weekday
from data.week_days import WeekDay
from api_modules import user_api, homework_api, class_api, schedule_api, time_table_api, additional_methods_api

app = Flask(__name__)


def main():
    db_session.global_init("db/API.db")
    app.register_blueprint(user_api.blueprint)
    app.register_blueprint(homework_api.blueprint)
    app.register_blueprint(class_api.blueprint)
    app.register_blueprint(schedule_api.blueprint)
    app.register_blueprint(time_table_api.blueprint)
    app.register_blueprint(additional_methods_api.blueprint)
    init_weekday()
    app.run(debug=True)



@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/test')
# def test():
#     print(get_next_lesson('27', "Русский"))
#     return 'Hello World!'

def init_weekday():
    db_sess = db_session.create_session()
    for weekday in day_id_to_weekday.values():
        wd = WeekDay(name=weekday)
        db_sess.add(wd)
        try:
            db_sess.commit()
        except Exception as e:
            pass
    return 'OK'


if __name__ == '__main__':
    main()
