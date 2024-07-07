def MaxContSubarray(nums):
    T = nums[0]
    Vmax = nums[0]
    Tmin = min(0, T)
    for i in range(1, len(nums)):
        T = T + nums[i]
        if T-Tmin > Vmax: Vmax = T-Tmin
        if T<Tmin : Tmin = T
        print(i, T, Tmin, Vmax)
    return Vmax



if __name__ == '__main__':
    arr = [1.0, 2.0, -5.0, 4.0, -3.0, 2.0, 6.0, -5.0, -1.0]
    print(MaxContSubarray(arr))
