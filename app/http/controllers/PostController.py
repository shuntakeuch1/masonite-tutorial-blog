from app.Post import Post

class PostController:
    ''' Class Docstring Description '''

    def show(self):
        posts = Post.all()

        return view('posts',{'posts': posts})

    def single(self):
        post = Post.find(request().param('id'))

        return view('single',{'post': post})

    def update(self):
        post = Post.find(request().param('id'))

        return view('update',{'post': post})

    def store(self):
        post = Post.find(request().param('id'))

        post.title = request().input('title')
        post.body = request().input('body')

        post.save()

        return 'post updated'

    def delete(self):
        post = Post.find(request().param('id'))
        post.delete()

        return 'post deleted'
