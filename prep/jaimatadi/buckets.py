from typing import List


class Solution:
    def classifyStudents(self, scores: List[int]) -> List[int]:
        failed = reg_pass = dist = 0

        for s in scores:
            if s < 50:
                failed += 1
            elif s >= 50 and s <= 80:
                reg_pass += 1
            else:
                dist += 1

        return [failed, reg_pass, dist] 


def run_tests():
    solution = Solution()

    tests = [
        ([45, 72, 81, 49, 50, 95, 80], [2, 3, 2]),
        ([100, 90, 85], [0, 0, 3]),
        ([20, 30, 49], [3, 0, 0]),
        ([50, 60, 70, 80], [0, 4, 0]),
        ([49, 50, 80, 81], [1, 2, 1]),
    ]

    for i, (scores, expected) in enumerate(tests, 1):
        result = solution.classifyStudents(scores)
        print(
            f"Test {i}:",
            "PASS" if result == expected else
            f"FAIL | got {result}, expected {expected}"
        )


if __name__ == "__main__":
    run_tests()