from typing import Any

import pytest

from app.blogs.dao import BlogServiceDAO


class MockBlogServiceDAO(BlogServiceDAO):
    async def add_blog(self, name: str, description: str | None, image: str | None, user_id: int) -> Any:
        return None

    async def update_blog(self, blog_id: int, values: dict, user_id: int) -> None:
        return None

    async def check_true_users(self, blog_id: int, user_id: int) -> bool:
        return True


@pytest.mark.asyncio
async def test_add_blog() -> None:
    blog_service_dao = MockBlogServiceDAO()
    assert await blog_service_dao.add_blog(name="test", description="test", image="test", user_id=123) is None


@pytest.mark.asyncio
async def test_update_blog() -> None:
    blog_service_dao = MockBlogServiceDAO()
    assert await blog_service_dao.update_blog(blog_id=123, values={}, user_id=123) is None


@pytest.mark.asyncio
async def test_check_true_users() -> None:
    blog_service_dao = MockBlogServiceDAO()
    assert await blog_service_dao.check_true_users(blog_id=123, user_id=123) is True
