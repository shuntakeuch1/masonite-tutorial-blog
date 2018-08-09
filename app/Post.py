''' A Post Database Model '''
from config.database import Model
from orator.orm import belongs_to

class Post(Model):
    # __table__ = 'blog'
    __fillable__ = ['title','author_id','body']

    @belongs_to('author_id','id')
    def author(self):
        from app.User import User
        return User
