from abc import abstractmethod

class Environment(object):
    @abstractmethod
    def __init__(self, rooms):
        self.rooms = rooms
        
    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')
        
    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n 
        
class Room:
    def __init__(self, number, status="dirty"):
        self.number = number
        self.status = status
        
class Agent(object):
    @abstractmethod
    def __init__(self): 
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass
    
class VaccumAgent(Agent):
    def __init__(self):
        pass
    
    def sense(self, env):
        self.environment = env
        
    def act(self):
        current_room_number = self.environment.current_room_number
        current_room = self.environment.rooms[current_room_number]
        
        if current_room.status == 'dirty':
            return 'clean' 
        elif current_room_number < len(self.environment.rooms) - 1:
            self.environment.current_room_number += 1
            return 'right'
        else:
            self.environment.current_room_number = 0
            return 'left' 

class NRooomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, rooms):
        self.rooms = rooms
        self.agent = agent
        self.current_room_number = 0
        self.delay = 1000 
        self.step = 1 
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            
            current_room = self.rooms[self.current_room_number]
            if res == 'clean':
                current_room.status ='clean' 
            elif res == 'right':
                self.current_room_number += 1
            else:
                self.current_room_number = 0
                
            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    
    def displayPerception(self):
        current_room = self.rooms[self.current_room_number]
        print("Perception at step %d is [%s,%s]" %(self.step, current_room.status, current_room.number))
        
    def displayAction(self):
        print("------- Action taken at step %d is [%s]" %(self.step, self.action))
        
    def delay(self, n=100):
        self.delay = n 
        
#Test program
if __name__ == '__main__': 
    rooms = [Room(i) for i in range(5)]
    vcagent = VaccumAgent() 
    env = NRooomVaccumCleanerEnvironment(vcagent, rooms)
    env.executeStep(50)
