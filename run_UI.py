from json import load
from os import listdir
from os.path import isdir
from os.path import isfile
from os.path import join
from chess_plot import chess_plot
from model_run import define_path

#from show_svg import viewer

def select_run_config():
    print('Please select run config by entering the number:')
    run_configs = listdir('./run_configs')
    i = 0
    for file in run_configs:
        print('[%s] %s' % (i, file))
        i += 1
    selected_index = int(input())
    return run_configs[selected_index]


def read_run_config(run_config_path):
    with open(run_config_path, 'r') as config_file:
        config = load(config_file)
        return config['pgn_file_paths']


def sanitize_pgn_file_paths(pgn_file_paths):
    sanitized_paths = list()
    for o in pgn_file_paths:
        if isdir(o):
            files = listdir(o)
            print('Searching in dir %s for pgn files' % o)
            for f in files:
                full_path = join(o, f)
                if isfile(full_path) and full_path.endswith('.pgn'):
                    sanitized_paths.append(full_path)
        elif isfile(o):
            if o.endswith('.pgn'):
                sanitized_paths.append(o)
            else:
                print('Ignoring path %s due to wrong file ending' % o)
        else:
            print('Ignoring path %s due to not being a file or directory')

    return sanitized_paths


def main():
    run_config = join('./run_configs/', select_run_config())
    pgn_file_paths = read_run_config(run_config)
    pgn_file_paths = sanitize_pgn_file_paths(pgn_file_paths)
    print(pgn_file_paths)
    define_path(pgn_file_paths)
    chess_plot(pgn_file_paths[0])

if __name__ == "__main__":
    main()
