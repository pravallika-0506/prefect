from prefect import flow, task
from prefect.blocks.system import Secret
from operators.yeedu import YeeduOperator


@flow(retries=0, retry_delay_seconds=5, log_prints=True)
def job_run_30_hours():
    operator = YeeduOperator(job_url='https://qa-aws-002.yeedu.io/tenant/a6a9c5ea-57b6-4a1c-aa99-84645f675b62/workspace/74/spark/conf/890813/metrics',
                             connection_name='login',
                             login_password='loginpassword')
    operator.execute()
