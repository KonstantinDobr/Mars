from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Job


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # Капитан
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # Колонист 1
    user = User()
    user.surname = "Colonist1"
    user.name = "First"

    user.age = 20
    user.position = "navigator1"
    user.speciality = "engineer1"
    user.address = "module_2"
    user.email = "сolonist1@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # Колонист 2
    user = User()
    user.surname = "Colonist2"

    user.age = 25
    user.position = "navigator2"
    user.speciality = "engineer2"
    user.address = "module_3"
    user.email = "сolonist2@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # Колонист 3
    user = User()
    user.surname = "Colonist3"

    user.age = 23
    user.position = "navigator3"
    user.speciality = "engineer3"
    user.address = "module_4"
    user.email = "сolonist3@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    # Работа 1
    job = Job()
    job.team_leader = 1
    job.job = "Exploration of mineral resources"
    job.work_size = 16
    job.collaborators = "1, 4, 8"
    job.is_finished = True
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    # Работа 2
    job = Job()
    job.team_leader = 2
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    app.run()

@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()
