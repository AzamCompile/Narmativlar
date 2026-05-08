class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # requestdan oldin
        path = request.path
        method = request.method

        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = "Anonymous"

        print("Path:", path)
        print("Method:", method)
        print("User:", user)
        print("-" * 30)

        response = self.get_response(request)
        return response