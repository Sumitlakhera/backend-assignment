from sqlalchemy.orm import Session
from app.db.models import User

def get_user_by_email(
        db: Session,
        email: str
):
    return (
        db.query(User)
        .filter((User.email == email))
        .first()
    )


def get_user_by_id(
        db: Session,
        User_id: int
):
    return(
        db.query((User))
        .filter((User.id == User_id))
        .first()
    )


def create_user(
        db: Session,
        name: str,
        email: str,
        hashed_password: str,
        role: str = "user"
):
    user = User(
        name= name,
        email =email,
        hashed_password = hashed_password,
        role = role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user