import pytest

from app.auth.dao import AuthServiceDAO


class MockAuthServiceDAO(AuthServiceDAO):
    async def check_users_exist(self, email: str | None, phone: str | None) -> bool:
        return True

    async def add_new_user(
        self, username: str, hashed_password: str, email: str | None, phone: str | None, city: str | None
    ) -> int:
        return 123

    async def login_user(self, email: str | None, phone: str | None) -> dict | None:
        return {"id": 123, "hashed_password": "test_password"}


@pytest.mark.asyncio
async def test_check_users_exist() -> None:
    auth_service_dao = MockAuthServiceDAO()
    assert await auth_service_dao.check_users_exist(email="test@example.com", phone=None) is True


@pytest.mark.asyncio
async def test_add_new_user() -> None:
    auth_service_dao = MockAuthServiceDAO()
    user_id = await auth_service_dao.add_new_user(
        username="new_user",
        hashed_password="new_password",
        email="new@example.com",
        phone="0987654321",
        city="new_city",
    )
    assert user_id == 123


@pytest.mark.asyncio
async def test_login_user() -> None:
    auth_service_dao = MockAuthServiceDAO()
    user = await auth_service_dao.login_user(email="test@example.com", phone=None)
    assert user["id"] == 123
    assert user["hashed_password"] == "test_password"
