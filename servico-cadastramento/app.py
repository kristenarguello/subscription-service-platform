from mangum import Mangum
from cadastramento import create_app

app = create_app()
handler = Mangum(app, lifespan="off")
