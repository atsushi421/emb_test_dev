import bt2
import argparse


def option_parser() -> str:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--source_dir_path',
                            required=True,
                            type=str,
                            help='The path to source trace dir')
    args = arg_parser.parse_args()

    return args.source_dir_path


def main(source_dir_path):
    # Create a trace collection message iterator with this path.
    msg_it = bt2.TraceCollectionMessageIterator(source_dir_path)

    # Iterate the trace messages.
    for msg in msg_it:
        # `bt2._EventMessageConst` is the Python type of an event message.
        if type(msg) is bt2._EventMessageConst:
            # An event message holds a trace event.
            event = msg.event

            # Print event's name.
            print(event.name)


if __name__ == '__main__':
    source_dir_path = option_parser()
    main(source_dir_path)
