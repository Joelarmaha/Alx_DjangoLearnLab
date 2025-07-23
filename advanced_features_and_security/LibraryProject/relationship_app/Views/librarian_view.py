from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
@login_required
def librarian_dashboard(request):
    return render(request, 'librarian_view.html', {'user': request.user})
