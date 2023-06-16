"""
Dependency injection container for pipelines.
Not really, but will do.
"""

from pipelines import services
from pipelines.config import ImportConfig
from pipelines.models.organizations import OrgId


def get_config(org_id: OrgId) -> ImportConfig:
    return ImportConfig(
        org_id=org_id,
        salesforce=ImportConfig.Salesforce(
            base_tables=["a", "b"],
            custom_tables=["c"],
            client_id="<client-id>",
            client_secret="<client-secret>",
            url="https://example.dev.salesforce.com",
        ),
        insights=ImportConfig.Insights(
            upload_url="https://example.dev.insights.com",
        ),
    )


def get_sf_api(config: ImportConfig) -> services.salesforce.SalesforceClient:
    sfapi = services.salesforce.SalesforceClient(
        config=services.salesforce.SalesforceClient.Config(
            url=config.salesforce.url,
            client_id=config.salesforce.client_id,
            client_secret=config.salesforce.client_secret,
        )
    )
    return sfapi


def get_s3_client(config: ImportConfig) -> services.s3.S3Client:
    s3_client = services.s3.S3Client(
        config=services.s3.S3Client.Config(
            AWS_CLIENT_ID="",
            AWS_CLIENT_SECRET="",
            AWS_BUCKET_NAME="",
            AWS_PATH_PREFIX="",
        )
    )
    return s3_client
