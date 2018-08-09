''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    # Blog
    Get().route('/blog','BlogController@show'),
    Post().route('/blog/create','BlogController@store'),
    Get().route('/posts','PostController@show'),
    Get().route('/post/@id','PostController@single'),

    Get().route('/post/@id/update','PostController@update'),
    Post().route('/post/@id/update','PostController@store'),
    Get().route('/post/@id/delete', 'PostController@delete'),

]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
]
