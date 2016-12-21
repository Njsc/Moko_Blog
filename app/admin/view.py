from flask_admin import AdminIndexView, expose
from flask_admin.contrib.mongoengine import ModelView
from wtforms import widgets, fields
from flask_login import current_user, logout_user, login_user
from form import LoginForm
from flask import url_for, redirect, request


class MyAdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login'))
        return super(MyAdminIndex, self).index()

    @expose('/login', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = form.get_user()
            login_user(user)
            redirect(url_for('.index'))

        self._template_args['form'] = form

        return super(MyAdminIndex, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


class UserView(ModelView):
    can_delete = False
    # can_create =

    def is_accessible(self):
        return current_user.is_authenticated()


class PostView(ModelView):
    column_display_pk = True
    form_overrides = dict(content=CKTextAreaField)
    create_template = 'admin/create_post.html'
    edit_template = 'admin/edit_post.html'
    column_choices = {
        'status': [
            (2, 'draft'),
            (1, 'published')
        ]
    }
    column_list = ('id', 'title', 'content', 'author', 'tags', 'status', 'create_time', 'modify_time')
    column_filters = ('title',)
    column_searchable_list = ('content',)
    column_sortable_list = ('create_time', 'modify_time')

    def is_accessible(self):
        return current_user.is_authenticated()
