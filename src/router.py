import asyncio
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)

class NotificationRouter:
    def __init__(self):
        self.providers = {
            "email": self._send_email,
            "sms": self._send_sms,
            "push": self._send_push
        }

    async def _send_email(self, user: str, msg: str):
        await asyncio.sleep(0.5)
        logging.info(f"[EMAIL] Sent to {user}: {msg}")
        return True

    async def _send_sms(self, user: str, msg: str):
        await asyncio.sleep(0.2)
        logging.info(f"[SMS] Sent to {user}: {msg}")
        return True

    async def _send_push(self, user: str, msg: str):
        await asyncio.sleep(0.1)
        logging.info(f"[PUSH] Sent to {user}: {msg}")
        return True

    async def route(self, payload: Dict[str, Any]):
        user = payload.get("user")
        msg = payload.get("message")
        channels = payload.get("channels", ["email"])
        
        tasks = []
        for ch in channels:
            if ch in self.providers:
                tasks.append(self.providers[ch](user, msg))
            else:
                logging.warning(f"Unknown channel: {ch}")
                
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return all(r is True for r in results)
