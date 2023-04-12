import flask

from . import db_session
from .jobs import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_news(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).get(jobs_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'jobs': jobs.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))
        }
    )
