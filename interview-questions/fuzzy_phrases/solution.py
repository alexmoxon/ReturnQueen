import json
import re

# Regex pattern to check if phrase is one word off
check_next = r'\s*\w*\s+'

# Fuzzy Search Implementation via Python Standard Library
def phrasel_search(P, Queries):
    ans = [[]]
    #Loop through the sent Queries
    for j, sent in enumerate(Queries):
        #Loop through Phrases
        for phrases in P:
            temp = ""
            #Holds number of words in phrase
            p_count = phrases.split(" ")
            #Loops through the words in each Phrase
            for k, word in enumerate(phrases.split(" ")):
                #Loops through Queries applying regex to word + temp to be used in finding one offs
                if k < len(p_count)-1:
                    temp += word + check_next
                #Exact phrase matches
                else:
                    temp += word
            #Searches for all occurences of regex pattern within Queries
            match = re.findall(temp, sent)

            #Adding matches to the return list
            if match:
                if len(ans) == 0:
                    ans[0] = match
                else:
                    try:
                        ans[j] += match
                    except IndexError:
                        ans.append(match)
    return ans

    #ans = [[]]
    #return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        #print(P)
        returned_ans = phrasel_search(P, Queries)
        print(returned_ans)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
