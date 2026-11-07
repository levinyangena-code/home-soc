"""Normalized event model shared by ingestion, detection, and the API."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


SourceType = Literal["router", "linux", "windows", "web", "docker"]
Outcome = Literal["success", "failure", "unknown"]


class NormalizedEvent(BaseModel):
    """A validated, source-neutral security event with its original raw line."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    timestamp: datetime
    source_type: SourceType
    host: str = Field(min_length=1, max_length=255)
    src_ip: str | None = None
    dst_ip: str | None = None
    dst_port: int | None = Field(default=None, ge=1, le=65535)
    user: str | None = Field(default=None, max_length=256)
    action: str | None = Field(default=None, max_length=256)
    outcome: Outcome = "unknown"
    process: str | None = Field(default=None, max_length=512)
    bytes_out: int | None = Field(default=None, ge=0)
    raw: str = Field(min_length=1)
