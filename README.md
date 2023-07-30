# Base FastAPI framework

This base structure can be used to kick-start production ready app development.  
This framework is configured for python 3.10. Make sure to configure it for your 
project's python version.

## Configurations
Python version:
- Python v3.10.0

Code quality:
- Black

Database:
- Postgresql

ORM:
- Tortoise

Migrations:
- Aerich

Cache:
- Redis

Background Jobs:
- Celery
- Flower


## ⚠️ Caution for Windows users
If you are running this on Windows then chances are this will fail with error
```
error connecting in 'pool-1': Psycopg cannot use the 'ProactorEventLoop' to run in async mode. Please use a compatible event loop, for instance by setting 'asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())'
```

To fix this, add below code before executing function `create_database_connection`  
```
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
create_database_connection(app)
```
The reason for failing this is on Windows by default `ProactorEventLoop` is used for
asyncio operations. This has some limiting as mentioned here (https://github.com/psycopg/psycopg/issues/76)
.  
So, changing the event loop to some other event loop works.
