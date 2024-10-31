def headers(token=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://app.production.tonxdao.app",
        "Referer": "https://app.production.tonxdao.app/",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers
