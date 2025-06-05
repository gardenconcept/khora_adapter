import os
import subprocess


def should_include(file_path):
    parts = file_path.split(os.sep)
    return (
        file_path.endswith(".py")
        and "__pycache__" not in parts
        and not any(part.startswith(".") for part in parts)
    )


def main():
    combined = []
    for root, dirs, files in os.walk(os.getcwd()):
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".") and d != "__pycache__"
        ]
        for file in files:
            file_path = os.path.join(root, file)
            if should_include(file_path):
                combined.append(f"\n# FILE: {file_path}\n")
                with open(
                    file_path,
                    encoding="utf-8",
                    errors="ignore",
                ) as f:
                    combined.append(f.read())
    joined = "".join(combined)
    subprocess.run(
        "clip", input=joined.encode("utf-8"), shell=True
    )
    print("Copied combined Python code to clipboard.")


if __name__ == "__main__":
    main()
