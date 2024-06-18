from prefect import flow, task
from prefect.blocks.system import Secret
from operators.yeedu import YeeduOperator


@flow(retries=0, retry_delay_seconds=5, log_prints=True)
def notebook_run_30_hours():
    operator = YeeduOperator(job_url='http://10.50.0.178:5173/tenant/d3f52457-ba55-4a97-b067-d8f72fb6f9be/workspace/1/spark/notebook/1',
                             connection_name='login',
                             login_password='loginpassword')
    operator.execute()
