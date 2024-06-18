import pathlib
import sys

import uvicorn
from pydantic.error_wrappers import ValidationError


def main():

    uvicorn.run(
        "cadastramento:create_app",
        factory=True,
        reload=True,
        # host=sets.ATHENA_HOST,
        port=8000,
        workers=1,
    )


if __name__ == "__main__":
    main()
