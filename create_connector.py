from model import CreateConnector, ConnectorConfig, Connector
from common import API_KEY, make_request


def create_connector(destination: str, schema: str, service: str):
    endpoint = "/connectors"

    data = CreateConnector(
        service=service,
        group_id=destination,
        config=ConnectorConfig(
            api_key=API_KEY,
            schema=schema,
        ),
    )

    response = make_request(
        "post",
        endpoint,
        Connector,
        data=data.model_dump(),
    )

    return response
