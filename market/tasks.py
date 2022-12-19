from .services import stock_register, quote_register, check_user_stocks
from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task(name = "task_stock_register")
def task_stock_register():
    logger.info("Loading stocks...")
    stock_register()
    logger.info("...Completed loading of stocks")
    return

@shared_task(name = "task_quote_register")
def task_quote_register():
    logger.info("Loading quotes...")
    quote_register()
    logger.info("...Completed loading of quotes")
    return

@shared_task(name = "task_check_user_stocks")
def task_check_user_stocks():
    logger.info("Checking user stokes...")
    check_user_stocks()
    logger.info("...Finishing user stokes check.")
    return
