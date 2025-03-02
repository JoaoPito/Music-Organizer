from pathlib import Path
import argparse

def get_list_of_subdirectories(path: Path):
    return [subdir for subdir in path.iterdir() if subdir.is_dir()]

def get_first_letter_counts(pathlist: list[Path]):
    initials = [subdir.name[0].upper() for subdir in pathlist]
    return {initial: initials.count(initial) for initial in set(initials)}

def group_by_frequency(frequency: dict[str, int], 
                       target_group_size=20):
    groups = [([],0)]
    for initial, count in sorted(frequency.items(), key=lambda x: x[0]):
        group = groups.pop() if groups[-1][1] + count < target_group_size else ([],0)
        groups.append((group[0] + [initial], group[1] + count))
    return groups

def group_directories_by_initial(subdirs: list[Path], 
                                 groups: list[list[str]], 
                                 output_path: Path):
    output_path.mkdir(parents=True, exist_ok=True)
    
    groups_upper = [[i.upper() for i in group[0]] for group in groups]
    
    for group_initials in groups_upper:
        group_dir_name = f"{group_initials[0]}-{group_initials[-1]}".upper()
        group_dir_path = output_path / group_dir_name
        group_dir_path.mkdir(exist_ok=True)
        
        for subdir in subdirs:
            if subdir.name[0].upper() in [i.upper() for i in group_initials]:
                subdir.rename(group_dir_path / subdir.name)
                print(f"Moved '{subdir}' to '{group_dir_path / subdir.name}'")

def main():
    parser = argparse.ArgumentParser(description='Organize music directories by initial letter.')
    parser.add_argument('input_path', type=Path, help='Path to the input directory containing music subdirectories.')
    parser.add_argument('output_path', type=Path, help='Path to the output directory where grouped directories will be created.')
    parser.add_argument('--max_size', type=int, default=20, help='Target size for each group of directories.')
    
    args = parser.parse_args()
    
    input_path = args.input_path
    output_path = args.output_path
    max_group_size = args.max_size
    
    subdirs = get_list_of_subdirectories(input_path)
    letter_counts = get_first_letter_counts(subdirs)
    groups = group_by_frequency(letter_counts, target_group_size=max_group_size)
    
    if len(groups) <= 1 or groups[0][1] == 0:
        print(f"Could not make any groups\n{groups}")
        return
    
    group_directories_by_initial(subdirs, groups, output_path)
    
if __name__ == '__main__':
    main()