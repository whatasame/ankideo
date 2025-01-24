import subprocess
import threading

from aqt import mw
from aqt.qt import *

from ..ffmpeg.commands import ConvertFFmpegCommand


class FFmpegOutputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("FFmpeg log")
        self.setMinimumWidth(600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.cancel_button = QPushButton("Cancel")
        layout.addWidget(self.cancel_button)


class FFmpegWorker:
    def __init__(self, ffmpeg_command: ConvertFFmpegCommand, callback: Callable[[str], None]):
        self.ffmpeg_command = ffmpeg_command
        self.callback = callback
        self.process = None
        self.thread = None
        self.output_dialog = None

    def run(self):
        self.output_dialog = FFmpegOutputDialog(mw)
        self.output_dialog.cancel_button.clicked.connect(self.cancel)
        self.output_dialog.show()

        self.thread = threading.Thread(target=self._run_ffmpeg)
        self.thread.start()

    def _run_ffmpeg(self):
        try:
            self.process = subprocess.Popen(
                self.ffmpeg_command.to_full_command(),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )

            for line in self.process.stdout:
                self._update_log(line)

            self.process.wait()

            if self.process.returncode == 0:
                mw.taskman.run_on_main(lambda: self.callback(self.ffmpeg_command.output_path))
                self._update_log(f"[Ankidia] FFmpeg process has finished successfully.")
            else:
                self._update_log(f"[Ankidia] FFmpeg process has failed with return code {self.process.returncode}")
        except Exception as e:
            self._update_log(f"[Ankidia] An error occurred: {str(e)}")
        finally:
            pass
            # TODO:
            #  mw.taskman.run_on_main(self.output_dialog.close)

    def _update_log(self, text):
        """
        An operation with UI should be run on the main thread.

        So use `mw.taskman.run_on_main` to run a function on the main thread.
        """
        mw.taskman.run_on_main(lambda: self.output_dialog.text_edit.appendPlainText(text.strip()))

    def cancel(self):
        if self.process:
            self.process.terminate()
            self._update_log("[Ankidia] FFmpeg process has been canceled.")
