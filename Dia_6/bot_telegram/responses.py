
def sample_response(input_text):
    # Pelo python ser case sensitive
    user_message = str(input_text).lower()

    if user_message in ("oi","ola","olá"):
        return "Eai blz?"
    elif "canal" in user_message:
        return "https://www.youtube.com/watch?v=TDoKNIHv0rA&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=16"
    else:
        return "não estou entendendo você tente novamente"
    