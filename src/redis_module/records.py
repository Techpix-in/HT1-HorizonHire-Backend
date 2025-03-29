from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional, ClassVar

class ResponseModel(BaseModel):
    token: str
    msg: str
    timestamp: str = datetime.now().isoformat()