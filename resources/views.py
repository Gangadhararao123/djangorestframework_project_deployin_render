from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login

from .models import Resource
from .forms import ResourceForm, SignupForm


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("resource_list")
    return render(request, "signup.html", {"form": form})


@login_required
def resource_list_view(request):
    resources = Resource.objects.all()
    return render(request, "resource_list.html", {"resources": resources})


@login_required
def resource_upload_view(request):
    if request.user.role != "lecturer":
        return HttpResponseForbidden("Only lecturers can upload")

    form = ResourceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.uploaded_by = request.user
        obj.save()
        return redirect("resource_list")

    return render(request, "resource_upload.html", {"form": form})


@login_required
def resource_edit_view(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.uploaded_by != request.user:
        return HttpResponseForbidden("You cannot edit this resource")

    form = ResourceForm(request.POST or None, request.FILES or None, instance=resource)
    if form.is_valid():
        form.save()
        return redirect("resource_list")

    return render(
        request,
        "resource_edit.html",
        {"form": form, "resource": resource},
    )


@login_required
def resource_delete_view(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.uploaded_by != request.user:
        return HttpResponseForbidden("You cannot delete this resource")

    if request.method == "POST":
        resource.delete()
        return redirect("resource_list")

    return render(
        request,
        "resource_confirm_delete.html",
        {"resource": resource},
    )
