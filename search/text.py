# from datetime import datetime
# from datetime import timezone
# time=datetime.fromisoformat('2020-01-06T00:00:00.000Z'[:-1]).astimezone(timezone.utc)
# time=time.isoformat(sep='T')
# print(time)
# print(type(time))

from asgiref.sync import sync_to_async
from time import sleep
from django_q.tasks import async_task

@sync_to_async
def crunching_stuff():
    sleep(10)
    print("Woke up after 10 seconds!")


async def index():
    context = {
        'msg' : "alokpatel m"
    }
    # asyncio.create_task(crunching_stuff())
    async_task("crunching_stuff", 10)
    print("alok")
    return context

index()



Q_CLUSTER = {
    'name': 'django_q_django',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': 'clustercfg.coderpaparedis.oxkdmz.memorydb.us-west-2.amazonaws.com',
        'port': 6379,
        'password': 'p948710311f252a334c3b21cabe0bd63f943f68f0824cd41932781e7793c785bf',
        'db': 0, }
}