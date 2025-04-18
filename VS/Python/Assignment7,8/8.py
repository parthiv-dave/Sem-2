def decode_message(message):
    def helper(index, path):
        if index == len(message):
            result.append("".join(path))
            return
        if message[index] == '0':
            return
        helper(index + 1, path + [chr(int(message[index]) + 64)])
        if index + 1 < len(message) and 1 <= int(message[index:index + 2]) <= 26:
            helper(index + 2, path + [chr(int(message[index:index + 2]) + 64)])

    result = []
    helper(0, [])
    return result

message = input("Enter encoded message: ")
decoded_messages = decode_message(message)
print("Possible Decodings:", decoded_messages)