# 2024-project
## Backend
API Documentation: [Backend README](backend/README.md)

### Environment
- Python 3.12.1
- Django 4.1.13
- djongo 1.3.6
- Channels 4.0.0

```bash
cd backend
pip install -r requirements.txt
```

### Run mongo container

```bash
docker run -p 27017:27017 --name devproject_db -d mongo:8.0.1
```

### Start existing container (If already running, skip this step)

```bash
docker start devproject_db
```

### Migrate Models to MongoDB

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run server

```bash
python manage.py runserver
```

### Admin
http://127.0.0.1:8000/admin/