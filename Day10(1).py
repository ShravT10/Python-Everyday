# # Write a function run_length_encode(s)
# # that compresses a string using run-length encoding (counts of repeated characters).

# Input: "aaabbc"
# Output: "a3b2c1"

def run_length_encode(s):
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

# Test
print(run_length_encode("aaabbc"))  # Output: "a3b2c1"
