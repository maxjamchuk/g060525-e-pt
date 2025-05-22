def calculate_sum(a,b):
    """Calculate sum of two numbers"""
    return a+b

def process_data(data):
    """Process data and return result"""
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add_data(self, x):
        self.data.append(x)
    
    def get_data(self):
        return self.data 