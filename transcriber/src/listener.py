import os

from public_configs.project_config import get_project_root
from transcriber.src.utils.mouse_recorder import record_mouse, print_record, export_to_file

file_path = os.path.join(get_project_root(), "transcriber", "test", "resources", "json", "mouse_event.json")

if __name__ == "__main__":
    mouse_records = record_mouse()
    print_record(mouse_records)

    # export_to_file(mouse_records, file_path)