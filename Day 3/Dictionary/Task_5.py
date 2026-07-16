default_settings = {
    "theme": "light",
    "font": 12,
    "language": "English"
}

user_settings = {
    "theme": "dark",
    "font": 14
}

settings = default_settings | user_settings

print(settings)