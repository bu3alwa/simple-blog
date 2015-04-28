@extends('master')
@section('content')
<h2>Register</h2>
        @if (isset($error))
          <strong>Error: </strong> {{ $error }}
        @endif
        <form action="{{ URL::to('register') }}" method=post>
        <dl>
          <dt>Username:
          <dd><input type=text name=username>
          <dt>Password:
          <dd><input type=password name=password>
          <dd><input type=submit value=Register>
          <dd><input type="hidden" name="_token" value="{{  csrf_token() }}">
        </dl>
      </form>
@stop
