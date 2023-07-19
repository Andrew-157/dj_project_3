import tempfile
from datetime import date
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse


from movies.models import Movie, Director
from taggit.models import Tag, TaggedItem


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        director = Director.objects.create(name="Quentin Tarantino",
                                           photo=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        number_of_movies = 5
        for id in range(1, number_of_movies+1):
            Movie.objects.create(
                title=f'Movie {id}',
                synopsis=f'Cool movie {id}',
                release_date=date(1990 + id, 10, 14),
                country='US',
                poster=tempfile.NamedTemporaryFile(
                    suffix=".jpg").name,
                director=director,
            )

        number_of_tags = 5
        for id in range(1, number_of_tags+1):
            Tag.objects.create(name=f'Tag {id}')

        unused_tag = Tag.objects.create(name='Unused')

        movie_content_type = ContentType.objects.get_for_model(Movie)

        for id in range(1, 6):
            TaggedItem.objects.create(
                object_id=id,
                tag_id=id,
                content_type=movie_content_type
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('movies:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('movies:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/index.html')

    def test_correct_context_object_name_is_used(self):
        response = self.client.get(reverse('movies:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('genres' in response.context)

    def test_list_only_used_genres(self):
        number_of_used_tags = TaggedItem.objects.count()
        response = self.client.get(reverse('movies:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['genres']), number_of_used_tags)
