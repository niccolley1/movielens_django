import datetime
from django.db import models
from django.utils import timesince
import datetime
from django.contrib.auth.models import User
from django.template import loader


# Things to do:
# Rename classes to singular
# movie_title to title
# drop movie_id and user_id in favor of built in id
# Reviews.user_id and movie_id remove _id

class Movie(models.Model):
    #standard information
    title = models.CharField(max_length=200)
    release = models.DateField()
    imdb_link = models.TextField(default="")
    imdb_id = models.TextField(default="")
    image_link = models.TextField(default="")

    # genre information
    g_unknown = models.IntegerField(default=0)
    g_action = models.IntegerField(default=0)
    g_adventure = models.IntegerField(default=0)
    g_animation = models.IntegerField(default=0)
    g_children = models.IntegerField(default=0)
    g_comedy = models.IntegerField(default=0)
    g_crime = models.IntegerField(default=0)
    g_documentary = models.IntegerField(default=0)
    g_drama = models.IntegerField(default=0)
    g_fantasy = models.IntegerField(default=0)
    g_noir = models.IntegerField(default=0)
    g_horror = models.IntegerField(default=0)
    g_musical = models.IntegerField(default=0)
    g_romance = models.IntegerField(default=0)
    g_scifi = models.IntegerField(default=0)
    g_thriller = models.IntegerField(default=0)
    g_war = models.IntegerField(default=0)
    g_western = models.IntegerField(default=0)

    # number of reviews
    avg_rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)


    def __str__(self):
        return str(self.id)

    def time_since_published(self):
        temp_date = datetime.datetime.strptime(self.release_date)
        return timesince.timesince(temp_date)

    @staticmethod
    def get_top(num):
        print("IN STATIC, NUM = ", num)
        num = int(num)
        sorted_movie = Movie.objects.filter(num_reviews__gte=20).order_by('-avg_rating', '-num_reviews')
        return sorted_movie[:num]


# 1|24|M|technician|85711
class Critic(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    zip_code = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return "{} Aged {}".format(self.sex, self.age)


# user id | item id | rating | timestamp.
# 253	465	5	891628467
class Review(models.Model):
    critic = models.ForeignKey(
        Critic,
        on_delete=models.CASCADE
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()


    def __str__(self):
        return "Movie - {}: Score - {}".format(self.movie,
                                               self.rating)

