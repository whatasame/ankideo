import subprocess
from typing import List

from aqt import *

from gui.ffmpeg_output_dialog import FFmpegOutputDialog
from .commands import FFmpegCommand


class FFmpegWorker(QObject):
    output_ready = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, command: FFmpegCommand):
        super().__init__()
        self.command = command
        self.is_cancelled = False

    def run(self):
        process = subprocess.Popen(
            self.command.to_full_command(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        while True:
            if self.is_cancelled:
                process.terminate()
                break
            line = process.stdout.readline()
            if not line:
                break
            self.output_ready.emit(line.strip())
        process.wait()
        self.finished.emit()

    def cancel(self):
        self.is_cancelled = True


class FFmpegManager:
    def __init__(
            self,
            commands: List[FFmpegCommand],
            on_all_tasks_completed: Callable[[List[str]], None],
            dialog_parent=None
    ):
        self.commands = commands
        self.on_all_tasks_completed = on_all_tasks_completed
        self.dialog_parent = dialog_parent

        self.thread_pool = QThreadPool()
        self.workers = []
        self.tasks_completed = 0
        self.total_tasks = len(commands)
        self.output_dialog = FFmpegOutputDialog(self.total_tasks, self.dialog_parent)

    def start_ffmpeg_tasks(self):
        self.tasks_completed = 0
        self.workers = []

        self.output_dialog.show()

        for i, command in enumerate(self.commands):
            worker = FFmpegWorker(command)
            worker.output_ready.connect(lambda text, idx=i: self.output_dialog.append_output(text, idx))
            worker.finished.connect(lambda idx=i: self.task_finished(idx))
            self.workers.append(worker)
            self.thread_pool.start(worker.run)

    def task_finished(self, index):
        self.output_dialog.task_completed(index)
        self.tasks_completed += 1

        if self.tasks_completed == self.total_tasks:
            self.on_all_tasks_completed([worker.command.output_path for worker in self.workers])

    def cancel_all_tasks(self):
        for worker in self.workers:
            worker.cancel()
