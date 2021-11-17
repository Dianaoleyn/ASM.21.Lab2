from app import app, routes

if __name__ == '__main__':
    if app.debug:
        app.run(debug=True)
    else:
        app.run(host='127.0.0.1')