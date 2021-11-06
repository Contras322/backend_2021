from django.shortcuts import render
from django.http import JsonResponse, Http404


BASE_MOVIES = {
        'name': ['Бойцовский клуб'],
        'rating': [9],
}


def movies(request):
    if request.method == 'POST':
        new_movie = request.POST.get('movie', None)
        movie_rating = request.POST.get('rating', None)
        if new_movie and movie_rating:
            BASE_MOVIES['name'].append(new_movie)
            BASE_MOVIES['rating'].append(movie_rating)
            return JsonResponse({'OK': 'movie\'s added'})

        else:
            return JsonResponse({'Error': 'Not found movie or rating'})

    elif request.method == 'GET':
        new_movie = request.GET.get('movie', None)
        movie_rating = request.GET.get('rating', None)
        if new_movie and movie_rating:
            BASE_MOVIES['name'].append(new_movie)
            BASE_MOVIES['rating'].append(movie_rating)
            return JsonResponse({'OK': 'movie\'s added'})

        else:
            return JsonResponse({'Error': 'Not found movie or rating'})

    raise Http404


def show_movies(request):
    return JsonResponse(BASE_MOVIES)


def show_current_movie(request, movie):
    index = BASE_MOVIES['rating'].index(movie)

    return JsonResponse({BASE_MOVIES['name'][index]: BASE_MOVIES['rating'][index]})
