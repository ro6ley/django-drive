![](https://tokei.rs/b1/github/ro6ley/django-drive?category=code)
[![HitCount](http://hits.dwyl.io/ro6ley/django-drive.svg)](http://hits.dwyl.io/ro6ley/django-drive)

# Django-Drive

A demo Django project showcasing the use of Django Administration to upload files to Amazon S3.

This repository contains the code for this [blogpost]() on [StackAbuse](https://stackabuse.com/).

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/ro6ley/django-drive.git
```

2. Check into the cloned repository
```
$ cd django-drive
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

5. Run migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```

6. Create a super user
```
$ python manage.py createsuperuser
```

7. Run the application
```
$ python manage.py runserver
```

8. Log in to the admin dashboard and populate Cars at http://localhost:8000/admin

9. Navigate to http://localhost:8000/cars and view the cars


## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
