# Example project

The demo lives in **[DLRSP/example](https://github.com/DLRSP/example)** on branch **`django-requests-api`**. It is a small Django site wired to this package.

## Clone and run

```shell
git clone --depth=50 --branch=django-requests-api https://github.com/DLRSP/example.git example-requests-api
cd example-requests-api

python -m venv env
source env/bin/activate
# Windows: env\Scripts\activate

pip install -r requirements/py312-django42.txt
# Pick another file under requirements/ if it matches your Python/Django versions.

python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) and browse the routes the example defines.

To use only this library in an existing project, you do not need the example: install **`django-requests-api`**, add **`requests_api`** to `INSTALLED_APPS`, and import from `requests_api` as in the [home page](../index.md).
