import pathlib
import sys

import uvicorn
from pydantic.error_wrappers import ValidationError

# from .settings import Settings


def main():
    # sets = Settings()

    # uvicorn.run( need to change to ours
    #     "athena:create_app",
    #     factory=True,
    #     reload=True,
    #     host=sets.ATHENA_HOST,
    #     port=sets.ATHENA_PORT,
    #     workers=sets.ATHENA_WORKERS,
    # )
    pass


if __name__ == "__main__":
    main()
