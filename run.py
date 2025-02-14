from app import createApp

app = createApp()

app.secret_key = "socios"

if __name__ == '__main__':
    app.run(debug=True)