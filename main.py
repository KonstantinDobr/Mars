from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Job
from forms.user import RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required
from forms.loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


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


if __name__ == '__main__':
    main()
