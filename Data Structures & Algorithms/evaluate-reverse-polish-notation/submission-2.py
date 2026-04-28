class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        

        for i in tokens:
            if i in "+-/*":
                right_num = nums.pop()
                left_num = nums.pop()

                if i == "+":
                    nums.append(left_num + right_num)
                elif i =="-":
                    nums.append(left_num - right_num)
                elif i =="*":
                    nums.append(left_num * right_num)
                elif i =="/":
                    nums.append(int(left_num / right_num))
            else:
                nums.append(int(i))

        return nums[0]