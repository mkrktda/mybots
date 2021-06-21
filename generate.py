import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.disconnect()
for i in range(1000):
    p.stepSimulation()
    time.sleep( 1/60 )
