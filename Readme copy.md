# Getting Started with Alokyoutubeapi

This project is using Django, DRF(django rest framework), and mongoDB Atlas(djongo engine).
### Start new Project
`django-admin startproject youtube_search`

### Start new app
use anyone
`django-admin startapp search` \
or
`python manage.py startapp search`

### runmigrations
`python manage.py makemigrations`

### migrate chages into database
`python manage.py migrate`

### create superuser for admin work
`python manage.py createsuperuser`


In the project directory, you can run:

### Home Page
http://127.0.0.1:8000/

`search your query from search box we will store in database and we will keep showing u all videos in database. `

### admin page
http://127.0.0.1:8000/admin/
#### use username and password both
`alok`

### list view in UI in cronologically reverse order
[http://127.0.0.1:8000/list/](http://127.0.0.1:8000/list/)

### Featch data from youtube API newly added nine videos will be shown in UI
[http://127.0.0.1:8000/featch/](http://127.0.0.1:8000/fetch/) \
[on GET](http://127.0.0.1:8000/fetch/)->   see UI to enter your query  \
[on POST](http://127.0.0.1:8000/fetch/)->  see all featched videos.



### show all videos in cronologically revese order of published time in UI
[http://127.0.0.1:8000/show/](http://127.0.0.1:8000/show/)
## This is real API seaction
### http://127.0.0.1:8000/api/
### http://127.0.0.1:8000/api/searchdata/
### http://127.0.0.1:8000/api/searchdata/1/
### http://127.0.0.1:8000/api/searchindex/
### http://127.0.0.1:8000/api/searchindex/1/
### http://127.0.0.1:8000/api/users/
### http://127.0.0.1:8000/api/users/1/
### http://127.0.0.1:8000/api/groups/
### http://127.0.0.1:8000/api/groups/1/

Runsthe app in the development mode \
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in your browser.

The page will reload when you make changes.\
You may also see any errors in the terminal.
