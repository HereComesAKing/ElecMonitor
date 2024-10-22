from os import getcwd, path
import win10toast

toaster = win10toast.ToastNotifier()

working_dir = getcwd()

toast_title = "电费监控"
toast_icon = path.join(working_dir, "elecmonitor.ico")
toast_warning_icon = path.join(working_dir, "warning.ico")


def toast_info(text: str) -> None:
    toaster.show_toast(toast_title, text, toast_icon)


def toast_warn(text: str) -> None:
    toaster.show_toast(toast_title, text, toast_warning_icon)
