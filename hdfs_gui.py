import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print("Error", result.stderr)

def list_files():
    path = input("Enter HDFS path (default '/'): ") or "/"
    run_cmd(["hdfs", "dfs", "-ls", path])

def upload_file():
    local = input("Enter local file path: ")
    hdfs = input("Enter target HDFS path (e.g. /user/hadoop/): ")
    run_cmd(['hdfs', 'dfs', '-put', local, hdfs])

def download_file():
    hdfs = input("Enter HDFS file path: ")
    local = input("Enter target local path: ")
    run_cmd(['hdfs', 'dfs', '-get', hdfs, local])

def move_file():
    hdfs_source = input("Enter HDFS file source path:")
    hdfs_destination = input("Enter HDFS file destination path:")
    run_cmd(['hdfs', 'dfs', '-mv', hdfs_source, hdfs_destination])

def copy_file():
    hdfs_source = input("Enter HDFS file source path:")
    hdfs_destination = input("Enter HDFS file destination path:")
    run_cmd(['hdfs', 'dfs', '-cp', hdfs_source, hdfs_destination])

def delete_file():
    hdfs = input("Enter HDFS file path to delete: ")
    run_cmd(['hdfs', 'dfs', '-rm', hdfs])

def main():
    print("\n--- HDFS CLI Menu ---")
    print("1. List files")
    print("2. Upload file")
    print("3. Download file")
    print("4. Move file")
    print("5. Copy file")
    print("6. Delete file")

    choice = input("Choose an option: ")

    if choice == '1':
        list_files()
    elif choice == '2':
        upload_file()
    elif choice == '3':
        download_file()
    elif choice == '4':
        move_file()
    elif choice == '5':
        copy_file()
    elif choice == '6':
        delete_file()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
