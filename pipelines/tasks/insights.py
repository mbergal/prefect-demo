import time

import numpy as np
from prefect import task  # type: ignore

from pipelines import models
from pipelines.config import ImportConfig


@task
def calculate_insights(
    tables: models.salesforce.SalesforceTables,
) -> models.insights.Insights:
    # Takes time to calculate insights
    time.sleep(10)

    return models.insights.Insights(average=np.average([x for x in tables.values()]))  # type: ignore


@task
def post_insights(import_config: ImportConfig, insights: models.insights.Insights):
    time.sleep(3)
    print(f"Posting insights to {import_config.insights.upload_url}")
