from typing import Any, Mapping, NewType

import numpy as np

SalesforceTableName = str

# Of course, this is not the real type for SalesForceTable
# it is here just for the sake of example
SalesforceTableContent = np.ndarray[Any, np.dtype[np.float64]]

SalesforceTables = Mapping[SalesforceTableName, SalesforceTableContent]

SalesforceJobId = NewType("JobId", str)
