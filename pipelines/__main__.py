from pipelines import flows
from pipelines.models.organizations import OrgId

print(flows.insights.produce_insights(OrgId("1234")))
