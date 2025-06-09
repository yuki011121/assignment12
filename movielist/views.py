# Create your views here.
import csv
from django.shortcuts import render
from django.conf import settings
import os

CSV_FILE_PATH = os.path.join(settings.BASE_DIR, 'movielist', 'movies.csv')

def read_movies_from_csv():
    movies = []
    try:
        with open(CSV_FILE_PATH, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append(row)
    except FileNotFoundError:
        print(f"Error: The file {CSV_FILE_PATH} was not found.")
    return movies

def display_data(request):
    movies_data = read_movies_from_csv()
    context = {
        'movies': movies_data,
        'page_title': 'All Movies' 
    }
    return render(request, 'movielist/data_display.html', context)

def add_data(request):
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_director = request.POST.get('director')
        new_year = request.POST.get('year')
        new_genre = request.POST.get('genre')
        
        new_movie = {
            'Title': new_title,
            'Director': new_director,
            'Year': new_year,
            'Genre': new_genre
        }

        try:
            with open(CSV_FILE_PATH, mode='a', encoding='utf-8', newline='') as file:
                fieldnames = ['Title', 'Director', 'Year', 'Genre']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_movie)
        except Exception as e:
            print(f"Error writing to CSV: {e}")
        all_movies_from_disk = read_movies_from_csv()

        context = {
            'movies': all_movies_from_disk,
            'page_title': 'Movie List (New Movie Added!)'
        }
        return render(request, 'movielist/data_display.html', context)
    
    return render(request, 'movielist/add_form.html')
