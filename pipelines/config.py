from dataclasses import dataclass
from typing import List

from pipelines.models.salesforce import SalesforceTableName
from pipelines.models.organizations import OrgId


@dataclass
class ImportConfig:
    org_id: OrgId

    @dataclass
    class Salesforce:
        base_tables: List[SalesforceTableName]
        custom_tables: List[SalesforceTableName]
        url: str
        client_id: str
        client_secret: str

    @dataclass
    class Insights:
        upload_url: str

    salesforce: Salesforce
    insights: Insights
