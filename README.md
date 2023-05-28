## Places Remember
#### This web application is a service for storing impressions about visited places.
#### Users can log in with their Vkontakte account and keep their list of places they have visited.
#### This will help them track their travels and share their recommendations with friends.

## Installation
### To install the application, you need to clone the repository:
```
git clone https://github.com/Khlff/placesRememberProject.git
cd placesRememberProject
```
          
* ### Launching locally:
  ```
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
  ```
  The application will be available at http://localhost:8000/
* ### In Docker container:
  ```
  docker-compose up -d
  ```
  The application will be available at http://0.0.0.0:8000/

###  Made by Nikita Khlopunov