from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Basic HTML template for the calculator
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form action="/calculate" method="get">
        <input type="text" name="num1" placeholder="Number 1" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="text" name="num2" placeholder="Number 2" required>
        <button type="submit">Calculate</button>
    </form>
    <div>
        <h2>Result: {{ result }}</h2>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root(result: str = ""):
    return HTMLResponse(content=html_content.replace("{{ result }}", result))

@app.get("/calculate")
async def calculate(num1: float, num2: float, operation: str):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = num1 / num2
    else:
        return {"error": "Invalid operation"}

    return HTMLResponse(content=html_content.replace("{{ result }}", str(result)))

