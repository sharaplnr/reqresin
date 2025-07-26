from voluptuous import Schema, Length, All

user = Schema({
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        })

response_list_users = Schema({
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": All([user], Length(min=1)),
    "support": {
        "url": str,
        "text": str
    }
})