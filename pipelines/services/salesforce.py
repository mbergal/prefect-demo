import random
from dataclasses import dataclass

import numpy as np

from pipelines import models


class SalesforceClient:
    @dataclass
    class Config:
        url: str
        client_id: str
        client_secret: str

    def __init__(
        self,
        config: Config,
    ) -> None:
        self.__config = config

    last_job_id: int = 0

    def query(self, query: str) -> models.salesforce.SalesforceJobId:
        SalesforceClient.last_job_id += 1
        return models.salesforce.SalesforceJobId(str(SalesforceClient.last_job_id))

    def result(
        self, job_id: models.salesforce.SalesforceJobId
    ) -> models.salesforce.SalesforceTableContent | None:
        # emulate results not available yet for some time
        if random.random() < 0.2:
            return np.random.rand(100, 100)
        else:
            return None
