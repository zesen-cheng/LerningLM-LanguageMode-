"""第 36 课：端到端联调。运行：python demo.py"""

def lesson_36():
    request = {"model": "toy-model", "messages": [{"role": "user", "content": "你好"}], "request_id": "demo-1"}
    routes = {"toy-model": "deterministic-mock"}
    backend = routes[request["model"]]
    generated = "你好" if backend == "deterministic-mock" else "未实现"
    response = {"request_id": request["request_id"], "backend": backend, "text": generated}
    print("客户端→网关→模拟后端→客户端:", response)
    assert response["backend"] == "deterministic-mock"

if __name__ == '__main__':
    lesson_36()
