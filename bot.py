from flask import Flask, request  # Use Flask with uppercase "F"
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity

app = Flask(__name__)  # Correct Flask initialization

# Your Azure App ID and password
APP_ID = "d3628f7b-cc40-4d9b-8ed5-7a50799e6104"
APP_PASSWORD = "03S8Q~_.uJsj16pqJWLzC0XLfywkEKbQD_SUMcDC"

# Use BotFrameworkAdapterSettings to pass credentials
adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

@app.route("/api/messages", methods=["POST"])
async def messages():
    body = await request.get_json()
    activity = Activity().deserialize(body)
    context = TurnContext(adapter, activity)
    await context.send_activity("Hello from my bot!")
    return "OK"

if __name__ == "__main__":
    app.run(port=3978)
