import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed)

print(f'list = {speed} ')
print(f'the mean is {mean}')
print(f'the median is {median} ')
print(f'the mode is {mode}'  )
