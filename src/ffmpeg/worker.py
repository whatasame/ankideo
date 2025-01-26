import subprocess
import threading

from aqt import mw
from aqt.qt import *

from ..core.utils import safe_remove_file
from ..ffmpeg.commands import FFmpegCommand
from ..gui.ffmpeg_output_dialog import FFmpegOutputDialog


class FFmpegWorker:
    """
    If you want to control UI elements from a new thread, must use `mw.taskman.run_on_main()` method.
    """

    def __init__(self, ffmpeg_command: FFmpegCommand, callback: Callable[[str], None]):
        self.ffmpeg_command = ffmpeg_command
        self.callback = callback
        self.process = None
        self.thread = None
        self.output_dialog = None

    def run(self):
        self.output_dialog = FFmpegOutputDialog(mw)
        self.output_dialog.cancel_button.clicked.connect(self._on_cancel)
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
                mw.taskman.run_on_main(lambda: self._on_success())
            else:
                mw.taskman.run_on_main(
                    lambda: self._on_failure(f"FFmpeg process returned code {self.process.returncode}"))
        except Exception as e:
            error_message = str(e)
            mw.taskman.run_on_main(lambda: self._on_failure(error_message))

    def _update_log(self, text):
        mw.taskman.run_on_main(lambda: self.output_dialog.text_edit.appendPlainText(text.strip()))

    def _on_success(self):
        self._update_log("[Ankidia] FFmpeg process has finished successfully.")
        self.callback(self.ffmpeg_command.output_path)
        self.output_dialog.close()

    def _on_failure(self, error_msg):
        """
        When passing a function to `clicked.connect`, use a lambda to pass arguments.

        Because when the button is clicked, `FFmpegWorker.run()` is already finished.
        """
        self._update_log(f"[Ankidia] An error occurred: {error_msg}")

        self.output_dialog.cancel_button.setText("Ok")
        self.output_dialog.cancel_button.clicked.disconnect()

        self.output_dialog.cancel_button.clicked.connect(lambda: self._handle_failure_confirm())

    def _handle_failure_confirm(self):
        safe_remove_file(self.ffmpeg_command.output_path)

        self.output_dialog.close()

    def _on_cancel(self):
        if self.process:
            self.process.terminate()
            self._update_log("[Ankidia] FFmpeg process has been canceled.")

            safe_remove_file(self.ffmpeg_command.output_path)

            self.output_dialog.close()
