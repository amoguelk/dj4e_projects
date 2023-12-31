from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad, Comment
from .owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerDeleteView,
)
from .forms import CommentForm, CreateForm


############
# Ad Views #
############
class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"

    def get(self, request, pk: int):
        """Gets and displays the ad with its comments and a form to add more comments

        Args:
            request (HttpRequest): The current request
            pk (int): The primary key of the ad

        Returns:
            HttpResponse: The page with the ad, comments and comment form
        """
        ad = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(ad=ad).order_by("-updated_at")
        comment_form = CommentForm()
        context = {"ad": ad, "comments": comments, "comment_form": comment_form}
        return render(request, self.template_name, context)


class AdCreateView(LoginRequiredMixin, View):
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("ads:all")

    def get(self, request):
        """Gets and displays a form to create an ad

        Args:
            request (HttpRequest): The current request

        Returns:
            HttpResponse: The response filled with the form
        """
        form = CreateForm()
        context = {"form": form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        """Posts the new ad information

        Args:
            request (HttpRequest): The current request

        Returns:
            HttpResponse | HttpResponseRedirect: The response filled with the form if there was an error, or a redirected response if it was successful
        """
        form = CreateForm(request.POST, request.FILES or None)

        # If there are errors
        if not form.is_valid():
            context = {"form": form}
            return render(request, template_name=self.template_name, context=context)

        # Add an owner
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("ads:all")

    def get(self, request, pk: int):
        """Gets and displays a form to update an ad

        Args:
            request (HttpRequest): The current request
            pk (int): The primary key of the ad to be updated

        Returns:
            HttpResponse: The response filled with the form
        """
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        context = {"form": form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, pk: int = None):
        """Posts the updated ad information

        Args:
            request (HttpRequest): The current request
            pk (int, optional): The primary key of the ad to be updated

        Returns:
            (HttpResponse | HttpResponseRedirect): The response filled with the form if there was an error, or a redirected response if it was successful
        """
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        # If there are errors
        if not form.is_valid():
            context = {"form": form}
            return render(request, template_name=self.template_name, context=context)

        ad = form.save(commit=False)
        ad.save()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad


def stream_file(request, pk: int) -> HttpResponse:
    """Displays the ad picture

    Args:
        pk (int): The primary key of the ad

    Returns:
        HttpResponse: The page displaying the picture
    """
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response["Content-Type"] = ad.content_type
    response["Content-Length"] = len(ad.picture)
    response.write(ad.picture)
    return response


#################
# Comment Views #
#################


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        """Posts the comment

        Args:
            request (HttpRequest): The current request
            pk (int, optional): The primary key of the ad

        Returns:
            (HttpResponseRedirect | HttpResponsePermanentRedirect): A redirect to the ad page
        """
        ad = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST["comment"], owner=request.user, ad=ad)
        comment.save()
        return redirect(reverse("ads:ad_detail", args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    def get_success_url(self) -> str:
        ad = self.object.ad
        return reverse("ads:ad_detail", args=[ad.id])
