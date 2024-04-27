import subprocess

if __name__ == "__main__":
    scripts = ["single_thread.py", "multi_thread.py", "multi_process.py"]

    for script in scripts:
        subprocess.run(["python3", script])
