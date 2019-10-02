# def find_number_occurrence(nums, target):
#       lower = 0
#       left = 0
#       right = len(nums)
#       while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] >= target:
#                   right = mid - 1
#             else:
#                   left = mid + 1
                  
#       if nums[left] != target:
#             return 0
#       lower = left
#       right = len(nums)
      
#       while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > target:
#                   right = mid - 1
#             else:
#                   left = mid + 1
                  
#       return left - lower

def find_number_occurrence(nums, target):
      def find_number_occurrence_r(nums, target):
            if len(nums) == 1:
                  return 1 if nums[0] == target else 0
            mid = (len(nums) - 1) // 2
            if nums[mid] == target:
                  return find_number_occurrence_r(nums[:mid], target) + (
                        find_number_occurrence_r(nums[mid + 1:], target)) + 1
            elif nums[mid] < target:
                  return find_number_occurrence_r(nums[mid + 1:], target)
            else:
                 return find_number_occurrence_r(nums[:mid], target)
      return find_number_occurrence_r(nums, target)     
            
if __name__ == '__main__':
      nums = [1 , 2, 3, 4, 4, 5, 6]
      print(find_number_occurrence(nums, 1))