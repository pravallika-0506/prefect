from prefect import flow, task
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials
from prefect.blocks.system import Secret
from operators.yeedu import YeeduOperator


@flow(retries=1, retry_delay_seconds=5, log_prints=True)
def yeedu_job_run():
    operator = YeeduOperator(job_url='https://qa-aws-002.yeedu.io/tenant/a6a9c5ea-57b6-4a1c-aa99-84645f675b62/workspace/20/spark/conf/890808/metrics?type=spark_job&page=1&limit=20',
                             connection_name='secureconnection',
                             login_password='loginpassword')
    operator.execute()




