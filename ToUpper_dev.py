def ToUpper(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - (ord('a') - ord('A')))
    return char

# Примеры использования
print(ToUpper('a'))  # Ожидается 'A'
print(ToUpper('b'))  # Ожидается 'B'
print(ToUpper('z'))  # Ожидается 'Z'
print(ToUpper('A'))  # Ожидается 'A'
print(ToUpper('1'))  # Ожидается '1'
print(ToUpper('@'))  # Ожидается '@'
