from __future__ import unicode_literals
from fabric.api import local


def ssh(service):
    """
    ssh into running service container
    :param service: ['math_docs']
    USAGE: fab ssh:service
    """
    assert service in ['math_docs'], "%s is unrecognized service"
    local('docker-compose exec %s sh' % service)


def remove_pyc():
    local('docker-compose exec backend find . -name \'*.pyc\' -delete')


def remove_migrations():
    local('docker-compose exec backend find . -path \'*/migrations/*.py\' -not -name \'__init__.py\' -delete')


def reset_db():
    """
    Reset db, migrate and generate fixtures.
    Useful when changing branch with different migrations.
    """
    # schema creation
    local('docker-compose exec backend python manage.py reset_db')
    local('docker-compose exec backend python manage.py makemigrations')
    local('docker-compose exec backend python manage.py migrate')
    local('docker-compose exec backend python manage.py init_db')


def notebook():
    """
    Start a jupyter notebook
    """
    local('docker-compose exec backend python manage.py shell_plus --notebook')


def formatter():
    """
    Perform linter check and fixes
    """
    local('docker-compose exec backend black . --exclude ".ipynb_checkpoints\/|.Trash-0\/|bin\/|etc\/|include\/|lib\/|share"')
    local('docker-compose exec frontend yarn lint --fix')


def serve(build):
    """
    fab serve:build
    """
    cmd = f'docker-compose exec frontend npm run-script {build}'
    local(cmd)
    cmd = 'docker-compose exec frontend serve -s build -l 4000'
    local(cmd)