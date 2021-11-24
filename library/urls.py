from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookView.as_view()),
    path("resources", views.Resources.as_view(), name='resources'),
    path("library_bases", views.BaseLibraries.as_view(), name='library_bases'),
    path("digital_library", views.DigitalLibrary.as_view(), name='digital_library'),
    path("open_sources", views.OpenSources.as_view(), name='open_sources'),
    path("open_access_resources", views.OpenAccessResources.as_view(), name='open_access_resources'),
    path("education_open_resources", views.EducationOpenResources.as_view(), name='education_open_resources'),
    path("services", views.Services.as_view(), name='services'),
    path("for_faculty", views.ForFaculty.as_view(), name='for_faculty'),
    path("help_research", views.HelpResearch.as_view(), name='help_research'),
    path("liaison_librarian", views.LiaisonLibrarian.as_view(), name='liaison_librarian'),
    path("about", views.AboutUs.as_view(), name='about'),
    path("collection_location", views.CollectionLocation.as_view(), name='collection_location'),
    path("us_rules", views.Rules.as_view(), name='us_rules'),
    path("library_figures", views.LibraryFigures.as_view(), name='library_figures'),
    path("library_events", views.LibraryEvents.as_view(), name='library_events'),
    path("staff", views.Staff.as_view(), name='staff'),
    path("news", views.News.as_view(), name='news'),
    path("contacts", views.Contacts.as_view(), name='contacts'),

    path("search/", views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.BookDetailView.as_view(), name='book_detail'),
]
