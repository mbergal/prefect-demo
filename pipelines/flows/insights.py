from typing import List

from prefect import flow  # type: ignore

from pipelines import models, tasks
from pipelines.config import ImportConfig
from pipelines.container import OrgId, get_config


def load_salesforce_tables(
    config: ImportConfig,
) -> models.salesforce.SalesforceTables:
    tables = config.salesforce.base_tables + config.salesforce.custom_tables
    loaded_data = tasks.salesforce.load_table_start_query.map(config, table=tables)
    job_ids = [future.result() for future in loaded_data]

    results: List[models.salesforce.SalesforceTableContent] = [
        future.result()
        for future in tasks.salesforce.load_table_get_result.map(
            config, table=tables, job_id=job_ids
        )
    ]  # type: ignore

    return {table: result for (table, result) in zip(tables, results)}


@flow
def produce_insights(org_id: OrgId):
    config = get_config(org_id=org_id)
    tables = load_salesforce_tables(config)
    insights = tasks.insights.calculate_insights(tables)
    tasks.insights.post_insights(config, insights)
    return insights
