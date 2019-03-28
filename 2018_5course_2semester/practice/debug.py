import pdb

def mean(nums):
    # list of numbers
    top = sum(nums)
    bot = len(nums)

    return float(top)/ float(bot)

if __name__ == '__main__':
    pdb.set_trace()
    buggie_list = [1,2,3,4,5,6,100]
    mean(buggie_list)
