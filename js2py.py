import re

def transpile_javascript_to_python(javascript_code):
    # Remove comments
    code = remove_comments(javascript_code)
    
    # Replace semicolons at the end of each line
    code = code.replace(';', '\n')
    
    # Transpile basic constructs
    code = transpile_constructs(code)
    
    return code

def remove_comments(code):
    # Remove single-line comments
    code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
    
    # Remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    
    return code

def transpile_constructs(code):
    # Transpile if statements
    code = re.sub(r'if\s*\((.*?)\)\s*\{', r'if \1:', code)
    
    # Transpile while loops
    code = re.sub(r'while\s*\((.*?)\)\s*\{', r'while \1:', code)
    
    # Transpile for loops
    code = re.sub(r'for\s*\((.*?);(.*?);(.*?)\)\s*\{', r'for \1;\2;\3:', code)
    
    # Transpile console.log
    code = code.replace('console.log', 'print')
    
    # Transpile variable declaration
    code = re.sub(r'var\s+(.*?)\s*=\s*(.*?);', r'\1 = \2', code)
    
    return code

# Example usage
javascript_code = '''
var x = 5;
if (x > 3) {
    console.log("Hello, world!");
}
'''

python_code = transpile_javascript_to_python(javascript_code)
print(python_code)
