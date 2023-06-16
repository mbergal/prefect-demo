from prefect import task  # type: ignore

from pipelines import container
from pipelines.config import ImportConfig
from pipelines.models.salesforce import (
    SalesforceJobId,
    SalesforceTableContent,
    SalesforceTableName,
)


@task(
    name="Start loading table query",
    task_run_name='Start loading table query for "{table}"',
)
def load_table_start_query(import_config: ImportConfig, *, table: str):
    sf_api = container.get_sf_api(import_config)

    # This is not exactly how it works, but it's close enough for the example
    job_id = sf_api.query(f"SELECT * FROM {table}")
    return job_id


@task(
    name="Get load table query result",
    task_run_name='Get load table query result {job_id} for table "{table}"',
    timeout_seconds=60,
    retry_delay_seconds=5,
    retries=12,
)
def load_table_get_result(
    import_config: ImportConfig,
    *,
    table: SalesforceTableName,
    job_id: SalesforceJobId,
) -> SalesforceTableContent:
    sf_api = container.get_sf_api(import_config)
    result = sf_api.result(job_id)
    if result is None:
        raise Exception("Result is not ready yet")
    else:
        return result
