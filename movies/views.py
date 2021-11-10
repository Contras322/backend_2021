"""
Movies views
"""
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


BASE_MOVIES = {
        'movie': ['Бойцовский клуб'],
        'rating': [9],
}


@csrf_exempt
def add_movie(request):
    """
    Operations with movies
    """
    if request.method == 'POST':
        new_movie = request.POST.get('movie', None)
        movie_rating = request.POST.get('rating', None)
        if new_movie and movie_rating:
            BASE_MOVIES['movie'].append(new_movie)
            BASE_MOVIES['rating'].append(int(movie_rating))
            return JsonResponse({'OK': 'movie\'s added'})

        return JsonResponse({'Error': 'Not found movie or rating'})

    elif request.method == 'GET':
        raise HttpResponseNotAllowed

    raise HttpResponseNotAllowed


@csrf_exempt
def show_movies(request):
    """
    Show all movies
    """
    if request.method == 'GET':
        raise HttpResponseNotAllowed

    return JsonResponse(BASE_MOVIES)


@csrf_exempt
def show_current_movie(request, rating):
    """
    Show info about 1 movie
    """
    if request.method == 'GET':
        raise HttpResponseNotAllowed

    index = BASE_MOVIES['rating'].index(rating)

    return JsonResponse({BASE_MOVIES['movie'][index]: BASE_MOVIES['rating'][index]})
