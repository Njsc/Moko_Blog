from flask_admin import Admin
from view import MyAdminIndex
from app.model import User, Post
from view import UserView, PostView


def create_admin(app=None):
    admin = Admin(app,
                  name='MokoBlog',
                  index_view=MyAdminIndex(),
                  base_template='admin/master_index.html'
                  )
    admin.add_view(UserView(User))
    admin.add_view(PostView(Post))
