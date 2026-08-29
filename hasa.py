class RAM:
    def __init__(self, memory, type):
        self.memory = memory
        self.type = type
    
    def Show(self):
        print(f"RAM: {self.memory}GB {self.type}")

class CPU:
    def __init__(self, cores: int, type: str, clockspeed: float):
        self.cores = cores
        self.type = type
        self.clockspeed = clockspeed
    
    def Show(self):
        print(f"CPU: {self.type}, {self.cores} cores @ {self.clockspeed}GHz")


class ROM:
    def __init__(self, storage: int, speed: int, type: str) :
        self.storage = storage
        self.speed = speed
        self.type = type
    
    def Show(self):
        print(f"ROM: {self.storage}GB {self.type} @ {self.speed}MB/s")


class Computer:
    def __init__(self, kwargs):
        self.RAM = RAM(kwargs['memoryRAM'], kwargs['typeRAM'])
        self.CPU = CPU(kwargs['coresCPU'], kwargs['typeCPU'], kwargs['clockspeedCPU'])
        self.ROM = ROM(kwargs['storageROM'], kwargs['speedROM'], kwargs['typeROM'])

C1Comps: dict = {
    'memoryRAM': 16,
    'typeRAM': 'DDR4',
    'coresCPU': 8,
    'typeCPU': 'Intel i7',
    'clockspeedCPU': 3.6,
    'storageROM': 512,
    'speedROM': 3500,
    'typeROM': 'NVMe SSD'
}

C1 = Computer(C1Comps)
C1.RAM.Show()
C1.CPU.Show()
C1.ROM.Show()
