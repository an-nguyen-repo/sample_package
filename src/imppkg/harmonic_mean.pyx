
def harmonic_mean(nums: list[float]):
    H = len(nums)/ sum([1/num for num in nums])
    return H 
