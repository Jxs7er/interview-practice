var twoSum = function (nums, target) {
    const obj = {}

    for (let i = 0; i < nums.length; i++) {
        const key = target - nums[i]

        if (obj[key] !== undefined)
            return [obj[key], i]

        obj[nums[i]] = i
    }

    return []
};