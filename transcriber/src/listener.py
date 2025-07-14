from transcriber.src.utils.mouse_recorder import record_mouse, print_record

if __name__ == "__main__":
    mouse_records = record_mouse()
    print_record(mouse_records)