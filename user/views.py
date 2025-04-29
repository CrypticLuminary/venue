from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserForm, CustomLoginForm, UserProfileForm
from .models import UserProfile

# User Registration
class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

# User Login
class UserLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'user/login.html'

# User Logout (simple)
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# Create User Profile
class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user/profile_create.html'
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# View User Profile
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'user/profile_view.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
