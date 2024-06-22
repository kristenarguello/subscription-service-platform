import uvicorn


def main():

    uvicorn.run(
        "assinaturas:create_app",
        factory=True,
        reload=True,
        port=8003,
        workers=1,
    )


if __name__ == "__main__":
    main()
