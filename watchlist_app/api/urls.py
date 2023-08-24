from django.urls import path
# from watchlist_app.api.views import MovieListAPIView, MovieDetailAPIView
from watchlist_app.api.views import WatchListAPIView, WatchDetailAPIView, StreamPlatformAPIView, \
    StreamPlatformDetailAPIView, ReviewListAPIView, ReviewDetailAPIView

# from watchlist_app.api.views import movie_list, movie_detail

urlpatterns = (
    # path('list/initial/', MovieListAPIView.as_view(), name='movie list'),
    # path('<int:pk>/initial/', MovieDetailAPIView.as_view(), name='movie details'),
    path('list/', WatchListAPIView.as_view(), name='watchlist list'),
    path('list/<int:pk>/', WatchDetailAPIView.as_view(), name='watchlist details'),
    path('stream/', StreamPlatformAPIView.as_view(), name='stream platform list'),
    path('stream/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='stream platform details'),

    path('stream/<int:pk>/review/', StreamPlatformDetailAPIView.as_view(), name='ala bala'),
    path('stream/review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review details'),

    # path('review/', ReviewListAPIView.as_view(), name='reviews list'),
    # path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review details'),
    # path('list/', movie_list, name='movie list'),
    # path('<int:pk>/', movie_detail, name='movie detail'),
)