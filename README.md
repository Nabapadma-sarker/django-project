# django-project
using pyhton framework django and postgresql

## Used packages
    Django==3.0.5
    psycopg2-binary==2.8.6

## SASS
sass have been added for styling.
also bootstrap have been added.

for creating new design ```npm i``` command will install bootstrap and sass.
then ```npm run sass``` will runtime build the sass when you make change on style.scss.

### All Pages 
#### Top Page 
![Alt top page](./doc/blog1.png?raw=true "Top page")
#### Detail Page 
![Alt Detail page](./doc/blog2.png?raw=true "Detail page")
#### Update Page 
![Alt update page](./doc/blog2.png?raw=true "update page")

creating new post and commenting on the post as a login user. default form 
validation used.

## docker and docker-compose
for development environment 3 servies have been used.
    1. postgres
    2. django web server
    3. pgadmin4

for runnig the application use command:
          ``` docker-compose -f docker-compose.yml up -d ```