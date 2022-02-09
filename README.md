# Simple-Fastapi-Blog

## Overview

This repository creates a simple blog website
in which the backend will be made via Python and utilising the FastAPI framework.
HTML and CSS was used in the frontend.

### How to Run Locally

Install the requirements with the following command:

```console
pip install -r requirements.txt
```

Then run the command in the terminal from the root:

```console
uvicorn app.main:app --reload --port 8080
```

Visit <http://127.0.0.1:8080/>  and you should see the homepage.

### Makefile Alternative to running locally

You can update your environment to ensure you're up to date with the following command.
This will git pull and install the requirements in one go:

```console
make update-env
```
The same uvicorn command could be run with the command:

```console
make up-api
```

## License

This project is licensed under the terms of the MIT license.
