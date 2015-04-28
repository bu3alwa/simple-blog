@extends('master')
@section('content')
<h2>Register</h2>
        @if (isset($error))
        <strong>Error: </strong> {{ $error }}
        @endif
        <form action="{{ URL::to('add-post') }}" method=post>
        <dl>
          <dt>Title:
          <dd><input type=text name=title>
          <dt>Body:
          <dd><input style="min-height: 100" type=text name=content>
          <dd><input type=submit value=submit>
          <dd><input type="hidden" name="_token" value="{{  csrf_token() }}">
        </dl>
      </form>
@stop
