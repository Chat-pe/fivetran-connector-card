from model import ConnectCardResponse, ConnectorCardConfig, CreateConnectCard
from common import make_request


# https://fivetran.com/connect-card/setup?redirect_uri=http://localhost:3000&auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkIjp7ImxvZ2luIjp0cnVlLCJ1c2VyIjoicXVhbnRpdGllc19yZWZ1cmJpc2giLCJhY2NvdW50IjoiY3VtYmVyc29tZV9jb2xsaWRlIiwiZ3JvdXAiOiJpbmN1cmFibGVfY3JlZGl0ZWQiLCJjb25uZWN0b3IiOiJmb3VnaHRfbGF3Z2l2ZXIiLCJtZXRob2QiOiJQYmZDYXJkIn0sImlhdCI6MTczODY5NTAzMX0.mq9KZ8ScNyoLUY9DNUazdWQPCLrAaGemHztDshrU9rA
def create_connect_card(connector_id: str, redirect_uri="https://app.supaboard.ai"):
    endpoint = f"/connectors/{connector_id}/connect-card"
    data = CreateConnectCard(
        connect_card_config=ConnectorCardConfig(
            redirect_uri=redirect_uri,
            hide_setup_guide=False,
        )
    )

    response = make_request(
        "post",
        endpoint,
        ConnectCardResponse,
        data=data.model_dump(),
    )

    return response
