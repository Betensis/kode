import json
from typing import Optional, Union

from core.settings import PROJECT_NAME


def logging_query(
    *, message: str, endpoint: str, error: Optional[Union[dict, list, str]] = None
):
    print(
        json.dumps(
            {
                "service": PROJECT_NAME,
                "message": message,
                "error": error,
                "endpoint": endpoint,
            }
        )
    )
