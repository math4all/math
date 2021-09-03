# Backend
Application's backend is based on [Django](https://www.djangoproject.com/).

## Requirements
In the following, we will list the main requirements used with the related capabilities.

### Django background tasks
[Django background tasks](https://django-background-tasks.readthedocs.io/en/latest/) is a databased-backed work queue for Django. It allows to execute long running processes in background.

!!! note
    This particular requirement is also used by the `worker` service, which is responsible for the execution of long running tasks.

### Django filters
[Django filters](https://django-filter.readthedocs.io/en/stable/) is a generic, reusable application to alleviate writing some of the more mundane bits of view code. Specifically, it allows users to filter down a queryset based on a model’s fields, displaying the form to let them do this.

### Django rest framework
[Django rest framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
Here some reasons for using it:

- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

### Django rest framework API Key
[Django API Key](https://florimondmanca.github.io/djangorestframework-api-key/) is a powerful library for allowing server-side clients to safely use your API. These clients are typically third-party backends and services (i.e. machines) which do not have a user account but still need to interact with your API in a secure way.

### Django reversion
[Django reversion](https://django-reversion.readthedocs.io/en/stable/) is an extension to the Django web framework that provides version control for model instances. In particular, provides the following features:

- Roll back to any point in a model instance’s history.
- Recover deleted model instances.
- Simple admin integration.

It is very useful as an audit tracking tool.

### Django split settings
[Django split settings](https://django-split-settings.readthedocs.io/en/latest/) organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards in settings file paths and mark settings files as optional.

### Djoser
[Djoser](https://djoser.readthedocs.io/en/latest/introduction.html) provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.

### DRF spectacular
[DRF spectacular](https://drf-spectacular.readthedocs.io/en/latest/) is an integral part of API development, and OpenAPI 3 is finally here to make that process a easier. By using drf-spectacular with Django rest framework, your schema and therefore your documentation & client will always stay close to your API.

### Faker
[Faker](https://faker.readthedocs.io/en/master/) is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.

### Pygal
[Pygal](http://www.pygal.org/en/stable/documentation/index.html) is a dynamic SVG charting library written in python. It is useful to embed info-graphics into PDF reports.

### Python socket.io
[Python socket.io](https://python-socketio.readthedocs.io/en/latest/) implements Socket.IO clients and servers that can run standalone or integrated with a variety of Python web frameworks. Useful to create real time applications with Python.

### Weasyprint
[Weasyprint](https://weasyprint.org/start/) is visual rendering engine for HTML and CSS that can export to PDF. It aims to support web standards for printing. It is extremely useful to generate PDF reports.

## Examples
Throughout the code, you'll be able to see an optimal set of examples, including:

- Models
- Serializers
- Filters
- Class & function based views
- Authentication & Permissions
- Real time communication
- PDF report generation
- Long running tasks execution

!!! tip
    It is highly recommended to check the code to see how to structure new backend features, and to visit requirements'
    user guides to learn how to use them.