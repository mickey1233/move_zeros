def movezeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    print(nums)
    # c=0
    # for i in range(len(nums)):
    #    if nums[i]!=0:
    #        nums[i], nums[c]= nums[c], nums[i]
    #        c+=1


if __name__ == "__main__":
    movezeroes([0, 1, 0, 3, 12])
    movezeroes([0])
