<!doctype html>
<title>Blog</title>
</head>
<body>

<section>
<h1>Menu</h1>
<ul>
    @if (isset($username))
        <li><a>Hi, {{ $username }}</a></li>
    @endif
  <li><a href="/">Home</a></li>
  <li><a href="add-post">Add Post</a></li>
  <li><a href="register">Register</a></li>
  <li>
      @if (Auth::check())
         <a href="{{ URL::to('logout') }}">log out</a>
      @else
         <a href="{{ URL::to('login') }}">log in</a>
      @endif
  </li>
</ul>
</section>
<section>
    @yield('content')
</section>
</html>
