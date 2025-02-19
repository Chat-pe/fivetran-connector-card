from pydantic import BaseModel
from typing import Generic, Literal, Optional, List, TypeVar

"""
For Documentation: 
https://fivetran.com/docs/rest-api/api-reference/connectors/create-connector#createaconnector

TODO: Double check all models
"""

T = TypeVar("T", bound=BaseModel)


class ConnectorConfig(BaseModel):
    api_key: str
    schema: str  # type: ignore


class ConnectorAuth(BaseModel, Generic[T]):
    connector_auth_parameters: Optional[T] = None


class ConnectorCardConfig(BaseModel):
    redirect_uri: str
    hide_setup_guide: Optional[bool] = False


class CreateConnector(BaseModel):
    service: str
    group_id: str
    config: ConnectorConfig
    paused: Optional[bool] = True
    pause_after_trial: Optional[bool] = False
    trust_fingerprints: Optional[bool] = False
    trust_certificates: Optional[bool] = False
    run_setup_tests: Optional[bool] = True
    sync_frequency: Optional[int] = 5
    daily_sync_time: Optional[str] = None
    data_delay_sensitivity: Optional[Literal["LOW", "NORMAL", "HIGH"]] = "NORMAL"
    data_delay_threshold: Optional[int] = None
    schedule_type: Optional[str] = "manual"
    local_processing_agent_id: Optional[str] = None
    proxy_agent_id: Optional[str] = None
    private_link_id: Optional[str] = None
    networking_method: Optional[str] = None
    auth: Optional[ConnectorAuth] = None
    connect_card_config: Optional[ConnectorCardConfig] = None


class ConnectorStatusItem(BaseModel):
    code: Optional[str]
    message: Optional[str]
    details: Optional[str]


class ConnectorStatus(BaseModel):
    tasks: List[ConnectorStatusItem] = []
    warnings: List[ConnectorStatusItem] = []
    schema_status: Optional[str] = None
    update_state: Literal["on_schedule", "delayed"]
    setup_state: Literal["incomplete", "connected", "broken"]
    sync_state: Literal["scheduled", "syncing", "paused", "rescheduled"]
    is_historical_sync: bool
    rescheduled_for: Optional[str] = None


class ConnectorSetupTests(BaseModel):
    title: str
    status: Literal["PASSED", "SKIPPED", "WARNING", "FAILED", "JOB_FAILED"]
    message: Optional[str] = None
    details: Optional[dict] = None


class ConnectorCard(BaseModel):
    token: Optional[str]
    uri: Optional[str]


class Connector(BaseModel):
    id: str
    service: str
    schema: str  # type: ignore
    paused: bool
    status: ConnectorStatus
    daily_sync_time: Optional[str] = None
    succeeded_at: Optional[str] = None
    sync_frequency: int
    group_id: str
    connected_by: str
    setup_tests: List[ConnectorSetupTests] = []
    source_sync_details: Optional[dict] = None
    service_version: int
    created_at: str
    failed_at: Optional[str] = None
    private_link_id: Optional[str] = None
    proxy_agent_id: Optional[str] = None
    networking_method: Optional[
        Literal[
            "Directly",
            "SshTunnel",
            "PrivateLink",
            "ProxyAgent",
            "UnmanagedPrivateLink",
            "UnmanagedProxyAgent",
            "Unknown",
        ]
    ]
    connect_card: Optional[ConnectorCard] = None

    pause_after_trial: Optional[bool] = False
    data_delay_sensitivity: Literal["LOW", "NORMAL", "HIGH", "CUSTOM"]
    data_delay_threshold: Optional[int] = 30
    schedule_type: Optional[Literal["auto", "manual"]] = "manual"
    local_processing_agent_id: Optional[str] = None
    connect_card_config: Optional[ConnectorCardConfig] = None
    hybrid_deployment_agent_id: Optional[str] = None
    config: Optional[dict] = None

class CreateConnectCard(BaseModel):
    connect_card_config: ConnectorCardConfig

class ConnectCard(BaseModel):
    token: Optional[str]
    uri: Optional[str]


class ConnectCardResponse(BaseModel):
    connect_card: Optional[ConnectCard] = None
    connector_id: str
    connect_card_config: Optional[ConnectorCardConfig] = None
