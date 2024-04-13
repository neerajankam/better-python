import dis

print(dis.dis("{}"))
# Bytecode for above dis
#  0           0 RESUME                   0
#
#  1           2 BUILD_MAP                0
#              4 RETURN_VALUE            None
print("--------------")
print(dis.dis("dict()"))
import timeit

# Time required to create an empty dictionary using {}
time_literal = timeit.timeit("{}", number=1000000)

# Time required to create an empty dictionary using dict()
time_function = timeit.timeit("dict()", number=1000000)

print("Time using {}: ", time_literal)
print("Time using dict(): ", time_function)

# Time using {}:  0.03013368800020544(50% faster)
# Time using dict():  0.045174241000495385
# Bytecode
#  0           0 RESUME                   0
#
#  1           2 PUSH_NULL
#              4 LOAD_NAME                0 (dict)
#              6 PRECALL                  0
#             10 CALL                     0
#             20 RETURN_VALUE

# Byte code operations and explanation(https://docs.python.org/3/library/dis.html)
# RESUME(where)
# A no-op. Performs internal tracing, debugging and optimization checks.

# BUILD_MAP(count)
# Pushes a new dictionary object onto the stack. Pops 2 * count items so that the dictionary holds count entries

# RETURN_VALUE
# Returns with STACK[-1] to the caller of the function.

# PUSH_NULL
# Pushes a NULL to the stack. Used in the call sequence to match the NULL pushed by LOAD_METHOD for non-method calls.

# LOAD_NAME(namei)
# Pushes the value associated with co_names[namei] onto the stack. The name is looked up within the locals, then the globals, then the builtins.

# CALL(argc)
# CALL pops all arguments and the callable object off the stack, calls the callable object with those arguments,
# and pushes the return value returned by the callable object.