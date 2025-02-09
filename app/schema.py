# #This refers to the schema  to define the shape of request and its also called the pydentic model
# from pydantic import BaseModel, EmailStr
# from datetime import datetime
# from typing import Optional
# from pydantic.types import conint
# from enum import Enum


# ##This handles what the user send to us
# class PostBase(BaseModel):
#     title: str
#     content: str
#     publish: bool = True


# class PostCreate(PostBase):#It will inherit everything from PostBase
#     pass



# #This will ensure that the users password doesnt return back for the user to see
# class UserOut(BaseModel):
#     id: int
#     email: EmailStr

#     class Config:
#          from_attributes = True

         

# #This handles what we send to the user
# class Post(PostBase):
#     id: int
#     # title: str
#     # content: str
#     # publish: bool
#     created_at: datetime
#     owner_id: int
#     owner:  UserOut


#     class Config:
#         from_attributes = True 


# class UserCreate(BaseModel):
#     #username: str
#     email: EmailStr
#     password: str
#     #created_at: datetime



# #Schema for the users login
# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

# #Schema for Token
# class Token(BaseModel):
#     access_token: str
#     token_type: str


# #Schema for Token Data
# class TokenDate(BaseModel):
#     id: Optional[str] = None


# # Add this to your schema.py
# class TokenData(BaseModel):
#     id: str



# class DirectionEnum(Enum):
#     upvote = 1
#     downvote = -1

# class Vote(BaseModel):
#     post_id: int
#     dir: DirectionEnum

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint
from enum import Enum


##This handles what the user sends to us
class PostBase(BaseModel):
    title: str
    content: str
    publish: bool = True


class PostCreate(PostBase):  # Inherits everything from PostBase
    pass


# This ensures that the user's password doesn’t return back to the user
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # ✅ Pydantic v2 fix


# This handles what we send to the user
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True  # ✅ Pydantic v2 fix


class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        from_attributes = True  # ✅ Ensures response validation works


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Schema for the user's login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for Token
class Token(BaseModel):
    access_token: str
    token_type: str


# Schema for Token Data
class TokenData(BaseModel):
    id: str  # ✅ Fixed typo (removed TokenDate)


class DirectionEnum( Enum):
    upvote = 1
    downvote = -1


class Vote(BaseModel):
    post_id: int
    dir: int#DirectionEnum
