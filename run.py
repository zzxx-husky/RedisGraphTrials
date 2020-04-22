import redis
from redisgraph import Graph
import timeit

r = redis.Redis(host='locahost', port=6379)
redis_graph = Graph("graph", r)

query = ""

start = timeit.default_timer()
redis_graph.query(query)
finish = timeit.default_timer()
print("Time used: ", finish - start, " seconds")
