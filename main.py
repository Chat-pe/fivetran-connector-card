from pprint import pprint
from create_connector import create_connector
from create_connect_card import create_connect_card

destination_id = "incurable_credited"
schema = "uncover_skin_klaviyo"
service = "klaviyo"
redirect_url = f"https://supaboard-credentials-manager.web.app/uncover-skin?success_platform={service}"

print("Creating connector...")
connector = create_connector(destination_id, schema, service)
print(f"Connector Id: {connector.id}")
print("Creating Connect Card")
connect_card = create_connect_card(connector.id, redirect_uri=redirect_url)


pprint(
    f"Share this URL with client: {connect_card.connect_card and connect_card.connect_card.uri}"
)
