from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView, ListView, DeleteView
from .models import PostExercise
from .forms import PostFormExercise

class HomePageView(TemplateView):
    template_name = "home.html"

    # https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/TemplateView/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_object'] = "Welcome to a Healthier Life!"

        return context

#this class is for user upload a new exercise plan
class AddPostViewExercise(FormView):
    template_name = "new_exercise.html"
    form_class = PostFormExercise
    success_url = "/"    # on success send back to homepage

    # displays success messages:
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        PostExercise.objects.create(
            user_id=self.kwargs['pk'],
            text_exercise_type=form.cleaned_data['text_exercise_type'],
            text_workout_plan=form.cleaned_data['text_workout_plan'],
            text_week_day=form.cleaned_data['text_week_day'],
            text_time=form.cleaned_data['text_time']
        )

        messages.add_message(self.request, messages.SUCCESS, "Yor exercise plan post was successful!")
        return super().form_valid(form)


class SeeExercises(ListView):
    model = PostExercise
    template_name = 'my_exercises.html'
    context_object_name = 'exercise_list'

    def get_queryset(self):  # returns list of published exercises
       exercise_list = PostExercise.objects.filter(user_id=self.kwargs["pk"])

       return exercise_list


class DeleteExercisePost(DeleteView):  # delete list of exercises
    model = PostExercise
    template_name = 'my_exercises.html'

    def get(self, request, *args, **kwargs):
        model_list = PostExercise.objects.filter(user_id=kwargs["pk"])
        model_list.delete()

        return redirect('exercise:exercises', kwargs["pk"])



