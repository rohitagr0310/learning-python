import subprocess

if __name__ == "__main__":
    scripts = ["multi_threading.py", "normal.py", "multi_processing.py"]

    for script in scripts:
        subprocess.run(["python3", script])
