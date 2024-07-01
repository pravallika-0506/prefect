from prefect import flow
from operators.yeedu import YeeduOperator
import logging
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials
from prefect.blocks.system import Secret
 
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
@flow(retries=0, retry_delay_seconds=5, log_prints=True)
def job_run_flow_remote():
    """
    Prefect flow to execute a Yeedu job.
 
    This flow uses the YeeduOperator to run a job specified by the job_url.
    The credentials and connection_details details are managed within the YeeduOperator using the block names.
    """
    # URL of the Yeedu Notebook or job
    job_url = 'http://dev-onprem-002.yeedu.io:8080/tenant/d3f52457-ba55-4a97-b067-d8f72fb6f9be/workspace/1/spark/notebook/2'
    logger.info(f"Job URL: {job_url}")
 
    # Connection name and login password block name are handled within the YeeduOperator
    connection_block_name = 'yeedu-onprem-http-connection'
    login_password_block_name = 'password-ldap'
    
    logger.info("Initializing Yeedu operator...")
 
    # Initialize and execute the Yeedu operator  
    operator = YeeduOperator(job_url=job_url,
                            connection_block_name=connection_block_name,
                            login_password_block_name=login_password_block_name)
        
    logger.info("Executing Yeedu job...")
    operator.execute()
    logger.info("Yeedu job execution completed.")
 
 
