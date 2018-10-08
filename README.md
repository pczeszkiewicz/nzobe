# Nozbe

## Author
Piotr Czeszkiewicz
piotr@czeszkiewicz.pl

## Quick start
#### Running locally
The easiest way to run the application is to use Docker.

https://github.com/pczeszkiewicz/nzobe.git . 
$ git checkout develop . 
$ cd nozbe_pczeszkiewicz . 
$ docker-compose build . 
$ docker-compose up . 

Next, use django command to import titles and names:

$ ./manage.py import_titles --file_path=title.basics.tsv.gz . 

$ ./manage.py import_names --file_path=name.basics.tsv.gz . 

#### Using Heroku app
The application has been deployed to Heroku: `https://nozbe-pczeszkiewicz.herokuapp.com/`. endpoints:

https://nozbe-pczeszkiewicz.herokuapp.com/api/title/ . 
https://nozbe-pczeszkiewicz.herokuapp.com/api/name/ . 


## Solution
I created a Django application using Django-REST framework, because this library allow to build full and complex 
REST API in easy way. 

#### GET /titles/
Returns list of movies in the database, example: 

https://nozbe-pczeszkiewicz.herokuapp.com/api/title/ . 
https://nozbe-pczeszkiewicz.herokuapp.com/api/title/?start_year=2004 . 
https://nozbe-pczeszkiewicz.herokuapp.com/api/title/?genres=short . 
https://nozbe-pczeszkiewicz.herokuapp.com/api/title/?start_year=2004&genres=short . 

#### GET/name/
Returns list of names with related movies, example: 

https://nozbe-pczeszkiewicz.herokuapp.com/api/name/ . 
https://nozbe-pczeszkiewicz.herokuapp.com/api/name/?search=foo . 

### Running locally
The solution can be run locally using Docker. 

$ cd nozbe_pczeszkiewicz . 
$ docker-compose build . 
$ docker-compose up . 
