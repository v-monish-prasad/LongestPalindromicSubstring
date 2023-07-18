def longestPalindromicSubstring(string):
    length = len(string)
    maxLength = 1
    longestPalindrome = string[0]

    for i in range(length):
        leftPointer, rightPointer = length - 1, i

        while leftPointer >= 0 and rightPointer < length:
            if string[leftPointer] != string[rightPointer]:
                break

            leftPointer -= 1
            rightPointer += 1

        if (rightPointer - leftPointer - 1) > maxLength:
            maxLength = rightPointer - leftPointer - 1
            longestPalindrome = string[leftPointer + 1:rightPointer]

    return longestPalindrome


if __name__ == "__main__":
    A = input()
    print(longestPalindromicSubstring(A))
