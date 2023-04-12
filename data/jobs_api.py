import flask

from . import db_session
from .jobs import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Job).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))
                 for item in news]
        }
    )
