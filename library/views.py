from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import books


class BookView(View):
    def get(self, request):
        book = books.objects.all()
        return render(request, "book/book.html", {"book_list": book})


class Resources(View):
    def get(self, request):
        return render(request, "book/library/resources.html", )


class BaseLibraries(View):
    def get(self, request):
        return render(request, "book/library/library_base.html", )


class DigitalLibrary(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class OpenSources(View):
    def get(self, request):
        return render(request, "book/library/opensource.html", )


class OpenAccessResources(View):
    def get(self, request):
        return render(request, "book/library/open_access_resources.html", )


class EducationOpenResources(View):
    def get(self, request):
        return render(request, "book/library/oer.html", )


class Services(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class ForFaculty(View):
    def get(self, request):
        return render(request, "book/library/forfaculty.html", )


class HelpResearch(View):
    def get(self, request):
        return render(request, "book/library/help_research.html", )


class LiaisonLibrarian(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class AboutUs(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class CollectionLocation(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class Rules(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class LibraryFigures(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class LibraryEvents(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class Staff(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class News(View):
    def get(self, request):
        return render(request, "book/library/about.html", )


class Contacts(View):
    def get(self, request):
        return render(request, "book/library/about.html", )

class Search(ListView):
    def get_queryset(self):
        return books.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context

class BookDetailView(View):
    def get(self, request, slug):
        Books = books.objects.get(url=slug)
        return render(request, "book/book_detail.html", {"Books": Books})