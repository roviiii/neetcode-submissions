class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       


        nums.sort() 
        returnList=[]
        
        
        for index in range(len(nums)):         
            if index!=0:

              if nums[index]==nums[index-1]:
                continue
            if nums[index]>0:
                break
            
            
            prefix=index+1
            suffix=len(nums)-1
            
            
            while prefix<suffix:

                
                total=nums[index]+nums[prefix]+nums[suffix]
                if total<0:
                    prefix+=1
                    

                elif total>0:
                    suffix-=1
                    

                else:
                 returnList.append([nums[index],nums[prefix],nums[suffix]])
                 prefix+=1
                 suffix-=1
                 while prefix < suffix and nums[prefix]==nums[prefix-1]:
                    prefix+=1


        return returnList
                

        