"you can use the reverseWords functon to reverse the words in a sentence except punctuation"

def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = " ".join(inputWords)
    return output


if __name__ == "__main__":
    input = "this is a small test for reversing words"
    rw = reverseWords(input)
    print("raw: ",input)
    print("reverse: ",rw)