from django.views.generic import (
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        print("delete get_queryset called")
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
