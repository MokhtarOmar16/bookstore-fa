from core.database import Base
from sqlalchemy import String , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError,VerificationError
import re

ph = PasswordHasher()

class User(Base):
    __tablename__ = "users"
    
    email :Mapped[str] = mapped_column(String(254), nullable=False)
    hash_password :Mapped[str] = mapped_column(String(254),)
    
    
    @validates("email")
    def validate_email(self, key, value:str):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, value):
            raise ValueError(f"Invalid email format: {value}")
        return value
    
    @property
    def password(self):
        """
        Prevents direct access to the password attribute.

        Raises an AttributeError if an attempt is made to read the password property.
        """
        raise AttributeError("password is not a readable attribute")
    
    
    @property.setter
    def password(self, value) -> None:
        self.hash_password =ph.hash(value)
    
    def verify_password(self, password :str) ->bool:
        """
        Verifies a given plaintext password against the stored hash.

        Args:
            password (str): The plaintext password to verify.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        try:
            return ph.verify(self.hash_password, password)
        except VerifyMismatchError:
            # Passwords do not match.
            return False
        except VerificationError as e:
            # Catch other verification errors (e.g., hash format is invalid).
            print(f"Verification Error: {e}")
            return False
    
    
    
