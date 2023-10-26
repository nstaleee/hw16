def decorator_key_word_str(func):
    def operation_deco(*args, **kwargs):
        operation = func(*args, **kwargs)
        operation = str(operation)
        print(*args)
        print(kwargs)
        return operation

    return operation_deco

@decorator_key_word_str
def final(text: str, text2: str) -> str:
    return text + text2

result = final(text='Hel',text2='lo')
print(result)