import os


SERVER_DEFAULTS = {
    "HOST": os.getenv("HOST, ""127.0.0.1"),
    "PORT": int(os.getenv("PORT", 8000)),
}

MONGO_DEFAULTS = {
    "MONGO_URL": os.getenv("MONGO_URI"),
    "COLLECTION_NAME": os.getenv("MONGO_COLLECTION_NAME", "heroku_7wmzjn5f")
}

S3_DEFAULTS = {
    "BUCKET_NAME": os.getenv("S3_BUCKET_NAME"),
    "ACCESS_KEY": os.getenv("S3_ACCESS_KEY"),
    "SECRET_ACCESS_KEY": os.getenv("S3_SECRET_ACCESS_KEY")
}

SERVER_ENDPONTS = {
    "RECEIPT":      "/receipts",
    "USER":         "/users"
}

_min = 60
_hr = 60 * _min
_day = 24 * _hr
_year = 365 * _day
BLOB_EXPIRATION = 1 * _year