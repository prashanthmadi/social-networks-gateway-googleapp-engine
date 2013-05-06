from tokenize import generate_tokens
import logging
tokenizedData = []
def tokenizer(inputline):
    for toknum, tokval, _, _, _  in generate_tokens(inputline):
        output = toknum + "|" + tokval + "|"
        logging.debug(output)
        tokenizedData.append(output)
    return tokenizedData


def tokenizerSimple(inputline):
    return inputline.split(" ")
