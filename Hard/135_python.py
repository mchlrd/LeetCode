class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        up_count = 1
        down_count = 0
        candies_given = 1
        peak = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:

                up_count += 1
                down_count = 0
                candies_given += up_count
                peak = up_count

            elif ratings[i] == ratings[i-1]:
                down_count = 0
                peak = 0
                up_count = 1
                candies_given += 1
            else:
                down_count += 1
                up_count = 1
                candies_given += down_count
                if peak <= down_count:
                    candies_given += 1

        return candies_given