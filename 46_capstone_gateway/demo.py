"""第 46 课：结课：接口与网关。运行：python demo.py"""

def lesson_46():
    import json
    model_id = "tiny-gpt-mock"
    request = {"model": model_id, "messages": [{"role": "user", "content": "你好"}], "stream": False}
    def gateway(req):
        if req.get("model") != model_id:
            return 404, {"error": "model_not_found"}
        return 200, {"model": model_id, "text": "你好！", "backend": "deterministic-mock"}
    status, body = gateway(request)
    stream_chunks = ["data: " + json.dumps({"delta": c}, ensure_ascii=False) + "\n\n" for c in body["text"]]
    print("非流式:", status, body)
    print("流式拼接:", "".join(json.loads(chunk[6:])["delta"] for chunk in stream_chunks))
    assert status == 200 and body["backend"] == "deterministic-mock"

if __name__ == '__main__':
    lesson_46()
