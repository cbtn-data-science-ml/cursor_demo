def get_user(x: int) -> dict:
    """Return a user record for the given id."""
    return {"id": x, "name": "Guest"}

Update app.py to call it:
from utils.user_service import get_user

def main():
    user = get_user(42)  # we'll update this call site automatically
    print(user)

if __name__ == "__main__":
    main()
