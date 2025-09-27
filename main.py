
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import ast
import operator as op

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Expression(BaseModel):
    expression: str

# supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def eval_expr(expr):
    """
    Safely evaluate an expression string
    """
    try:
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
    else:
        raise TypeError(node)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/calculate")
async def calculate(expression: Expression):
    result = eval_expr(expression.expression)
    return {"result": result}