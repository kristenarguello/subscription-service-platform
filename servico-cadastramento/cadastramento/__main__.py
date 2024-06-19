import threading
import uvicorn
from .event_consumers.pgto_servico_cadastramento import event_consumer_init


def start_event_consumer():
    consumer_thread = threading.Thread(target=event_consumer_init)
    consumer_thread.daemon = True
    consumer_thread.start()


def main():
    start_event_consumer()

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
