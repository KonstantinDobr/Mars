from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
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


if __name__ == '__main__':
    main()
