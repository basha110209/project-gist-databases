class Gist:
    def __init__(self, github_id, description, created_at, updated_at, public):
        self.github_id = github_id
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.public = public

    def __repr__(self):
        return f"<Gist {self.github_id}>"
