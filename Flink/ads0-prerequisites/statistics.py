# STATISTICS #

# DO NOT MODIFY CONSTANTS
MEASURES_SAMPLE = [
    10.1, 10.2, 9.9, 10.1, 11.3, 14.2, 12.3, 12.3, 12.3, 12.1, 12.3, 11.9,
    10.2, 10.1, 9.8, 8.9, 9.7, 9.8, 9.8, 10.2, 10.3, 10.5, 12.3, 10.1, 8.9,
    9.8, 10.5, 10.1, 10.6, 10.7, 10.0, 9.9, 13.0, 13.1, 13.0, 13.2, 14.0]


def median_and_means(measures):
    '''
    To get an accurate summary of a set of measure, this function computes the
    following value and returns them in a tuple:
        - median
        - mean (average)
        - mean of the values between the first quartile and third quartile

    E.g., median_and_means([1,2,3,4,5,6,7,8]) is (5, 5, 5)

    @param measures a list of measures
    @return a tuple (med, mean, mean_50) where med is the median of the values
    in measures, mean is the mean and mean_50 the mean of the 50% of value in
    the middle of the range.
    '''
    raise NotImplementedError
