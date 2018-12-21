from django_extensions.management.jobs import BaseJob


class Job(BaseJob):
    help = "My daily sample job."
    when = "minutely"

    # when = "secondly"

    def execute(self):
        # executing empty sample job
        print('minute task start')
        import time
        time.sleep(30)
        print('30 seconds passed')
        print('and 30 seconds left')
