import re


def contain_substr(text, substr):
    if text is None:
        return False
    return substr in text


def extract_number(text):
    return extract_re(text, r'(\d+\.?\d*|\d*\.?\d+)[^st|^nd|^rd|^th]')


def extract_index(text):
    return extract_re(text, r'1st|2nd|3rd|\d+th')


def extract_words(text):
    if text is not None:
        text = text.lower()
    return extract_re(text, r'[a-zA-Z-]+')


def extract_re(text, pattern):
    if text is None:
        return []
    pattern = re.compile(pattern)
    result = pattern.findall(text)
    return result


if __name__ == '__main__':
    print(extract_words(
        'Are the products in the 2nd, 4th and 5th images and tes-tt - suited for 30th degree delicate clean?'))
