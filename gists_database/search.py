from .models import Gist

def search_gists(db_connection, github_id=None, created_at=None, **kwargs):
    query = "SELECT * FROM gists WHERE 1=1"
    params = {}

    if github_id:
        query += " AND github_id = :github_id"
        params['github_id'] = github_id

    if created_at:
        query += " AND datetime(created_at) = datetime(:created_at)"
        params['created_at'] = created_at

    for key, value in kwargs.items():
        if key.endswith('__gt'):
            query += f" AND datetime({key[:-4]}) > datetime(:{key})"
        elif key.endswith('__gte'):
            query += f" AND datetime({key[:-5]}) >= datetime(:{key})"
        elif key.endswith('__lt'):
            query += f" AND datetime({key[:-4]}) < datetime(:{key})"
        elif key.endswith('__lte'):
            query += f" AND datetime({key[:-5]}) <= datetime(:{key})"
        params[key] = value

    cursor = db_connection.execute(query, params)
    return cursor.fetchall()

