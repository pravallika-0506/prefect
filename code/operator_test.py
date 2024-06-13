@flow(retries=0, retry_delay_seconds=5, log_prints=True)
def parse_job_url():
    operator = YeeduOperator(job_url='https://qa-gcp.yeedu.io/tenant/bf34353f-0df2-4015-a3fc-85ac437f967e/workspace/2/spark/conf/4/metrics?type=spark_job&page=1&limit=20',
                             connection_name='secureconnection',
                             login_password='loginpassword')
    operator.execute()
