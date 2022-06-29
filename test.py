from simpy import Store
import simpy
env = simpy.Environment(initial_time=0)
store = Store(env)

def put():
    while True:
        k = 'test'
        yield store.put(k)
        print("element kept at -",env.now)
        #yield env.timeout(1)

def ok():
    while True:
        print("element started to get",env.now)
        msg = yield store.get()
        print(msg)
        print("element print at - ",env.now)
        yield env.timeout(1)

env.process(ok())
env.process(put())
env.run(until=3)