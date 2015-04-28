@extends('master')

@section('content')
        @if (isset($error))
        <strong>Error: </strong> {{ $error }}
        @endif
        <form action="{{ URL::to('login') }}" method=post>
        <dl>
          <dt>Username:
          <dd><input type=text name=username>
          <dt>Password:
          <dd><input type=password name=password>
          <dd><input type=submit value=Login>
	        <dd><input type="hidden" name="_token" value="{{  csrf_token() }}">
        </dl>
      </form>
@stop
