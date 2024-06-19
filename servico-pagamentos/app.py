from mangum import Mangum
from pagamentos import create_app

app = create_app()
handler = Mangum(app, lifespan="off")
