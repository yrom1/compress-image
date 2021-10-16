import subprocess

with open('TEST-README.md', 'w') as f:
    def write_subprocess_to_markdown(cmd: str) -> str:
        f.write('```')
        f.write(cmd)
        f.write('\n')
        result = subprocess.run(cmd.split(' '), capture_output=True, text=True)
        f.write(result.stdout)
        f.write(result.stderr)
        f.write('```\n')

    f.write('# Help\n')
    write_subprocess_to_markdown('python3 compress.py --help')

    f.write('# Usage Examples\n')
    write_subprocess_to_markdown('python3 compress.py')
