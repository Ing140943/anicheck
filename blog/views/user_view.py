from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import UpdateProfileForm
from django.contrib.auth.decorators import login_required



class ProfilePageView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'blog/user_profile.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        locate = get_object_or_404(User, id=self.kwargs['pk'])
        object_list = self.object.reviews.filter().order_by('-pub_date')

        context = super(ProfilePageView, self).get_context_data(locate=locate, object_list=object_list, **kwargs)
        return context

@login_required
def update_user(request, **kwargs):
    profile_form = UpdateProfileForm(instance=request.user)
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()

            return redirect('blog:profile', pk=request.user.id)
    return render(request, 'blog/edit_profile.html', {'profile_form': profile_form})