## Masonite tutorial

```
$ git clone git@github.com:shuntakeuch1/masonite-tutorial-blog.git
$ cd masonite-tutorial-blog
$ cp .env-example .env
```

Edit .env 
```
DB_DRIVER=sqlite
DB_DATABASE=masonite
```
Create DB and Launch server
```
$ craft migrate
$ craft serve
```
http://localhost:8000/blog
