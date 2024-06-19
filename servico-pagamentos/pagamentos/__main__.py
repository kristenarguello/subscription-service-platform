import uvicorn
from pydantic.error_wrappers import ValidationError


def main():

    uvicorn.run(
        "pagamentos:create_app",
        factory=True,
        reload=True,
        # host=sets.ATHENA_HOST,
        port=8001,
        workers=1,
    )


if __name__ == "__main__":
    main()
