# class StudentIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0  # Start from the first element
#
#     def __next__(self):
#         if self.index == len(self.data):
#             raise StopIteration
#         item = self.data[self.index]
#         self.index += 1
#         return item
#
# class StudentController:
#     def __init__(self):
#         self.list_student = []
#
#     def __iter__(self):
#         return StudentIterator(self.list_student)
#
# controller = StudentController()
# controller.list_student.append('jadne')
# controller.list_student.append('yufu')
#
# # Using the for loop is more idiomatic
# for item in controller:
#     print(item)
#
# # Or, if you prefer using the while loop:
# iterator = iter(controller)  # This is equivalent to controller.__iter__()
#
# while True:
#     try:
#         item = next(iterator)  # This is equivalent to iterator.__next__()
#         print(item)
#     except StopIteration:
#         break