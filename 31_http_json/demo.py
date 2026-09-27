"""第 31 课：HTTP/JSON 最小接口。运行：python demo.py"""

def lesson_31():
    import json
    request = {"method": "POST", "path": "/generate", "body": {"prompt": "我喜欢", "max_new_tokens": 2}}
    def handle(req):
        if req["method"] != "POST" or req["path"] != "/generate":
            return 404, {"error": "not_found"}
        if not isinstance(req["body"].get("prompt"), str):
            return 400, {"error": "invalid_prompt"}
        return 200, {"text": req["body"]["prompt"] + "苹果"}
    status, body = handle(request)
    print("本机无端口 HTTP/JSON 处理逻辑:", status, json.dumps(body, ensure_ascii=False))
    assert (status, body["text"]) == (200, "我喜欢苹果")

if __name__ == '__main__':
    lesson_31()
