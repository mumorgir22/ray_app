import phonenumbers
from fastapi import HTTPException
from phonenumbers import NumberParseException
from starlette import status


def validate_phone_number(value: str) -> str:
    try:
        parsed_phone = phonenumbers.parse(value)
    except NumberParseException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The string supplied did not seem to be a phone number.",
        )
    if not phonenumbers.is_valid_number(parsed_phone):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid phone number",
        )
    return value


def validate_values(values: dict) -> dict:
    if not values:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Body can't be empty",
        )
    return values
