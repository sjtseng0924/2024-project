# 2024-project
## Backend
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

### Start existing container

```bash
docker start devproject_db
```

### Migrate

```bash
python manage.py migrate
```

### Run server

```bash
python manage.py runserver
```