from typing import List


class Solution:
    def daysToFinish(self, time: List[int], book: List[int]) -> int:
        days = 0
        read = 0
        t = 0
        
        while t < len(time) and read < len(book):
            time_today = time[t]

            while read < len(book) and time_today >= book[read] :
                # print(f"reading: {book[read]}, timeleft: {time_today} read: {read}")
                time_today -= book[read]
                read += 1

            days += 1
            t += 1
        # print("days: ",days, "read: ",read)

        return days if len(book) == read else -1 
        


def run_tests():
    solution = Solution()

    tests = [
        ([60, 45, 90], [30, 20, 40, 50], 3),
        ([100, 100], [30, 40, 20], 1),
        ([30, 30, 30], [20, 40], -1),
        ([50, 50, 50], [50, 50, 50], 3),
        ([120], [30, 30, 30, 30], 1),
        ([20, 100, 20], [60, 20, 20], 2),
    ]

    for i, (time, book, expected) in enumerate(tests, 1):
        result = solution.daysToFinish(time, book)
        print(
            f"Test {i}:",
            "PASS" if result == expected else
            f"FAIL | got {result}, expected {expected}"
        )


if __name__ == "__main__":
    run_tests()