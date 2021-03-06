from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class EventBridgeSchema(BaseModel):
    version: str
    id: str  # noqa: A003,VNE003
    source: str
    account: str
    time: datetime
    region: str
    resources: List[str]
    detailtype: str = Field(None, alias="detail-type")
    detail: Dict[str, Any]
