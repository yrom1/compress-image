import subprocess

TEST_IMAGE_FILEPATH = "/home/ryan/Downloads/image.png"

with open("README.md", "w") as f:

    def write_subprocess_to_markdown(command_list: list[str]) -> str:
        f.write("```\n")
        f.write("$ " + " ".join(command_list))
        f.write("\n")
        result = subprocess.run(command_list, capture_output=True, text=True)
        f.write(result.stdout)
        f.write(result.stderr)
        f.write("```\n")

    f.write("# Help\n")
    write_subprocess_to_markdown(["python3", "compress.py", "--help"])
    f.write("# Usage Examples\n")
    write_subprocess_to_markdown(["python3", "compress.py"])
    write_subprocess_to_markdown(["python3", "compress.py", TEST_IMAGE_FILEPATH])
    write_subprocess_to_markdown(["python3", "compress.py", TEST_IMAGE_FILEPATH, "-v"])
    write_subprocess_to_markdown(["python3", "compress.py", TEST_IMAGE_FILEPATH, "-s"])
    write_subprocess_to_markdown(
        ["python3", "compress.py", TEST_IMAGE_FILEPATH, "-v", "-q", "50"]
    )