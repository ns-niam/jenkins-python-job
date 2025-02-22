import sys

if len(sys.argv) < 2:
    print("Error: No names provided.")
    sys.exit(1)

print("Names from command-line arguments:")
for name in sys.argv[1:]:
    print(name)
