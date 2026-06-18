from flask import Flask, request, render_template
from ollama import chat

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    
    user_message = ""
    ai_message = ""

    
    if request.method == "POST":

        
        user_message = request.form.get("message", "").strip()

       
        if user_message:

            response = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful, friendly, and professional AI assistant. "
                            "Give well-formatted answers using paragraphs, bullet points, "
                            "and numbering whenever appropriate."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            ai_message = response["message"]["content"]

    # Render the page
    return render_template(
        "home.html",
        user_message=user_message,
        message=ai_message
    )


if __name__ == "__main__":
    app.run(debug=True)