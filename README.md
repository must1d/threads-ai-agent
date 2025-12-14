# Threads AI Agent

AI agent for creating Threads posts using web scraping and AWS Bedrock.

## Installation

### Prerequisites
- Python 3.10+
- PDM (Python Dependency Manager)

### Install PDM
```bash
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
```

### Install the project
```bash
# Clone the repository
git clone <your-repo-url>
cd threads-ai-agent

# Install dependencies
pdm install

# Install Playwright browsers
pdm run playwright install chromium
```

## Usage

### Run the AI Agent
```bash
pdm run threads-agent <username>
```

The agent will:
1. Analyze the user's Threads posts and replies
2. Study their writing style, tone, and patterns
3. Generate Thread suggestions mimicking their style
4. Save output to `outputs/<username>_<timestamp>.md`

## Development

### Install development dependencies
```bash
pdm install -d
```

### Run tests
```bash
pdm run pytest
```

### Format code
```bash
pdm run black .
```

## Configuration

Make sure you have AWS credentials configured for Bedrock access:
- AWS CLI configured
- Appropriate IAM permissions for Bedrock
