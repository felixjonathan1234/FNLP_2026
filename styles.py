def load_css():
    return """
    <style>
    body {
        background: linear-gradient(to right, #1e3c72, #2a5298);
    }

    .user-bubble {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
        text-align: right;
    }

    .bot-bubble {
        background-color: #f1f0f0;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
    }

    .product-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        margin: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    .title {
        text-align: center;
        font-size: 40px;
        color: white;
        font-weight: bold;
    }
    </style>
    """