"""
Movies views
"""
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from movies.models import Movie
from genres.models import Genre


@require_POST
@csrf_exempt
def add_movie(request):
    """
    Operations with movies
    """
    movie = Movie.objects.create(
        name=request.POST.get('movie', None),
        rating=request.POST.get('rating', None),
        genre=Genre.objects.get(id=request.POST.get('genre', None))
    )

    return JsonResponse({'OK': f'movie\'s added, {movie.id}'})


@require_GET
def show_movies(request):
    """
    Show all movies
    """
    res = []

    for obj in Movie.objects.all():
        res.append(model_to_dict(obj))

    return JsonResponse(res, safe=False)


@require_GET
def show_current_movie(request, movie_id):
    """
    Show info about 1 movie
    """
    res = []

    for obj in Movie.objects.filter(id=movie_id):
        res.append(model_to_dict(obj))

    return JsonResponse(res, safe=False)


@require_GET
def delete_movie(request, movie_id):
    """
    Delete one movie
    """
    try:
        movie = Movie.objects.filter(id=movie_id).last()
        movie.delete()

        return JsonResponse({'Status': f'Movie {movie.id} was deleted'})

    except Movie.DoesNotExist:

        return JsonResponse({'Status': 'Not found'})


@require_POST
@csrf_exempt
def update_movie(request):
    """
    Update one movie
    """
    try:
        Movie.objects.filter(id=request.POST.get('movie', None)).update(
            name=request.POST.get('name', None),
            rating=request.POST.get('rating', None),
            genre=Genre.objects.get(id=request.POST.get('genre', None))
        )

        return JsonResponse({'Status': 'Movie was updated'})

    except Movie.DoesNotExist:

        return JsonResponse({'Status': 'Not found'})