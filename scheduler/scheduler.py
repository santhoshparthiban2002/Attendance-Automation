from apscheduler.schedulers.background import BackgroundScheduler
from .models import Job, JobExecution
from django.utils import timezone
from .jobs import *
def run_job(job,function):
    job_execution = JobExecution.objects.create(job=job,status='running')
    try:
        function()
        job_execution.status = 'success'
    except Exception as e:
        job_execution.error = str(e)
        job_execution.status = 'failed'
    finally:
        job_execution.save()


scheduler = BackgroundScheduler(timezone=timezone.get_current_timezone())


job1,created = Job.objects.get_or_create(job_name='auto_detect_sundays')
if created or  Job.objects.filter(job_name=job1).exists():
    scheduler.add_job(run_job, 'cron', args=[job1,auto_detect_sundays],minute="*",second=0)
    #scheduler.add_job(run_job, 'cron', args=[job1,auto_detect_sundays],year="*",day=1,month=1,hour=7,minute=0,second=0)

job2,created = Job.objects.get_or_create(job_name='auto_delete')
if created or  Job.objects.filter(job_name=job2).exists():
    #scheduler.add_job(run_job, 'cron', args=[job2,auto_delete],minute="*",second=0)
    scheduler.add_job(run_job, 'cron', args=[job2,auto_delete],year="*",day=1,month=1,hour=7,minute=0,second=0)


job3,created = Job.objects.get_or_create(job_name='attendance_absent')
if created or  Job.objects.filter(job_name=job3).exists():
    #scheduler.add_job(run_job, 'cron', args=[job3,attendance_absent],minute="*",second=0)
    scheduler.add_job(run_job, 'cron', args=[job3,attendance_absent],day="*",hour=14,minute=0,second=0)



scheduler.start()