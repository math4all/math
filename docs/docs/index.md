# Getting started
This project is a boilerplate application based on [Django](https://www.djangoproject.com/) & [React](https://reactjs.org/). It contains useful examples that are common in
web development.

## Start the project
- Clone the repo
- Install [Docker](https://www.docker.com/products/docker-desktop)
- Install [Fabric3](https://pypi.org/project/Fabric3/)
- Add `.env` in `./backend` with content

    ``` text linenums="1" hl_lines="10-12"
    ENV=develop

    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_SSL_MODE=off
    SECRET_KEY=q$w!oi*7)x$=c#s(9+h@2prnbas$rsy-eh(#xm5fkd(vq3%^7o

    EMAIL_HOST={your-email-host}
    EMAIL_HOST_USER={your-email-host-user}
    EMAIL_HOST_PASSWORD={your-email-host-password}

    DOMAIN=localhost:3000
    SITE_NAME=socketio

    DEBUGGER=False
    ```

    !!! note
        Replace `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` with your emails credentials.

- Add `.env` in `./postgres` with content
    ``` text linenums="1"
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_SSL_MODE=off
    ```

- Add `.env` and `.env.local` in `./frontend` with content
    ``` text linenums="1"
    NODE_ENV=development
    REACT_APP_ENV=LOCAL
    SKIP_PREFLIGHT_CHECK=true
    REACT_APP_BACKEND_HOST=http://localhost:8000
    ```

- Add folders `./backend/storage/static` and `./backend/storage/media` that will contain Django's static & media files

- Open terminal at root level of the repo, and run
    ```
    (root) ➜ docker-compose run frontend yarn
    ```
    This will populate the `./backend/node_modules` folder, enabling ESLint in VS Code (see VS Code setup section)

- Open terminal at root level of the repo, and run
    ```
    (root) ➜ docker-compose up
    ```

- Open another terminal at root level of the repo, and run
    ```
    (root) ➜ fab reset_db
    ```

- Open the browser at [http://localhost:3000](http://localhost:3000) to see the React app, and login using credentials `admin@example.com / Passw0rd!`.

- Open the browser at [http://localhost:8000/admin](http://localhost:8000/admin) to see the Django admin, and login using credentials `admin@example.com / Passw0rd!`.

!!! warning "Windows issues"
    When running on Windows, be sure to setup Docker to run in Linux mode. Moreover, it can happens that `git` automatically restyled the EOL (End Of Line) of bash files. To avoid this problem, run this global command
    ```
    git config --global core.autocrlf input
    ```
    This command avoids the EOL (End Of Line) replacement. The latter is due to git which automatically reformat the file based on the current OS. As a conseguence, Linux-style EOL are replaced with Windows-style EOL.
