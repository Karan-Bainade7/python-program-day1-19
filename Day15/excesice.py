# Python Match Case Statement Syntax

# The match-case syntax is based on structural pattern matching, which enables matching against data structures like sequences, mappings and even classes, providing more granularity and flexibility in handling various conditions. This feature is particularly useful when dealing with different types of data in a clear and organized manner.

# match subject:
#     case pattern1:
#         # Code block if pattern1 matches
#     case pattern2:
#         # Code block if pattern2 matches
#     case _:
#         # Default case (wildcard) if no other pattern matches

person= input("my case is")
match person:
        case "A":
            print("Hello, A!")
        case "B":
            print("Hello, B!")
        case _:
            print("Hello, stranger!")


            
