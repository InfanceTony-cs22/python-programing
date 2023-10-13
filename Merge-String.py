def merge_the_tools(string, k):
    # your code goes here

   
 
    n = len(string)
    parts = [string[i:i+k] for i in range(0, n, k)]

    for part in parts:
        seen = set()
        result = []
        for char in part:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print("".join(result))





if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
