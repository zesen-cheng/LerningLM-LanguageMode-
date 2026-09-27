"""第 35 课：网关与可观察性。运行：python demo.py"""

def lesson_35():
    keys = {"course-key": "student"}
    quota = {"student": 2}
    def authorize(key):
        identity = keys.get(key)
        if identity is None:
            return 401
        if quota[identity] <= 0:
            return 429
        quota[identity] -= 1
        return 200
    statuses = [authorize("wrong"), authorize("course-key"), authorize("course-key"), authorize("course-key")]
    print("鉴权/限流状态码:", statuses)
    assert statuses == [401, 200, 200, 429]

if __name__ == '__main__':
    lesson_35()
