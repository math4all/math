# Development tools

## VS Code setup

The following section will explain how to configure VS Code to have a better development experience.

### Suggested VS Code extensions

Here a list of extensions that can help developers to better work on the front-end code.

- [Eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint): provides both linting and formatting features and is easily customizable by using the `.eslintrc` file (see [here](https://eslint.org/docs/rules/)).

- [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer): useful extension to handle brackets in the code.

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker): useful to avoid typos.

- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense): provides suggestions when entering a path in the code.

- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces): detects and avoids unnecessary white spaces.

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): enable intellisense, formatting and other stuffs related to Python files.

### VS Code suggested settings

VS Code settings file and .vscode directory should not be included in the repository. This is a bad-practice because, in this way, if a developer has different settings in its local environment, it has to change the settings file to all developers, causing, potentially, conflicts.

For this project suggested VS Code settings are the following:

``` json
// .vscode/settings.json
{
    "editor.tabSize": 2,
    "workbench.editor.highlightModifiedTabs": true,
    "editor.minimap.enabled": false,
    "window.title": "${dirty}${activeEditorMedium}",
    "editor.renderWhitespace": "all",
    "trailing-spaces.trimOnSave": true,
    "files.trimFinalNewlines": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": true
    },
    "eslint.alwaysShowStatus": true,
    "eslint.options": {
        "extensions": [
            ".html",
            ".js",
            ".jsx"
        ]
    },
    "eslint.validate": [
        "javascript",
        "javascriptreact"
    ],
    "eslint.workingDirectories": [
        {
            "directory": "./frontend/src/",
            "changeProcessCWD": true
        }
    ],
    "python.pythonPath": "./venv/bin/python",
    "python.analysis.extraPaths": [
        "backend"
    ],
    "cSpell.words": [
        "asgi"
    ],
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.autoComplete.addBrackets": true,
    "python.analysis.completeFunctionParens": true,
}
```

## Debugging
To debug the backend, do the following:

- Set `DEBUGGER=True` in `./backend/.env`
- Add the following configuration in VS Code:
    ``` json
    // .vscode/launch.json
    {
        "configurations": [
            {
                // requires vscode extension: ms-python.python
                "name": "debugger",
                "type": "python",
                "request": "attach",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}/backend",
                        "remoteRoot": "/code"
                    }
                ],
                "port": 5678,
                "host": "localhost",
                "logToFile": true,
            }
        ]
    }
    ```
- Run `docker-compose up`
- Place a breakpoint in VS Code
- Click the Debug button

To debug the frontend, you can use the keyword `debugger` combined with Google Chrome developer tool.


## Intellisense and autosuggestions for backend
Since this is a dockerized project, it is not trivial to configure the proper interpreter with VS Code. Setting the correct interpreter is indeed fundamental to have intellisense and autosuggetions in our backend code. To this aim, we suggest an easy (even though not elegant) workaround: create a virtualenv and install the backend requirements, i.e.,
```
(root) ➜ python3 -m venv venv
(root) ➜ source venv/bin/activate
[venv] (root) ➜ cd backend
[venv] (backend) ➜ pip install -r requirements.txt
```
In this way, we will have the python interpreter in `./venv/bin/python` (which is almost identical to the one in the backend container) and we can set that easily in VS Code (see `"python.pythonPath": "./venv/bin/python"` in `settings.json` file above).

## Fabric commands
An additional `fabfile.py` module has been added to facilitate the development experience and to execute the following commands:

- `(root) ➜ fab ssh:{service-name}`: used to SSH inside a given container.

    !!! note
        `{service-name}` must be one of the following:

        - `backend`
        - `worker`
        - `frontend`
        - `postgres`
        - `docs`

- `(root) ➜ fab remove_pyc`: used to remove `*.pyc` files from the backend
- `(root) ➜ fab remove_migrations`: used to remove migrations files from the backend
- `(root) ➜ fab reset_db`: used to reset the DB
- `(root) ➜ fab notebook`: used to start [Jupyter](https://jupyter.org/) notebook
- `(root) ➜ fab formatter`: used to format backend (through [black](https://github.com/psf/black) package) and frontend (through [eslint](https://eslint.org/) package)
- `(root) ➜ fab serve:{build-name}`: used to build the frontend and serve it at [http://localhost:4000](http://localhost:4000).

    !!! note
        `{build-name}` must be equal to `build`. In future, we might add new scripts in `package.json`, and therefore
        `{build-name}` will consequently be in a larger set of options.

## Code Analysis
The project also allows to do code analysis with SonarQube. To this aim, execute the following steps:

- run `docker-compose -f docker-compose.sonar.yaml up`
- access [http://localhost:9000](http://localhost:9000)
- if it is the first time that you do the login, then use the default credentials: `username: admin` & `password: admin` (the system will then enforce you to change the password)
- Now that you're logged in to your local SonarQube instance, let's analyze a project:
    - Click the Create new project button.
    - Give your project a Project key and a Display name and click the Set Up button.
    - Under Provide a token, select Generate a token. Give your token a name, click the Generate button, and click Continue.
    - Select your project's main language under Run analysis on your project, and follow the instructions to analyze your project. Here you'll download and execute a Scanner on your code (if you're using Maven or Gradle, the Scanner is automatically downloaded).
