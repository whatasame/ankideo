import select
import subprocess
from typing import List

from aqt import *

from .command import FFmpegCommand
from ..gui.worker_output_dialog import WorkerOutputDialog


class FFmpegWorker(QObject):
    output_ready = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, command: FFmpegCommand):
        super().__init__()
        self.command = command
        self.process = None
        self.is_cancelled = False

    def run(self):
        with subprocess.Popen(
                self.command.to_full_command(),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
        ) as self.process:
            while self.process.poll() is None:
                ready, _, _ = select.select([self.process.stdout], [], [], 0.1)
                if ready:
                    line = self.process.stdout.readline()
                    if line:
                        self.output_ready.emit(line.strip())

            if not self.is_cancelled:
                self.output_ready.emit(f"\n[Ankidia] Task completed. Result saved to {self.command.output_path}")
                self.finished.emit()

        # TODO: handle errors

    def cancel(self):
        self.is_cancelled = True
        if self.process:
            self.process.terminate()

        if self.command.output_path.exists():
            os.remove(self.command.output_path)


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

        self.output_dialog = WorkerOutputDialog(
            parent=self.dialog_parent,
            num_tasks=self.total_tasks,
            on_cancel=self.cancel_all_tasks
        )

    def start_ffmpeg_tasks(self):
        self.tasks_completed = 0
        self.workers = []

        self.output_dialog.show()

        for i, command in enumerate(self.commands):
            worker = FFmpegWorker(command)
            worker.output_ready.connect(lambda text, idx=i: self.output_dialog.append_output(idx, text))
            worker.finished.connect(lambda: self.task_finished())
            self.workers.append(worker)

            self.thread_pool.start(worker.run)

    def task_finished(self) -> None:
        self.tasks_completed += 1  # TODO: race condition?

        if self.tasks_completed == self.total_tasks:
            self.on_all_tasks_completed([worker.command.output_path for worker in self.workers])
            self.output_dialog.close()

    def cancel_all_tasks(self):
        for worker in self.workers:
            worker.cancel()
