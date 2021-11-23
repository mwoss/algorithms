"""
Implement rate limiter that would allow no more than 5 req per 2 seconds for given user.
Aim for reusable and configurable implementation.
"""
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Request:
    client_id: str  # it could be IP, some unique internal ID
    data: object


class RateLimiter:

    def __init__(self, req_cap: int, time_window_length_ms: int):
        self._client_limits = defaultdict(lambda: deque(maxlen=req_cap))
        self._req_cap = req_cap
        self._time_window_length_ms = time_window_length_ms

    def limit(self, request: Request) -> Tuple[Request, int]:
        client_req_queue = self._client_limits[request.client_id]
        request_timestamp = time.time()

        if len(client_req_queue) < self._req_cap:
            client_req_queue.append(request_timestamp)
            return request, 200

        # repetition just for code clarity
        if self._time_window_length_ms < request_timestamp - client_req_queue[0]:
            client_req_queue.append(request_timestamp)
            return request, 200

        return request, 429


if __name__ == '__main__':
    rl = RateLimiter(5, 2000)
    print(rl.limit(Request("1", {})))
    print(rl.limit(Request("1", {})))
    print(rl.limit(Request("1", {})))
    print(rl.limit(Request("1", {})))
    print(rl.limit(Request("1", {})))
    print(rl.limit(Request("1", {})))  # we should expect code 429
