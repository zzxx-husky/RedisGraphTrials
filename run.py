import redis
from redisgraph import Graph
import timeit

r = redis.Redis(host='localhost', port=6379)
redis_graph = Graph("pm_test", r)

qf = open('1000_edges.cypher', 'r')
query = ''.join(qf.readlines()[1:])

start = timeit.default_timer()
redis_graph.query(query)
finish = timeit.default_timer()
print("Time used: ", finish - start, " seconds")
