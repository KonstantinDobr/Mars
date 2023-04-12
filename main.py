from flask import Flask, render_template, redirect, abort, request
from data import db_session, jobs_api
from data.users import User
from data.jobs import Job
from forms.user import RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.loginform import LoginForm
from forms.jobs import JobForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Job()
        job.job = form.title.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.team_leader = form.team_leader.data
        job.is_finished = form.is_finished.data
        db_sess = db_session.create_session()
        current_user.jobs.append(job)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление информации о работе',
                           form=form)

@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).filter(Job.id == id, (Job.user == current_user) | (current_user.id == 1)
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Job).filter(Job.id == id, (Job.user == current_user) | (current_user.id == 1)
                                          ).first()
        if job:
            form.title.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.team_leader.data = job.team_leader
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Job).filter(Job.id == id, (Job.user == current_user) | (current_user.id == 1)
                                          ).first()
        if job:
            job.job = form.title.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.team_leader = form.team_leader.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование информации о работе',
                           form=form
                           )


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
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
