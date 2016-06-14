from celery.task.schedules import crontab
from celery.decorators import periodic_task
from mysite.utils import scrapers
from celery.utils.log import get_task_logger
from datetime import datetime

logger = get_task_logger(__name__)

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def scraper_example():
    logger.info("Start task")
    now = datetime.now()
    result = scrapers.scraper_example(now.day, now.minute)
    logger.info("Task finished: result = %i" % result)

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def scraper_get():
    now = datetime.now()
    logger.info("Start task get() at {0}".format(now))
    result = scrapers.get_feed()
    logger.info("Task finished: result = %s" % result)