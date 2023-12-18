from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from bson import ObjectId
from entity.commentDTO import Comment

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class CommentModel(BaseModel):
    """
    Container for a single result record.
    """

    # The primary key for the ResultDTO, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    # id: Optional[PyObjectId] = Field(alias="_id", default=None)
    comment: List[Comment] = Field(...)
    url: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "comment": ["comment"],
                "url": "url",
            }
        },
    )

class UpdateCommentModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """
    comment: Optional[Comment] = None
    url: Optional[str] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "comment": ["comment"],
                "url": "url",
            }
        },
    )
