<?php

use App\User;
use App\Post;

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

/* authenticated user */

Route::group(array('middleware' => 'guest'), function()
{
  //Login route
  Route::get('login', function()
  {
  	return View::make('login');
  });


  Route::post('login',  function()
  {
  	$data = Request::only('username', 'password');


  	if(Auth::attempt($data))
  	{
  		return redirect('/');
  	}
  	else
  	{
  		return View::make('login')->with('error', 'Login failed');
  	}
  });


});

/* Unauthenticated users */

//Home route
Route::get('/', function()
{
  $posts = DB::table('post')->get();
  if(Auth::check())
    $user = Auth::user()->username;
  else
    $user = null;

  return View::make('home', array('posts' => $posts, 'username' => $user));
});

//Register route
Route::get('register', function()
{
  if(Auth::check())
    return redirect('/');
  else
    $user = null;

  return View::make('register')->with('username', $user);
});

Route::post('register', function()
{
  $data = Request::only('username', 'password');
  $user = array_pull($data, 'username');
  $pass = array_pull($data, 'password');

  if($user == '' or $pass == '')
    return View::make('register')->with('error', 'Please enter a username or password');

  $validator = Validator::make(array('username' => $user), array('username' => ['required', 'min:5']));

  if($validator->fails())
    return View::make('register')->with('error', 'Username already exists');

  $newuser = new User;
  $newuser->username = $user;
  $newuser->password = crypt($pass, '$5$rounds=110000$' . $_ENV['APP_KEY']);

  $newuser->save();
  return redirect('/');
});

//add-post route
Route::get('add-post', function()
{
  if(Auth::check())
    $user = Auth::user()->username;
  else
    $user = null;

  return View::make('add-post')->with('username', $user);
});

Route::post('add-post', function()
{
  $data = Request::only('title', 'content');
  DB::transaction(function($data) use ($data)
  {
    DB::table('post')->insert(array('title' => array_pull($data, 'title'), 'body' => array_pull($data, 'content')));
  });
  return redirect('/');
});

//logout route
Route::get('logout',function()
{
  Auth::logout();
  return redirect('/');
});


Route::controllers([
	'auth' => 'Auth\AuthController',
	'password' => 'Auth\PasswordController',
]);
