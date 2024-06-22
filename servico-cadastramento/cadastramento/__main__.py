import uvicorn


def main():

    uvicorn.run(
        "cadastramento:create_app",
        factory=True,
        reload=True,
        port=8000,
        workers=1,
    )


if __name__ == "__main__":
    main()
