from app.Post import Post

class BlogController:
    ''' Class Docstring Description '''

    def show(self):
        return view('blog')

    def store(self):
        Post.create(
            title=request().input('title'),
            body=request().input('body'),
            author_id=request().user().id
        )

        return 'post created'
