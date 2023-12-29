class Solution:
    def average(self, salary: List[int]) -> float:
        c=(sum(salary)-(max(salary)+min(salary)))/(len(salary)-2)
        return c