import time


class TimerService:

    def __init__(self):

        self.start_time = None

    def start(self):

        self.start_time = time.time()

    def reset(self):

        self.start_time = None

    def is_running(self):

        return self.start_time is not None

    def elapsed_seconds(self):

        if self.start_time is None:
            return 0

        return int(
            time.time() - self.start_time
        )

    def elapsed_formatted(self):

        total_seconds = self.elapsed_seconds()

        hours = total_seconds // 3600

        minutes = (
            total_seconds % 3600
        ) // 60

        seconds = total_seconds % 60

        return (
            f"{hours:02}:"
            f"{minutes:02}:"
            f"{seconds:02}"
        )

    def elapsed_precise(self):

        if self.start_time is None:
            return 0.0

        return (
            time.time()
            - self.start_time
        )