.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running tests..."
	python -m pytest test.py -v

build:
	@echo "Building the Docker image..."
	docker build -t health-calculator-service:latest .

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf .pytest_cache

docker-run:
	@echo "Running the Docker container..."
	docker run -p 5000:5000 health-calculator-service:latest