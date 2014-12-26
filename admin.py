from flask import Flask
from flask.ext.admin import Admin, BaseView, expose
from app import app
from flask.ext.admin.contrib.sqla import ModelView
from models import User, Message, db

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

admin = Admin(app)
# admin.add_view(MyView(name='Users'))
# admin.add_view(MyView(name='Messages'))

class MyMessage(ModelView):
    # Override displayed fields
    column_list = ('message_id', 'author_id', 'text', 'pub_date')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyMessage, self).__init__(Message, session, **kwargs)
        
class MyUser(ModelView):
    # Override displayed fields
    column_list = ('id', 'username', 'email', 'care_giver', 'care_seeker')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyUser, self).__init__(User, session, **kwargs)
        


# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Message, db.session))
admin.add_view(MyUser(db.session))
admin.add_view(MyMessage(db.session))