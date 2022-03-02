"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def helper(self,emp_id):
        self.imp = self.employee_data[emp_id][0]
        for i in range(len(self.employee_data[emp_id][1])):
            self.imp += self.helper(self.employee_data[emp_id][1][i])
      
        return self.imp   
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employee_data = {}
        self.imp = 0
        for i in range(len(employees)):
            self.employee_data[employees[i].id] = (employees[i].importance,employees[i].subordinates)
        return self.helper(id)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        