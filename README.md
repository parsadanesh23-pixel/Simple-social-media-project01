# Simple-social-media-project01
# 📝 Simple Notes App (Python OOP Project)

A practice project written in Python using **Object-Oriented Programming (OOP)**. Users can sign up and then post notes, view their own or other users' posts, and delete their posts. Data is stored locally in JSON files.

## ✨ Features

- User signup with username, name, and password
- Post a new note
- View a specific user's posts
- View your own posts
- Delete a post
- View all posts in the system

## 🗂️ Project Structure

```
.
├── user.py         # User signup class
├── menu.py         # Main menu and post management
├── users.json       # Simple user database
└── posts.json        # Simple post database
```

## 🛠️ Tech Stack

- Python 3
- `json` module for data storage (no real database needed)

## 🚀 How to Run

1. Make sure `users.json` and `posts.json` exist in the project folder (at least containing `{}`).
2. Run the program from the terminal:

```bash
python menu.py
```

3. Enter the number of the option you want from the menu shown.

## 📋 Menu Preview

```
1. post a note
2. see the posts of a person
3. see the posts of yourself
4. delete your post
5. see the every posts
6. exit
```

## 👤 Author

A practice project for learning Python and OOP concepts.
