"""
The AddPostViewExerciseTest class tests the functionality of adding a post for an exercise plan.
The SeeExercisesTest class tests the functionality of viewing a list of exercise plans.
The DeleteExercisePostTest class tests the functionality of deleting an exercise plan.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from exercise.models import PostExercise
from exercise.forms import PostFormExercise


class AddPostViewExerciseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('add_post_exercise', kwargs={'pk': self.user.pk})
        self.data = {
            'text_exercise_type': 'test exercise type',
            'text_workout_plan': 'test workout plan',
            'text_week_day': 'test week day',
            'text_time': 'test time',
        }

    def test_add_post_exercise(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(PostExercise.objects.count(), 1)
        post = PostExercise.objects.first()
        self.assertEqual(post.user_id, self.user.pk)
        self.assertEqual(post.text_exercise_type, self.data['text_exercise_type'])
        self.assertEqual(post.text_workout_plan, self.data['text_workout_plan'])
        self.assertEqual(post.text_week_day, self.data['text_week_day'])
        self.assertEqual(post.text_time, self.data['text_time'])
         # testing the successful message
        messages = get_messages(response.wsgi_request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your exercise plan post was successful!')

    def test_add_post_exercise_invalid_form(self):
        self.data['text_exercise_type'] = ''
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(PostExercise.objects.count(), 0)

        form = response.context['form']
        self.assertEqual(form.errors['text_exercise_type'], ['This field is required.'])

    class SeeExercisesTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='12345')
            self.exercise = PostExercise.objects.create(
                user=self.user,
                text_exercise_type='Test Exercise Type',
                text_workout_plan='Test Workout Plan',
                text_week_day='Test Week Day',
                text_time='Test Time'
            )
            self.url = reverse('see_exercises', kwargs={'pk': self.user.pk})

        def test_get_queryset(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'my_exercises.html')
            self.assertQuerysetEqual(response.context['exercise_list'], [repr(self.exercise)])

        def test_get_queryset_with_no_exercises(self):
            self.exercise.delete()
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'my_exercises.html')
            self.assertQuerysetEqual(response.context['exercise_list'], [])

    class DeleteExercisePostTest(TestCase):

        def test_delete_exercise_post(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 302)

            # Check that the post is  really deleted
            post_exists = PostExercise.objects.filter(id=self.post_exercise.id).exists()
            self.assertFalse(post_exists)

            # Check that the user is redirected to the exercise list page
            redirect_url = reverse('exercise:exercises', kwargs={'pk': self.user_id})
            self.assertRedirects(response, redirect_url)

