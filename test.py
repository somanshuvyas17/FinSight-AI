import subprocess

prompt = "Say exactly: Hello Mr. Stark"

result = subprocess.run(
    ["ollama", "run", "llama3.2"],
    input=prompt,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

print("STDOUT:")
print(result.stdout)

print("\nSTDERR:")
print(result.stderr)

print("\nRETURN CODE:")
print(result.returncode)

