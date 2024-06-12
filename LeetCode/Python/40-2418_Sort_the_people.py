class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = list(zip(names, heights))
        
        people_sorted = sorted(people, key=lambda x: x[1], reverse=True)
        
        sorted_names = [person[0] for person in people_sorted]
        
        return sorted_names

        names1 = ["Mary", "John", "Emma"]
        heights1 = [180, 165, 170]
        print(sort_people(names1, heights1))  

        names2 = ["Alice", "Bob", "Bob"]
        heights2 = [155, 185, 150]
        print(sort_people(names2, heights2))


