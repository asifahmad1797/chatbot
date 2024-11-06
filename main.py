import re
import main_responses as main


def probability(message, word_inlist, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    
#for couting nd taking percentage of word taken from user by comparing from response
    for word in message:
        if word in word_inlist:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(word_inlist))
    for word in required_words:
        if word not in message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_ans(message):
    prob_list = {}

    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal prob_list
        prob_list[bot_response] = probability(message, list_of_words, single_response, required_words)

    # normal responses 
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'i'])

    #main responses 
    response(main.ADVICE, ['give', 'advice'], required_words=['advice'])
    response(main.EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(main.COMPANY,['company', 'institution'] , single_response=True)
    response(main.chet,['who','chetana'],single_response=True)
    response(main.sah,['who','sahil'],single_response=True)
    response(main.asi,['who','asif'],single_response=True)
    response(main.sri,['who','srinivas'],single_response=True)

    best_match = max(prob_list, key = prob_list.get)
   # print(prob_list)
   # print(f'Best match = {best_match} | Score: {prob_list[best_match]}')

    return main.unknown() if prob_list[best_match] < 1 else best_match


# for continuous question nd removing extra simbols
def ans(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_ans(split_message)
    return response

while True:
    print('AdaInsys: ' + ans(input('You: ')))
