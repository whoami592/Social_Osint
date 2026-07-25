from urllib.parse import quote


PLATFORMS = {
    "GitHub": "https://github.com/{username}",
    "Reddit": "https://www.reddit.com/user/{username}/",
    "X": "https://x.com/{username}",
    "Instagram": "https://www.instagram.com/{username}/",
    "TikTok": "https://www.tiktok.com/@{username}",
    "YouTube": "https://www.youtube.com/@{username}",
}


def generate_profiles(username):
    username = username.strip()

    if not username:
        return []

    results = []

    for platform, template in PLATFORMS.items():
        results.append({
            "platform": platform,
            "username": username,
            "url": template.format(username=quote(username))
        })

    return results