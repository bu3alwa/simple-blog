@extends('master')

@section('content')
    <ul class=entries>
    @if(isset($posts))
        @foreach ($posts as $post)
             <li><h2>{!! $post->title !!}</h2>{!! $post->body !!}</li>
        @endforeach
    @else
        <li><em>No Posts in the database</em></li>
    @endif
    </ul>
@stop
