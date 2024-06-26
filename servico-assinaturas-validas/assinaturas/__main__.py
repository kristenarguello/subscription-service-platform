import uvicorn


def main():

    uvicorn.run("assinaturas:create_app", port=80, host="0.0.0.0")


if __name__ == "__main__":
    main()
