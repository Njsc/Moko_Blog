from flask_script import Manager, Server
from app import create_app
from app.model import User, Post
from werkzeug.security import generate_password_hash

app = create_app()
manager = Manager(app)
manager.add_command("runserver",
                    Server(host='0.0.0.0',
                           port=5000,
                           use_debugger=True))


@manager.command
def add_user():
    admin = User(username='jiangyu', password=generate_password_hash('123jy123'))
    admin.save()


@manager.command
def add_post():
    user = User.objects(username='jiangyu').first()
    post = Post(title='Moko', content='Moko content', author=user, tags=['python', 'flask'], status=1)
    post.save()


if __name__ == '__main__':
    manager.run()
