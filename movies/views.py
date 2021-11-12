"""
Movies views
"""
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


BASE_MOVIES = {
        'movie': ['Fight Club', 'Flying over the Cuckoos nest'],
        'rating': [9, 10],
}


@csrf_exempt
def add_movie(request):
    """
    Operations with movies
    """
    if request.method == 'GET':
        raise HttpResponseNotAllowed

    elif request.method == 'POST':
        new_movie = request.POST.get('movie', None)
        movie_rating = request.POST.get('rating', None)
        if new_movie and movie_rating:
            BASE_MOVIES['movie'].append(new_movie)
            BASE_MOVIES['rating'].append(int(movie_rating))
            return JsonResponse({'OK': 'movie\'s added'})

        return JsonResponse({'Error': 'Not found movie or rating'})

    raise HttpResponseNotAllowed


def show_movies(request):
    """
    Show all movies
    """
    if request.method == 'POST':
        raise HttpResponseNotAllowed

    return JsonResponse(BASE_MOVIES)


def show_current_movie(request, rating):
    """
    Show info about 1 movie
    """
    if request.method == 'POST':
        raise HttpResponseNotAllowed

    index = BASE_MOVIES['rating'].index(rating)

    return JsonResponse({BASE_MOVIES['movie'][index]: BASE_MOVIES['rating'][index]})
