import time
from django.db import connection

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        query_count = 0

        # Measure the number of queries using a context manager
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            query_count = len(connection.queries)

        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        response["X-Request-Processing-Time"] = str(end_time - start_time)
        response['X-Database-Queries'] = str(query_count)
        print("time: ", str(end_time - start_time))
        print("query_count: ", str(query_count))
        return response
