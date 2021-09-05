def reverseAsciiEncodedString(encodeString):
    ans =""
    for i in range(len(encodeString)-1,0,-2):
        asciinum = int(encodeString[(i-1):(i+1)])
        ans += chr(asciinum)
    return ans


"""回文串 palindrome"""
"""palindrome data stream"""

if __name__ == '__main__':
    str = '7976'
    print(reverseAsciiEncodedString(str))