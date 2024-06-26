import uvicorn
from pydantic.error_wrappers import ValidationError


def main():

    uvicorn.run(
        "pagamentos:create_app",
        host="0.0.0.0",
        port=80,
    )


if __name__ == "__main__":
    main()
