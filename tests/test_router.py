import pytest
from src.router import NotificationRouter

@pytest.mark.asyncio
async def test_routing():
    router = NotificationRouter()
    payload = {
        "user": "skyler",
        "message": "System alert!",
        "channels": ["email", "push"]
    }
    success = await router.route(payload)
    assert success is True
