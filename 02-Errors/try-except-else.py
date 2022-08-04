class User:
    def __init__(self, name: str, score: dict):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"<User {self.name} {self.score}>"


def calculate_score(user: User):
    return user.score["clicks"] * 5


def send_user_notification(user):
    try:
        calculate_score(user)
    except KeyError:
        print(f"Values for user '{user.name}' in wrong format.")
    else:
        print(f"Notification send to {user.name}")


def main():
    user = User("Rolf", {"clicks": 14})
    wrong_user = User("Pete", {"click": 14}) # KeyError -> clicks without s
    send_user_notification(user)
    send_user_notification(wrong_user)


if __name__ == "__main__":
    main()
