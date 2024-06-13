from prefect import flow, task
import requests
# from operators.test import YeeduOperator

@flow(retries=0, retry_delay_seconds=5, log_prints=True)
def parse_job_url():
    operator = YeeduOperator('job_url','secureconnection','loginpassword')
    operator.execute()
