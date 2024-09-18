## **Instaloader: Полная документация**

**Instaloader** — это Python-библиотека, которая позволяет загружать фотографии, видео, истории и другую информацию из Instagram. 

### **Установка**

Установите Instaloader с помощью pip:

```bash
pip install instaloader
```

### **Основные функции**

1. **Загрузка профиля пользователя**

   Загрузите все посты (фото и видео) профиля пользователя, включая фотографии профиля.

   ```python
   import instaloader

   L = instaloader.Instaloader()

   # Загрузка всех постов профиля
   L.download_profile('username', profile_pic_only=False)

   # Загрузка только фотографии профиля
   L.download_profile('username', profile_pic_only=True)
   ```

2. **Загрузка историй**

   Загрузите все истории пользователя, если у вас есть доступ к этому профилю.

   ```python
   import instaloader

   L = instaloader.Instaloader()

   # Получение профиля
   profile = instaloader.Profile.from_username(L.context, 'username')

   # Загрузка историй
   for story in L.get_stories(userids=[profile.userid]):
       for item in story.get_items():
           L.download_storyitem(item, f"{profile.username}_stories")
   ```

3. **Загрузка постов по хештегу**

   Загрузите посты, соответствующие определенному хештегу.

   ```python
   import instaloader

   L = instaloader.Instaloader()

   # Загрузка постов по хештегу
   hashtag = instaloader.Hashtag.from_name(L.context, 'hashtag_name')

   for post in hashtag.get_posts():
       L.download_post(post, target=f"#{hashtag.name}")
   ```

4. **Авторизация и доступ к приватным аккаунтам**

   Для доступа к закрытым аккаунтам выполните вход в Instagram.

   ```python
   import instaloader

   L = instaloader.Instaloader()

   # Вход в Instagram
   L.login('your_username', 'your_password')

   # Загрузка профиля закрытого аккаунта
   L.download_profile('private_username')
   ```

5. **Получение информации о пользователе**

   Вы можете получить информацию о подписчиках, подписках и постах пользователя.

   ```python
   import instaloader

   L = instaloader.Instaloader()

   # Получение профиля
   profile = instaloader.Profile.from_username(L.context, 'username')

   # Получение списка подписчиков
   followers = profile.get_followers()
   for follower in followers:
       print(f"Follower: {follower.username}")

   # Получение списка подписок
   followees = profile.get_followees()
   for followee in followees:
       print(f"Followee: {followee.username}")
   ```

6. **Фильтрация постов по дате**

   Загрузите посты за определенный период.

   ```python
   import instaloader
   from datetime import datetime

   L = instaloader.Instaloader()

   # Получение профиля
   profile = instaloader.Profile.from_username(L.context, 'username')

   # Фильтрация постов по дате
   SINCE = datetime(2022, 1, 1)
   UNTIL = datetime(2022, 12, 31)

   for post in profile.get_posts():
       if SINCE <= post.date_utc <= UNTIL:
           print(f"Post URL: {post.url}, Likes: {post.likes}")
   ```

### **Дополнительные функции**

- **Загрузка IGTV и Highlights**: Instaloader поддерживает загрузку IGTV-видео и сохраненных историй (Highlights).

  ```python
  import instaloader

  L = instaloader.Instaloader()

  # Загрузка IGTV видео
  for post in instaloader.Hashtag.from_name(L.context, 'igtv').get_posts():
      L.download_post(post, target='igtv')

  # Загрузка Highlights
  profile = instaloader.Profile.from_username(L.context, 'username')
  for highlight in profile.get_highlights():
      for item in highlight.get_items():
          L.download_storyitem(item, f"{profile.username}_highlights")
  ```

- **Работа с комментариями**: Instaloader позволяет получать комментарии к постам.

  ```python
  import instaloader

  L = instaloader.Instaloader()

  # Получение профиля
  profile = instaloader.Profile.from_username(L.context, 'username')

  # Получение постов и комментариев
  for post in profile.get_posts():
      print(f"Post URL: {post.url}")
      for comment in post.get_comments():
          print(f"Comment by {comment.owner.username}: {comment.text}")
  ```

### **Настройки и параметры**

- **Параметры загрузки**: Вы можете настроить параметры загрузки, такие как количество постов, формат файла и т.д.

  ```python
  import instaloader

  L = instaloader.Instaloader(download_pictures=True, download_videos=True, download_video_thumbnails=True)
  ```

- **Профилирование и отладка**: Вы можете включить профилирование и отладочные сообщения для диагностики.

  ```python
  import instaloader

  L = instaloader.Instaloader()
  L.context.log_level = instaloader.logging.DEBUG
  ```

### **Полезные ссылки**

- [Instaloader GitHub Repository](https://github.com/instaloader/instaloader) — Основной репозиторий библиотеки.
- [Instaloader Wiki](https://github.com/instaloader/instaloader/wiki) — Документация и руководства по использованию.

---

## **Полный список методов и атрибутов**

**Instaloader**

- `Instaloader()`: Создание объекта Instaloader.
  - `download_profile(profile, profile_pic_only=False)`: Загрузка всех постов и (опционально) фотографии профиля пользователя.
  - `download_post(post, target)`: Загрузка конкретного поста.
  - `download_storyitem(storyitem, target)`: Загрузка истории.

**Profile**

- `Profile.from_username(context, username)`: Получение профиля пользователя по его имени.
- `profile.get_posts()`: Получение всех постов профиля.
- `profile.get_followers()`: Получение списка подписчиков профиля.
- `profile.get_followees()`: Получение списка подписок профиля.
- `profile.get_highlights()`: Получение сохраненных историй (Highlights) профиля.
- `profile.get_tagged_posts()`: Получение постов, в которых упоминается профиль.

**Post**

- `post.url`: URL поста.
- `post.date_utc`: Дата и время публикации поста в формате UTC.
- `post.likes`: Количество лайков поста.
- `post.caption`: Описание поста.
- `post.get_comments()`: Получение всех комментариев к посту.
- `post.get_likes()`: Получение пользователей, поставивших лайк посту.

**Hashtag**

- `Hashtag.from_name(context, hashtag)`: Получение объектов хештегов по их имени.
- `hashtag.get_posts()`: Получение всех постов с указанным хештегом.

**Story**

- `L.get_stories(userids)`: Получение историй пользователей по их ID.
- `story.get_items()`: Получение всех элементов (историй) в истории пользователя.

**Highlight**

- `profile.get_highlights()`: Получение сохраненных историй профиля.
- `highlight.get_items()`: Получение всех элементов (историй) в сохраненной истории.

### **Опции загрузки**

Instaloader поддерживает различные опции загрузки:

- `download_pictures`: Скачать фотографии (по умолчанию True).
- `download_videos`: Скачать видео (по умолчанию True).
- `download_video_thumbnails`: Скачать миниатюры видео (по умолчанию True).
- `save_metadata`: Сохранение метаданных (по умолчанию True).

### **Примеры**

**Загрузка профиля с фильтрацией по дате**

```python
import instaloader
from datetime import datetime

L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, 'username')

SINCE = datetime(2022, 1, 1)
UNTIL = datetime(2022, 12, 31)

for post in profile.get_posts():
    if SINCE <= post.date_utc <= UNTIL:
        L.download_post(post, target='filtered_posts')
```

**Скачивание всех историй с их сохранением**

```python
import instaloader

L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, 'username')

for story in L.get_stories(userids=[profile.userid]):
    for item in story.get_items():
        L.download_storyitem(item, f"{profile.username}_stories")
```

### **Примечания**

- **Политика использования**: Соблюдайте политику Instagram и их правила использования данных.
- **Аутентификация**: Для доступа к приватным аккаунтам и дополнительным функциям требуется аутентификация.
- **Ограничения API**: Имейте в виду, что Instagram может вводить ограничения на количество запросов и доступ к данным.
