


if __name__ == '__main__':
    from group import group
    from app import app
    import routes
else:
    from .app import app
    from .group import group
    import routes



if __name__ == "__main__":
    app.run(debug=True)
