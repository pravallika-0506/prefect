from prefect import flow, task
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials
from prefect.blocks.system import Secret
from operators.yeedu import YeeduOperator


@flow(retries=1, retry_delay_seconds=5, log_prints=True)
def yeedu_job_run():
    operator = YeeduOperator(job_url='https://qa-gcp.yeedu.io/tenant/bf34353f-0df2-4015-a3fc-85ac437f967e/workspace/2/spark/conf/5/metrics?type=spark_job&page=1&limit=20',
                             connection_name='secureconnection',
                             login_password='loginpassword')
    operator.execute()




