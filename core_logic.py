import ast
import operator as op
import math

# supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def eval_expr(expr):
    """
    Safely evaluate an expression string
    """
    try:
        # Allow the use of 'pi' as a constant
        expr = expr.replace('pi', str(math.pi))
        node = ast.parse(expr, mode='eval').body
        return eval_(node)
    except (TypeError, SyntaxError, KeyError, ZeroDivisionError):
        return "Error"

def eval_(node):
    if isinstance(node, ast.Constant): # for python 3.8+
        return node.value
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        if type(node.op) not in operators:
            raise TypeError(node)
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        if type(node.op) not in operators:
            raise TypeError(node)
        return operators[type(node.op)](eval_(node.operand))
    elif isinstance(node, ast.Name) and node.id == 'pi':
        return math.pi
    else:
        raise TypeError(node)
