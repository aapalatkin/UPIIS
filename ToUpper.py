def ToUpper(char):
    # Проверка, что на вход подается ровно один символ
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    
    # Проверка, является ли символ строчной буквой латинского алфавита
    if 'a' <= char <= 'z':
        # Преобразование строчного символа в заглавный
        return chr(ord(char) - (ord('a') - ord('A')))
    
    # Возвращение символа без изменений, если он не является строчной буквой
    return char

# Примеры использования
print(ToUpper('a'))  # Ожидается 'A'
print(ToUpper('b'))  # Ожидается 'B'
print(ToUpper('z'))  # Ожидается 'Z'
print(ToUpper('A'))  # Ожидается 'A'
print(ToUpper('1'))  # Ожидается '1'
print(ToUpper('@'))  # Ожидается '@'

# Примеры ошибок
try:
    print(ToUpper('ab'))  # Ожидается ошибка
except ValueError as e:
    print(e)  # Ожидается вывод сообщения об ошибке

try:
    print(ToUpper(''))  # Ожидается ошибка
except ValueError as e:
    print(e)  # Ожидается вывод сообщения об ошибке
