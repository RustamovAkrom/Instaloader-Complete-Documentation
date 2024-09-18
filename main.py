import instaloader

il = instaloader.Instaloader()

username = "rustamovakromjon327"
profile = instaloader.Profile.from_username(il.context, username=username)


print(f"[+] Profile info: {username}\n{profile.biography}\nPosts count: {profile.mediacount}\nFollowers: {profile.followers}")


for post in profile.get_posts():
    print(post.url)


# Bu kod faqat ishlatib korish uchun...