# Runs the code for custom input tests
run:
	python3 src/main.py

# Cleans the project directory of temporary files
clean:
	rm -rf src/components/__pycache__
	rm -rf .DS_Store