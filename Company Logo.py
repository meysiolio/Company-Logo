from collections import Counter

if __name__ == '__main__':
    s = input()
    
    for i in Counter(sorted(s)).most_common(3):
        print(i[0],i[1])