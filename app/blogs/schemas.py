from pydantic import BaseModel, root_validator

from core.utils.validators import validate_values


class BlogSchemaResponse(BaseModel):
    id: int
    name: str
    description: str | None
    image: str | None


class BlogCreateSchema(BaseModel):
    name: str
    description: str | None
    image: str | None


class BlogUpdateSchema(BaseModel):
    name: str | None
    description: str | None
    image: str | None

    @root_validator(pre=True)
    def check_patch_values(cls, values: dict) -> dict:
        return validate_values(values)
