import requests
import sqlite3

def import_gists_to_database(db, username, commit=True):
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)
    gists = response.json()

    cursor = db.cursor()
    for gist in gists:
        cursor.execute("""
            INSERT INTO gists (github_id, description, created_at, updated_at, public)
            VALUES (?, ?, ?, ?, ?)
        """, (gist['id'], gist['description'], gist['created_at'], gist['updated_at'], gist['public']))
    
    if commit:
        db.commit()
