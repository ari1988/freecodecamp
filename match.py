def http_error(status_code):
    match status_code:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 498 | 499 | 491:
            return "Client Error"
        case 500:
            return "Internal Server Error"
        case 502:
            return "Bad Gateway"
        case 503:
            return "Service Unavailable"
        case _:
            return "Something's wrong with the internet"

for i in range(400, 504):
    print(f"{i}: {http_error(i)}")